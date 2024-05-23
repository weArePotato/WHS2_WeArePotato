####
#  To help us create environment-specific keypairs
#  that automatically get added to ssm's parameter store
#  for use in deploys
####
import boto3
from raft.tasks import task
from .base import AwsTask
from ..base.utils import notice_end, notice


__all__ = [
    'new_key_pair',
    'show_public_key',
]


@task(klass=AwsTask, help=dict(
    name='the name of the app',
    namespace='the ssm and keypair namespace',
    session='leave this blank, it will be filled in by the context',
))
def new_key_pair(
        ctx, name, namespace, key_type='ed25519',
        param_type='SecureString', key_arn=None,
        session=None, **kwargs):
    """
    creates a new key pair and stores it in aws ssm
    the ssm key for the private key will be /namespace/name
    while the name of the keypair will be  namespace/name

    This function to allows us to create environment-
      specific deploy keys that would allow us to, for example, do
      deploys from codebuild a little more easily

    Args:

        ctx: ignore, used internally by convoke
        name (str):
            the name of the key pair
        namespace (str):
            the namespace of the keypair, the namespace of the ssm
            parameter, and the alias to kms key
        key_type (str):
            specifies the type of key to create (rsa or ed25519),
            defaults to ed25519
        param_type (str):
            specifies the type of SSM parameter (String or SecureString)
        key_arn (str):
            if you want to override looking for a key with the
            alias `namespace`, then specify the key arn explicitly.
        session: ignore, used internally
    """
    session = session or boto3.Session(**kwargs)
    ec2 = session.client('ec2')
    if not name.endswith('deploy_key'):
        name = f'{name}_deploy_key'
    key_name = f'{namespace}/{name}'
    notice('creating key pair')
    response = ec2.create_key_pair(KeyName=key_name, KeyType=key_type)
    private_key = response['KeyMaterial']
    parameter_name = f'/{key_name}'
    notice_end(key_name)

    kms = session.client('kms')
    key_id = None
    if key_arn:
        notice(f'key {key_arn}?')
        try:
            response = kms.describe_key(KeyId=key_arn)
            notice_end()
            key_id = response['KeyMetadata']['KeyId']
        except:
            notice_end('not found')

    if not key_id:
        notice(f'key aliased {namespace}?')
        try:
            response = kms.describe_key(KeyId=f'alias/{namespace}')
            key_id = response['KeyMetadata']['KeyId']
            notice_end()
        except:
            notice_end('not found')

    notice('creating ssm parameter')
    ssm = session.client('ssm')
    params = dict(
        Name=parameter_name,
        Description=f'[{namespace}] deployment key for {name}',
        Value=private_key,
        Type=param_type,
    )
    if param_type == 'SecureString' and key_id:
        params['KeyId'] = key_id
    ssm.put_parameter(**params)
    notice_end()


@task(klass=AwsTask, help=dict(
    name='the name of the app',
    namespace='the ssm and keypair namespace',
    session='leave this blank, it will be filled in by the context',
))
def show_public_key(ctx, name, namespace, session=None, **kwargs):
    """
    shows the public key for the /namespace/name private key
    generated from `new_key_pair`

    Args:

        ctx: ignore, used internally by convoke
        name (str):
            the name of the key pair
        namespace (str):
            the namespace of the keypair, the namespace of the ssm
            parameter, and the alias to kms key
        session: ignore, used internally
    """
    from cryptography.hazmat.primitives import serialization as crypto_serialization

    session = session or boto3.Session(**kwargs)
    if not name.endswith('deploy_key'):
        name = f'{name}_deploy_key'
    key_name = f'{namespace}/{name}'
    parameter_name = f'/{key_name}'
    notice('getting key from ssm')
    ssm = session.client('ssm')
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    value = response['Parameter']['Value']
    notice_end()
    private_key = crypto_serialization.load_ssh_private_key(
        value.encode('utf-8'),
        password=None,
    )
    public_key = private_key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    print(public_key.decode('utf-8'))
