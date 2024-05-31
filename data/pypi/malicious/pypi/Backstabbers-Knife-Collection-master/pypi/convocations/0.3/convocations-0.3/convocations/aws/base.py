import json
import os
import webbrowser
from datetime import datetime
from getpass import getuser
from hashlib import sha1
from time import sleep
from time import time
from typing import Optional, Tuple, Any, List, Dict
from typing import Mapping

import boto3.session
import requests
from dateutil.parser import parse as parse_time
import pytz
from botocore.utils import SSOTokenLoader
from botocore.credentials import JSONFileCache
from botocore.exceptions import ClientError
from raft import Context
from raft.tasks import Task
from ..base.utils import notice, notice_end, get_context_value

g_cache_dir_noticed = False


def cache_dir():
    """
    gets the aws cache dir, which is user specific as ~/.aws/sso/cache
    and ensures that the directories exist with permissions 0700
    all the way down
    """
    global g_cache_dir_noticed
    if not g_cache_dir_noticed:
        notice('checking for cache dir')
    d = os.path.expanduser('~')
    dirs = [ '.aws', 'sso', 'cache' ]
    rg = []
    for x in dirs:
        d = os.path.join(d, x)
        rg.append(d)
    if not os.path.exists(d):
        for x in rg:
            os.makedirs(x, 0o700, exist_ok=True)
    if not g_cache_dir_noticed:
        notice_end(d, 'green')
        g_cache_dir_noticed = True
    return d


def client_credentials(sso_oidc, force=False):
    """
    performs the first step of the 7-step oidc handshake by
    registering the client and caching client credentials
    :param sso_oidc: the boto3 sso-oidc client
    :param bool force: specify this flag to bypass the cache
    :return: dict
    """
    cache = SsoTokenSaver('convocations')
    message = 'client credentials'
    expiration_key = 'clientSecretExpiresAt'
    if not force:
        creds = cache.load(expiration_key, message) or {}
        if creds:
            return creds
    notice('registering client')
    creds = sso_oidc.register_client(
        clientName='convocations',
        clientType='public',
    )
    notice_end()
    notice('caching response')
    cache.save(creds)
    notice_end()
    return creds


class SsoTokenSaver(SSOTokenLoader):
    """
    class that caches sso client credentials and device authorizations
    in the aws sso cache dir so that cached credentials play nicely with
    boto3 and botocore
    """
    def __init__(self, start_url):
        super().__init__()
        self.token_cache = JSONFileCache(cache_dir())
        self.start_url = start_url
        try:
            self.cache_key = self._generate_cache_key(start_url)
        except:
            self.cache_key = self._generate_cache_key(start_url, None)

    def save(self, response):
        """
        caches a token response or a client registration response
        :param dict response: the dict response returned from a call
            to `register_client` or `create_token`
        :return:
        """
        cache_key = self.cache_key
        self.token_cache[cache_key] = response

    def load(self, expiration_key, message='checking expiration'):
        """
        loads the cached response from the cache and checks its expiration.
        if the response is still valid (i.e., not expired), the response is
        returned.  Otherwise we return None
        :param expiration_key: the key in the response with expiration
        :param message: the notification message displayed as we check cache
        :return: the cached credentials, if valid, or none
        """
        try:
            notice(message)
            creds = self.token_cache[self.cache_key]
            expires_at = creds.get(expiration_key)
            if expires_at:
                now = int(time())
                delta = expires_at - now
                is_current = delta > 0
                if is_current:
                    notice_end(f'{delta / 3600:0.2f}h', 'green')
                    return creds
            notice_end('expired')
        except KeyError:
            notice_end('miss')
        return None


