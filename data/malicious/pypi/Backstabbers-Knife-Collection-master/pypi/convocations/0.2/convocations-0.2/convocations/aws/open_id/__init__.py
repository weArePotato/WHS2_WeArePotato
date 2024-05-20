from raft import task
from ..base import AwsTask


@task(klass=AwsTask, help=dict(
    role='the name of the role to login to',
    force_sso='specify to bypass cache usage',
    profile='the already-configured aws profile to use for sso login',
))
def sso_login(ctx, role=None, force_sso=False, session=None, profile=None, **kwargs):
    """
    logs in via sso to the role name specified.  If no role name is specified,
    login will log into the first role alphabetically.  follows the boto3
    convention and caches short-term credentials in the ~/.aws/sso/cache
    directory.  Use the force_sso flag to bypass the use of cached credentials.
    """
