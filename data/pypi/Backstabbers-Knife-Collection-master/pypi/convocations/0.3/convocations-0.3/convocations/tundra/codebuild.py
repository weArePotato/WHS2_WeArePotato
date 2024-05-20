from datetime import datetime
import os
from tempfile import NamedTemporaryFile

from raft import task
from convocations.aws.base import AwsTask


__all__ = [
    'aws_apt_sources',
    'migrate',
    'setup',
    'setup_galaxy',
    'bundle',
    'deploy',
    'Codebuild',
]


@task
def setup(ctx):
    """
    installs dependencies in the codebuild environment
    this installation is dead simple because we don't have
    to worry about python virtual environments
    """
    pip = 'pip install -q'
    ctx.run(f'{pip} -U wheel')
    ctx.run(f'{pip} -U pip setuptools nodeenv')
    ctx.run(f'{pip} -r requirements.txt')


@task
def setup_galaxy(ctx):
    """
    installs ansible-galaxy dependencies
    """
    ctx.run('ansible-galaxy install -r deploy/requirements.yml')


@task
def client(ctx):
    """
    builds the vue.js client
    """
    ctx.run('npm i -g parcel-bundler')
    with ctx.cd('client'):
        ctx.run('npm i')
        ctx.run('npm run build')


@task
def aws_apt_sources(ctx):
    """Fixes /etc/apt/sources.list by pointing to aws ubuntu mirrors"""
    with open('/etc/apt/sources.list', 'r') as f:
        data = f.read()
    region = os.environ.get('AWS_DEFAULT_REGION', 'us-east-2')
    data = data.replace(
        'http://archive.ubuntu.com', f'http://{region}.ec2.archive.ubuntu.com'
    )
    with open('/etc/apt/sources.list', 'w') as f:
        f.write(data)


@task
def migrate(ctx):
    """
    runs django migrations from codebuild
    -- not for use on local
    ```yaml
    codebuild:
      envs:
        master: prod
        staging: staging
    ```
    """
    from .utils import which_python
    envs = ctx.codebuild
    migrating_branches = list(envs.keys())
    x = Codebuild()
    if x.is_branch:
        branch = x.git_branch
    else:
        print('No migrations, we are not in a branch codebuild')
        return

    if branch not in migrating_branches:
        print(f'only migrating for branches {migrating_branches}')
        return

    python = which_python(ctx)
    tundra_env = envs[branch]
    os.environ['TUNDRA_ENV'] = tundra_env
    ctx.run(f'{python} manage.py migrate')


@task
def bundle(ctx):
    """
    creates a bundle and deploys to s3 as an artifact for use with deploys
    requires the following configuration:

    ```yaml
    codebuild:
      bundles:
        versioned:
          name: path/to/{version}.zip
          bucket: s3.bucket.name
        staging:
          name: path/to/bundle_name
          bucket: s3.bucket.name
        master:
          name: pat/to/bundle.zip
          bucket: s3.bucket.name
    ```
    """
    import pytz
    from ..base.utils import get_context_value
    from ..base.utils import notice, notice_end
    x = Codebuild()
    conf = get_context_value(ctx, 'codebuild.bundles') or {}
    if x.is_branch:
        conf = conf[x.git_branch]
        version = x.git_branch
    else:
        conf = conf.versioned
        version = x.git_version
    name = conf.name.format(version=version)
    bucket = conf.bucket
    notice('creating local bundle')
    t = NamedTemporaryFile(delete=False)  # pylint: disable=consider-using-with
    ctx.run(f"zip -q -r {t.name} . -x '/data/*'")
    notice_end()
    latest = 'latest.zip'
    latest = f's3://{bucket}/{name}/{latest}'
    dated = datetime.now(pytz.timezone('CST6CDT'))
    dated = dated.strftime('%Y%m%d.%H%M.zip')
    dated = f's3://{bucket}/archive/{name}/{dated}'
    notice(f'uploading {latest}')
    ctx.run(f'aws s3 cp {t.name} {latest}', hide='both')
    notice_end()
    notice(f'uploading {dated}')
    ctx.run(f'aws s3 cp {latest} {dated}', hide='both')
    notice_end()
    os.remove(f'{t.name}')


@task(klass=AwsTask)
def deploy(ctx, profile=None, session=None):
    """
    deploys from codebuild to the specified tundra environment

    aws:
      profile: profile_name
    tundra:
      deploy:
        deploy_keys:
          limit1: namespace/key1
          limit2: namespace/key2
        staging:
          limit: staging_limit
          branch: staging
        prod:
          limit: production_limit
          branch: master
    """
    from .deploy import _deploy
    x = Codebuild()
    branch = x.git_branch
    conf = ctx.tundra.deploy
    found = False
    which = None
    for x, value in conf.items():
        if value.branch == branch:
            found = True
            which = x
    if not branch or not found:
        print(f'Nothing to be done, we do not deploy {branch}')
        return
    conf = conf.get(which)
    limit = conf.limit
    _deploy(ctx, conf, limit, branch, session=session)


class Codebuild:
    ref = None
    git_branch = None
    git_version = None

    @property
    def is_tag(self):
        return self.ref.startswith('tag/')

    @property
    def is_branch(self):
        return bool(self.git_branch)

    def __init__(self):
        self.ref = os.environ.get('CODEBUILD_WEBHOOK_TRIGGER', '')
        self.git_branch = self.ref.rsplit('/', 1)[-1].strip()
        if self.is_tag and self.git_branch.startswith('v'):
            self.git_version = self.git_branch
            self.git_branch = None
        if self.git_branch == '':
            self.git_branch = os.environ.get('CODEBUILD_SOURCE_VERSION', '')