class SsoCredentialSaver:
    def __init__(self, start_url, role_name, account_id):
        self.token_cache = JSONFileCache(cache_dir())
        self.start_url = start_url
        self.role_name = role_name
        self.account_id = account_id
        self.cache_key = self.generate_cache_key()

    def generate_cache_key(self):
        args = {
            'startUrl': self.start_url,
            'roleName': self.role_name,
            'accountId': self.account_id,
        }
        # NOTE: It would be good to hoist this cache key construction logic
        # into the CachedCredentialFetcher class as we should be consistent.
        # Unfortunately, the current assume role fetchers that sub class don't
        # pass separators resulting in non-minified JSON. In the long term,
        # all fetchers should use the below caching scheme.
        args = json.dumps(args, sort_keys=True, separators=(',', ':'))
        h = sha1(args.encode('utf-8')).hexdigest().replace(':', '_')
        return h.replace(os.path.sep, '_')

    def _parse_timestamp(self, timestamp_ms):
        from pytz import utc
        # fromtimestamp expects seconds so: milliseconds / 1000 = seconds
        timestamp_seconds = timestamp_ms / 1000.0
        timestamp = datetime.fromtimestamp(timestamp_seconds, utc)
        return timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    def save(self, credential_response):
        cache_key = self.cache_key
        credentials = credential_response['roleCredentials']
        self.token_cache[cache_key] = {
            'ProviderType': 'sso',
            'Credentials': {
                'AccessKeyId': credentials['accessKeyId'],
                'SecretAccessKey': credentials['secretAccessKey'],
                'SessionToken': credentials['sessionToken'],
                'Expiration': self._parse_timestamp(credentials['expiration']),
                'ExpirationTime': credentials['expiration'],
            }
        }

    def load(self):
        cache_key = self.cache_key
        try:
            notice('cached role creds')
            creds = self.token_cache[cache_key]
            creds = creds.get('Credentials') or {}
            expiration = creds.get('Expiration')
            expiration = parse_time(expiration)
            now = datetime.now(pytz.utc)
            delta = (expiration - now).total_seconds()
            is_current = delta > 0
            if is_current:
                notice_end(f'{delta / 3600:0.2f}h', 'green')
                return creds
            notice_end('expired')
            return None
        except KeyError:
            notice_end('not found')
            return None


