import posixpath

from raft import task, Collection
from ...base.utils import notice, notice_end
from ..base import AwsTask


codeartifact_collection = Collection()


@task(klass=AwsTask)
def login_to_repo(
        ctx, name=None, domain=None, owner=None,
        repo_format='pypi', profile=None,
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
    url = f'{endpoint[:8]}aws:{token}@{endpoint[8:]}'
    url = posixpath.join(url, 'simple')
    ctx.run('pip config set global.timeout 10')
    ctx.run(f'pip config set global.extra-index-url {url}')


codeartifact_collection.add_task(login_to_repo)
