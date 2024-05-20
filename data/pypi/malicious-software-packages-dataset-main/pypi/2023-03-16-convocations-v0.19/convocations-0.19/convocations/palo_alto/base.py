import warnings

from raft.context import Context
from ..aws.base import AwsTask
from ..base.utils import get_context_value

try:
    from urllib3.exceptions import InsecureRequestWarning
    import requests
    import yaml
    from murmuration import kms_wrapped
    from lxml import etree
except ImportError:
    pass


class XmlApiTask(AwsTask):
    def __call__(self, *args, **kwargs):
        ctx = args[0]
        host = kwargs.pop('host', None)
        bucket = kwargs.pop('bucket', None)
        if isinstance(ctx, Context):
            kwargs['host'] = host or get_context_value(ctx, 'palo_alto.host')
            kwargs['bucket'] = bucket or get_context_value(ctx, 'palo_alto.bucket')
            kwargs['username'] = get_context_value(ctx, 'palo_alto.username')
            kwargs['password'] = get_context_value(ctx, 'palo_alto.password')
            kwargs['peer'] = get_context_value(ctx, 'palo_alto.peer')
        super().__call__(*args, **kwargs)


class XmlApi:
    def __init__(self, host, username=None, password=None, profile=None, **kwargs):
        self.session = requests.Session()
        self.session.verify = False
        self.host = host
        self.base_url = f'https://{self.host}/api/'
        self.generate(host, username, password, profile, **kwargs)

    @classmethod
    def resolve_creds(cls, username, password, session=None):
        from ..aws.base import get_parameter
        if username.startswith('/'):
            username = get_parameter(session, username)
        if password.startswith('/'):
            password = get_parameter(session, password, True)
        return username, password

    def generate(self, host, username=None, password=None, profile=None, **kwargs):
        """
        generates an api key using the rest api with the palo alto
        """
        session = kwargs.get('session')
        filename = kwargs.get('filename')
        if filename:
            with open(filename, 'r') as f:
                conf = yaml.load(f, Loader=yaml.SafeLoader)
            api_conf = conf.get('api') or {}
            username = username or api_conf.get('username')
            password = password or api_conf.get('password')
            profile = profile or conf.get('profile')
        username, password = self.resolve_creds(username, password, session)
        if not password:
            try:
                password = kms_wrapped.decrypt(password, profile=profile)
            except:
                pass

        doc = self.post('keygen', None, user=username, password=password)
        api_key = doc.text
        self.session.headers = {
            'X-PAN-KEY': api_key,
        }

    def raw(self, method, params=None, data=None, files=None):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', category=InsecureRequestWarning)
            response = self.session.request(
                method, self.base_url,
                params=params, data=data, files=files)
            return response

    def get(self, type_, action=None, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = type_
        if action:
            params['action'] = action
        response = self.raw('get', params)
        return self.handle_response(response)

    @classmethod
    def handle_response(cls, response):
        doc = etree.fromstring(response.content)
        if doc.tag == 'response':
            stuff = doc.xpath('/response/result')
            if stuff:
                stuff = stuff[0]
            for x in stuff:
                return x
        return doc

    def post(self, type_, action, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = type_
        if action:
            params['action'] = action
        response = self.raw('post', data=params)
        return self.handle_response(response)

    def import_cert(self, name, category,
                    certificate_format='pem',
                    filename=None, content=None, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = 'import'
        params['category'] = category
        params['certificate-name'] = name
        params['format'] = certificate_format
        files = {
            'certFile': content,
        }
        if filename and not content:
            with open(filename, 'r') as f:
                files['certFile'] = f.read()
        response = self.raw('post', data=params, files=files or None)
        return self.handle_response(response)

    def import_pfx(self, name, content, passphrase, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = 'import'
        params['category'] = 'keypair'
        params['certificate-name'] = name
        params['format'] = 'pkcs12'
        params['passphrase'] = passphrase
        files = {
            'file': (name, content, 'application/x-pkcs12'),
        }
        response = self.raw('post', data=params, files=files or None)
        return self.handle_response(response)

    def import_pem(self, name, cert_content, key_content=None, passphrase=None,
                   **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = 'import'
        params['category'] = 'keypair' if key_content else 'certificate'
        params['certificate-name'] = name
        params['format'] = 'pem'
        if passphrase:
            params['passphrase'] = passphrase
        mime_type = 'application/x-pem-file'
        files = {
            'certFile': (f'{name}.crt', cert_content, mime_type),
        }
        if key_content:
            files['keyFile'] = (f'{name}.key', key_content, mime_type)
        response = self.raw('post', data=params, files=files or None)
        return self.handle_response(response)

    def commit(self, description):
        params = {
            'description': description,
            'cmd': '<commit></commit>'
        }
        params['type'] = 'commit'
        response = self.raw('post', data=params)
        return self.handle_response(response)