def device_authorization(sso_oidc, client_creds, start_url, force=False):
    """
    performs steps 2-4 of the 7-step oidc handshake by performing the
    device authorization, redirecting the user to the sso sign-in page,
    and then exchanging the device auth for an access token once sign in
    is complete and authorized
    :param sso_oidc: the boto3 sso-oidc client
    :param client_creds: the client credentials response from `register_client`
    :param start_url: the sso start url specified in the profile or the context
    :param force: specify this flag to bypass use of cached credentials
    :return:
    """
    cache = SsoTokenSaver(start_url)
    message = 'cached device authorization'
    expiration_key = 'accessTokenExpiration'
    if not force:
        creds = cache.load(expiration_key, message) or {}
        if creds:
            return False, creds
    notice('device authorization')
    response = sso_oidc.start_device_authorization(
        clientId=client_creds['clientId'],
        clientSecret=client_creds['clientSecret'],
        startUrl=start_url,
    )
    device_code = response['deviceCode']
    url = response['verificationUriComplete']
    expires_in = response['expiresIn']
    interval = response['interval']
    interval = max(interval, 7)
    notice_end(f'{url} / {expires_in} / {interval}')
    webbrowser.open(url, autoraise=True)
    for n in range(1, expires_in // interval + 1):
        notice(f'poll #{n}')
        sleep(interval)
        try:
            creds = sso_oidc.create_token(
                grantType='urn:ietf:params:oauth:grant-type:device_code',
                deviceCode=device_code,
                clientId=client_creds['clientId'],
                clientSecret=client_creds['clientSecret'],
            )
            creds['accessTokenExpiration'] = creds['expiresIn'] + time()
            creds['expiresAt'] = creds['accessTokenExpiration']
            cache.save(creds)
            notice_end()
            return True, creds
        except sso_oidc.exceptions.AuthorizationPendingException:
            notice_end('wait')
    return False, None


def get_role(sso, role, account_id, device_auth):
    """
    performs steps 5 of the 7-step oidc handshake by performing the
    role selection automatically. we will choose the first role available
    alphabetically if no role is specified
    :param sso: the boto3 sso client
    :param device_auth: the device auth response from `create_token`
    :param role: the role to choose, can be None to just pick the first role
    :param account_id: the account id we are signing into
    :return: the role we should use
    """
    notice('listing account roles')
    access_token = device_auth['accessToken']
    try:
        account_roles = sso.list_account_roles(
            accessToken=access_token,
            accountId=account_id,
        )
    except sso.exceptions.UnauthorizedException:
        notice_end('refresh token')
        return None
    roles = account_roles['roleList']
    all_roles = [ x['roleName'] for x in roles ]
    if 'AWSOrganizationsFullAccess' in all_roles:
        all_roles.remove('AWSOrganizationsFullAccess')
    all_roles.sort(key=lambda lx: lx.lower())
    if role and role not in all_roles:
        notice_end(f'could not find {role}.  Please try: {", ".join(all_roles)}')
        return None
    role = role or all_roles[0]
    notice_end(f'{role} / {", ".join(all_roles)}')
    return role


def get_role_creds(sso, device_auth, account_id, start_url, role, force=False):
    """
    performs step 6 of the 7-step oidc handshake which is exchanging the
    access token for the role credentials we can use.

    the response will be formatted as:

    ```
    {
        'AccessKeyId': 'AK.....',
        'SecretAccessKey': '01...',
        'SessionToken': '....',
        'Expiration': '2022-09-10T10:00:00'
    }
    ```

    :param sso: the boto3 sso client
    :param device_auth: the response from a previous call to `create_token`
    :param account_id: the account id we are signing into
    :param start_url: the start_url that initiates the oidc process
    :param role: the role that we are assuming
    :param force: specify this flag to bypass the cache
    :return: the cached credential formatted response to `get_role_credentials`
    """
    cache = SsoCredentialSaver(start_url, role, account_id)
    if not force:
        creds = cache.load() or {}
        if creds:
            return creds
    notice(f'getting credentials for {role}')
    cache = SsoCredentialSaver(start_url, role, account_id)
    access_token = device_auth['accessToken']
    creds = sso.get_role_credentials(
        roleName=role,
        accountId=account_id,
        accessToken=access_token,
    )
    cache.save(creds)
    notice_end()
    return cache.load()


def unpack_sso_config(ctx: Context, sso_config: dict, role: str) -> Tuple[str, str, str, str]:
    """
    values in the context are prioritized over values in the aws config
    """
    account_id = get_context_value(ctx, 'aws.account_id')
    account_id = account_id or get_context_value(ctx, 'aws.sso_account_id')
    account_id = account_id or sso_config.get('sso_account_id')
    account_id = f'{account_id}'
    sso_region = get_context_value(ctx, 'aws.sso_region')
    sso_region = sso_region or sso_config.get('sso_region')
    start_url = get_context_value(ctx, 'aws.start_url')
    start_url = start_url or sso_config.get('sso_start_url')
    role = role or get_context_value(ctx, 'aws.role')
    role = role or sso_config.get('sso_role_name')
    return account_id, sso_region, start_url, role


def make_sso_session(
        ctx: Optional[Context] = None,
        role: Optional[str] = None,
        session: Optional[boto3.session.Session] = None,
        profile: Optional[str] = None,
        force_sso: Optional[bool] = False,
        sso_config: Optional[dict] = None) -> Optional[boto3.session.Session]:
    """
    performs the 7-step oidc handshake to create an sso session with aws.
    see explanation here https://stackoverflow.com/a/71850591/6043170
    """
    from botocore.session import Session as CoreSession
    from boto3 import Session
    if session:
        return session
    if profile and not sso_config:
        core_session = CoreSession(profile=profile)
        profiles = core_session.full_config.get('profiles', {})
        sso_config = profiles.get(profile, {})
    sso_config = sso_config or {}
    t = unpack_sso_config(ctx, sso_config, role)
    account_id, sso_region, start_url, role = t
    region = get_context_value(ctx, 'aws.region')
    profile = profile or get_context_value(ctx, 'aws.profile')

    session = Session(region_name=sso_region)
    sso_oidc = session.client('sso-oidc')
    client_creds = client_credentials(sso_oidc, force_sso)
    reauth, device_auth = device_authorization(
        sso_oidc, client_creds, start_url, force_sso)
    if not device_auth:
        return None
    sso = session.client('sso')
    role = get_role(sso, role, account_id, device_auth)
    if not role:
        return None
    role_creds = get_role_creds(
        sso, device_auth,
        account_id, start_url, role,
        force_sso or reauth)
    secret_access_key = role_creds['SecretAccessKey']
    access_key_id = role_creds['AccessKeyId']
    session = Session(
        region_name=region,
        profile_name=profile,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        aws_session_token=role_creds['SessionToken'],
    )
    get_account_id(session)
    get_alias(session)
    return session


def get_account_id(session: boto3.session.Session) -> Optional[str]:
    """
    gets the account id we are signed into and caches the result
    as an attribute on the `session` object
    :param session: a boto3.session.Session object
    :return str: the aws account id (usually a 12-digit number)
    """
    account_id = getattr(session, 'account_id', None)
    if not account_id:
        sts = session.client('sts')
        notice('account id')
        data = sts.get_caller_identity()
        account_id = session.account_id = data['Account']
        notice_end(data['Account'], 'yellow', attrs=[ 'bold' ])
        notice('username')
        session.whoami = data['Arn'].rsplit('/', 1)[-1]
        notice_end(session.whoami, 'blue', attrs=[ 'underline' ])
    return account_id


def get_alias(session: boto3.session.Session) -> Optional[str]:
    """
    gets the iam account alias of the account we are signed into and
    caches the result as an attribute on the `session` object
    :param session: a boto3.session.Session object
    :return str: the human understandable iam account alias
    """
    alias = getattr(session, 'alias', None)
    if not alias:
        notice('alias')
        iam = session.client('iam')
        aliases = iam.list_account_aliases()
        aliases = aliases['AccountAliases']
        alias = session.alias = aliases[0] if aliases else 'unknown'
        notice_end(f'{session.alias}', 'yellow', attrs=[ 'bold' ])
    return alias


def make_session(profile, session=None, region=None):
    """
    creates an aws session using the provided profile and region
    :param str profile: the name of the aws profile
    :param boto3.session.Session session: an existing session if one exists
    :param str region: the aws region -- e.g., us-east-2
    :rtype: boto3.session.Session
    """
    if session:
        return session
    notice(f'checking profile {profile}')
    session = boto3.Session()
    if profile not in session.available_profiles:
        notice_end('not found')
        return None
    notice_end()
    session = boto3.Session(profile_name=profile, region_name=region)
    get_account_id(session)
    get_alias(session)
    return session


class AwsTask(Task):
    def __call__(self, *args, **kwargs):
        profile = kwargs.get('profile')
        ctx = args[0]
        session = kwargs.get('session')
        has_context = isinstance(ctx, Context)
        if has_context:
            session = session or getattr(ctx, 'context', None)
        prefix = kwargs.get('prefix')
        force_sso = kwargs.pop('force_sso', False)
        if profile is None and has_context:
            try:
                profile = ctx.aws.profile
            except AttributeError:
                pass
        if prefix is None and isinstance(ctx, Context):
            try:
                prefix = ctx.convocations.prefix
            except AttributeError:
                pass
        is_sso = False
        sso_config = None
        try:
            is_sso = ctx.aws.start_url
        except AttributeError:
            pass
        if not is_sso:
            from botocore.session import Session as CoreSession
            if profile:
                core_session = CoreSession(profile=profile)
                profiles = core_session.full_config.get('profiles', {})
                sso_config = profiles.get(profile, {})
                is_sso = sso_config.get('sso_start_url')
                is_sso = is_sso and sso_config.get('sso_account_id')
                is_sso = is_sso and sso_config.get('sso_region')
        if is_sso:
            role = kwargs.get('role')
            session = make_sso_session(
                ctx, role, session, profile, force_sso,
                sso_config)
        else:
            session = make_session(profile, session)
        if has_context:
            setattr(ctx, 'session', session)
        kwargs['session'] = session
        kwargs['prefix'] = prefix
        return super().__call__(*args, **kwargs)


def get_tag(p, key):
    try:
        tags = p.get('Tags', [])
    except AttributeError:
        tags = p.tags or []
    key = key.lower()
    for x in tags:
        if x['Key'].lower() == key:
            return x['Value']
    return ''


def name_tag(p: Any, lower=True) -> str:
    """
    searches a dict or an object for tags with the value name and returns the
    first such tag value
    """
    name = get_tag(p, 'Name')
    if lower:
        name = name.lower()
    return name


def yielder(client, method: str, session=None, **kwargs) -> List[Dict]:
    if not session:
        return
    if isinstance(client, str):
        client = session.client(client)
    p = client.get_paginator(method)
    for page in p.paginate(**kwargs):
        for key, value in page.items():
            if key != 'NextMarker' and isinstance(value, list):
                yield from value


def get_path(data, path, default=None):
    """
    allows access to a dict by the dotted path
    """
    keys = path.split('.')
    value = data
    for x in keys:
        if isinstance(value, Mapping) and x in value:
            value = value[x]
        else:
            return default
    return value


def post_to_slack(ctx, session, room, message):
    session = session or boto3.DEFAULT_SESSION
    token = getattr(ctx, f'{room}_token', None)
    if not token:
        notice(f'getting {room} token')
        ssm = session.client('ssm')
        try:
            response = ssm.get_parameter(Name=f'/dev/slack/{room}')
            token = response['Parameter']['Value']
            notice_end()
        except ClientError as ex:
            notice_end(ex.response['Error']['Code'])
            return False
    message = f'*{getuser()}* {message}'
    url = f'https://hooks.slack.com/services/{token}'
    return requests.post(url, json={ 'text': message }, timeout=5)
