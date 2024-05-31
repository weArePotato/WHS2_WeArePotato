import os
from raft import task
from ..base.utils import notice_end
from ..aws.base import AwsTask


__all__ = [
    'staging',
    'prod',
    'dags',
]


@task(klass=AwsTask)
def staging(ctx, limit=None, branch=None, profile=None, session=None, **kwargs):
    """
    deploys to staging environment
    requires the following configuration:

    ```yaml
    aws:
      profile: profile_name
    tundra:
      deploy:
        deploy_keys:
          limit1: namespace/key1
          limit2: namespace/key2
        staging:
          limit: default_limit
          branch: staging
    ```
    """
    conf = ctx.tundra.deploy.staging
    limit = limit or conf.limit
    branch = branch or conf.branch
    _deploy(ctx, conf, limit, branch, session=session)


@task(klass=AwsTask)
def prod(ctx, limit=None, branch=None, profile=None, session=None, **kwargs):
    """
    deploys to the prod environment

    requires the following configuration:

    ```yaml
    aws:
      profile: profile_name
    tundra:
      deploy:
        prod:
          limit: default_limit
          branch: master
    ```
    """
    conf = ctx.tundra.deploy.prod
    limit = limit or conf.limit
    branch = branch or conf.branch
    _deploy(ctx, conf, limit, branch, session=session)


def _deploy(ctx, conf, limit, branch=None, playbook='deploy.yml', tags=None,
            session=None, **kwargs):
    with ctx.cd('deploy'):
        os.makedirs('.sockets', exist_ok=True)
        if os.path.exists('ansible.cfg'):
            os.environ['ANSIBLE_CONFIG'] = './ansible.cfg'
        ansible = f'ansible-playbook -i hosts {playbook}'
        if limit:
            ansible = f'{ansible} --limit {limit}'
        if branch:
            ansible = f'{ansible} -e branch={branch}'
        if tags:
            ansible = f'{ansible} --tags {tags}'
        if kwargs:
            extra = ' '.join([
                f'-e {key}="{value}"' for key, value in kwargs.items()
            ])
            ansible = f'{ansible} {extra}'
        ctx.run(ansible, pty=True)


@task(klass=AwsTask)
def flower(ctx, limit=None, profile=None, session=None, **kwargs):
    """
    deploys flower, requires the following configuration:

    ```yaml
    aws:
      profile: profile_name
    tundra:
      deploy:
        deploy_keys:
          limit1: namespace/key1
          limit2: namespace/key2
        flower:
          limit: default_limit
          playbook: flower.yml
    ```
    """
    conf = ctx.tundra.deploy.flower
    playbook = conf.get('playbook', 'flower.yml')
    limit = limit or conf.limit
    _deploy(ctx, conf, limit, None, playbook, session=session)


@task(klass=AwsTask)
def dags(ctx, dag, limit=None, profile=None, session=None, **kwargs):
    """
    pushes a specific dag from your local to the peaky / staging environment.
    this will overwrite any dags in these directories.

    requires the following context:

    ```yaml
    aws:
      profile: profile_name
    tundra:
      deploy:
        deploy_keys:
          limit1: namespace/key1
          limit2: namespace/key2
        dags:
          limit: default_limit
          playbook: dags.yml
    ```
    """
    conf = ctx.tundra.deploy.dags
    limit = limit or conf.get('limit', None)
    playbook = conf.get('playbook', 'dags.yml')
    if not limit:
        notice_end('no limit specified for dag deploys')
        return
    _deploy(ctx, conf, limit, None, playbook, session=session, dag=dag)
