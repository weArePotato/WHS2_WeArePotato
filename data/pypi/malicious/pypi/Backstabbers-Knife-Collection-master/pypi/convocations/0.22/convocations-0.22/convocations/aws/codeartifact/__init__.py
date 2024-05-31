import os
import posixpath
import re
from configparser import ConfigParser
from os.path import expanduser

from raft import task, Collection
from ...base.utils import notice, notice_end
from ..base import AwsTask


codeartifact_collection = Collection()


@task(klass=AwsTask)
def login_to_repo(
        ctx, name=None, domain=None, owner=None,
        repo_format='pypi', profile=None,
        pip=False, twine=False,
        region=None, session=None, **kwargs):
    """
    logs into the specified codeartifact pypi repository and configures pip

    config sample:

    ```yaml
    codeartifact:
      default_repo: myrepo
      myrepo:
        domain: mydomain
        owner: 012345678901
        format: npm
        region: us-west-1
    ```
    """
    from boto3.session import Session
    from convocations.base.utils import get_context_value as ctx_value
    name = name or ctx_value(ctx, 'codeartifact.default_repo')
    prefix = f'codeartifact.{name}'
    domain = domain or ctx_value(ctx, f'{prefix}.domain')
    owner = owner or ctx_value(ctx, f'{prefix}.owner')
    repo_format = repo_format or ctx_value(ctx, f'{prefix}.format')
    repo_format = repo_format or 'pypi'
    region = region or ctx_value(ctx, f'{prefix}.region')
    login_session = session
    if region and session.region_name != region:
        login_session = Session(
            profile_name=session.profile_name,
            region_name=region)
    client = login_session.client('codeartifact')
    notice(f'getting {name} endpoint')
    params = dict(
        domain=domain,
        repository=name,
        format=repo_format,
    )
    if owner:
        params['domainOwner'] = f'{owner}'
    response = client.get_repository_endpoint(**params)
    endpoint = response['repositoryEndpoint']
    notice_end()
    notice('getting authorization token')
    del params['repository']
    del params['format']
    params['durationSeconds'] = 43200
    response = client.get_authorization_token(**params)
    token = response['authorizationToken']
    notice_end()
    if pip:
        notice('configuring pip')
        url = f'{endpoint[:8]}aws:{token}@{endpoint[8:]}'
        url = posixpath.join(url, 'simple')
        ctx.run('pip config set global.timeout 10', hide='both')
        ctx.run(f'pip config set global.extra-index-url {url}', hide='both')
        notice_end()
    if twine:
        config = ConfigParser()
        twine_config_path = expanduser('~/.pypirc')
        notice(f'reading {twine_config_path}')
        if os.path.exists(twine_config_path):
            config.read(twine_config_path)
            notice_end()
        else:
            notice_end(False)
        notice('configuring twine')
        if not config.has_section('distutils'):
            config.add_section('distutils')
        index_servers = config['distutils'].get('index-servers') or ''
        index_servers = index_servers.split('\n')
        index_servers = [ x.strip() for x in index_servers ]
        index_servers.append(name)
        index_servers = '\n'.join(index_servers)
        config['distutils']['index-servers'] = index_servers
        if not config.has_section(name):
            config.add_section(name)
        config[name]['username'] = 'aws'
        config[name]['password'] = token
        config[name]['repository'] = endpoint
        with open(twine_config_path, 'w') as f:
            config.write(f)
        notice_end()


codeartifact_collection.add_task(login_to_repo)
