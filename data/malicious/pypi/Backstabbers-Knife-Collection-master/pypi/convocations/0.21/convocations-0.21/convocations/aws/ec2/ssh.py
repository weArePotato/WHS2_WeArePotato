# pylint: disable=not-context-manager
import contextlib
import os
from tempfile import NamedTemporaryFile
from raft.tasks import task

from ...base.utils import notice, notice_end
from ..base import AwsTask
from . import instance_by_name
from . import get_tag


@contextlib.contextmanager
def download_deploy_key(session, parameter_name):
    """
    downloads a deploy key from ssm to a temporary file, yields the temporary
    filename context
    :param session: the aws session
    :type  session: boto3.session.Session
    :param parameter_name: the name of the ssm parameter
    :type  parameter_name: str
    :return:
    """
    ssm = session.client('ssm')
    if not parameter_name.startswith('/'):
        parameter_name = f'/{parameter_name}'
    parameter = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    with NamedTemporaryFile(mode='w', buffering=1) as f:
        f.write(parameter['Parameter']['Value'])
        f.flush()
        os.chmod(f.name, 0o600)
        yield f


@task(klass=AwsTask, help={
    'public': 'use this flag to ssh to the public ip address instead'
              ' of the private ip address',
    'username': 'specify an alternative username to use when logging'
                ' into the remote server--e.g., centos, ec2-user or ubuntu.',
    'name': 'the tag name to match in aws.  n.b., we will use the first'
            ' instance with that name that appears in the api response.  you'
            ' may want to use the `instances` convocation to narrow down'
            ' conflicts'
})
def ssh(ctx, name, username=None, public=False, port=22, ip_override=None,
        session=None, **kwargs):
    """
    allows us to ssh to the instance if the key_pair was created by the
    new_key_pair convocation

    First, a new keypair is generated using the
    `new_key_pair` convocation and saved as namespace/name_deploy_key.
    This will create a new ec2 ssh key pair and store
    the private key in ssm under the path /namespace/name_deploy_key.  The
    deploy key is encrypted using the cmk with the namespace alias.  Then,
    when the instance is created, the key pair will be specified for the
    ssh instance.
    """
    x = instance_by_name(ctx, name, session=session)
    notice('getting key name')
    key_name = get_tag(x, 'deploy_key') or x.key_name
    notice_end(key_name)
    notice('username')
    username = username or get_tag(x, 'ssh_user')
    notice_end(username)
    notice('getting ip address')
    if public:
        ip_address = ip_override or x.public_ip_address or x.private_ip_address
    else:
        ip_address = ip_override or x.private_ip_address
    notice_end(ip_address)
    parameter_name = key_name
    if not key_name.startswith('/'):
        parameter_name = f'/{key_name}'
    with download_deploy_key(session, parameter_name) as f:
        if username:
            ssh_cmd = f'ssh -i {f.name} -p {port} {username}@{ip_address}'
            notice_end(ssh_cmd)
            ctx.run(ssh_cmd, pty=True)
        else:
            ctx.run(f'ssh -i {f.name} -p {port} {ip_address}', pty=True)
