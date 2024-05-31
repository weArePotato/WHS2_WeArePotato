from collections.abc import Mapping
from configparser import ConfigParser
from raft import task

from ..aws.base import AwsTask
from ..base.utils import notice_end, notice, get_context_value


@task
def generate_fernet_key(ctx, filename=None):
    """
    generates a fernet key for the airflow.cfg file
    if no fernet key exists within the current configuration.  If a fernet
    key exists within the current configuration, we simply ignore.
    """
    filename = filename or ctx.airflow.config
    p = ConfigParser()
    p.read(filename)
    fernet_key = p['core'].get('fernet_key')
    if not fernet_key:
        from cryptography.fernet import Fernet
        fernet_key = Fernet.generate_key().decode()
        p['core']['fernet_key'] = fernet_key
        with open(filename, 'w') as f:
            p.write(f)


def traverse_and_decrypt(d, session):  # pylint: disable=inconsistent-return-statements
    from waddle import ParamBunch
    if not isinstance(d, Mapping):
        return ParamBunch.try_decrypt(d, session=session)
    for key, value in d.items():
        if isinstance(value, Mapping):
            new_value = dict(traverse_and_decrypt(value, session))
            yield key, new_value
        elif isinstance(value, list):
            new_value = []
            for x in value:
                x = ParamBunch.try_decrypt(x, session=session)
                new_value.append(x)
            yield key, new_value
        else:
            yield key, ParamBunch.try_decrypt(value, session=session)
    return


@task(klass=AwsTask)
def setup_local_connections(ctx, key=None, session=None, **kwargs):
    """
    installs connections on your local airflow
    """
    import requests
    from waddle import ParamBunch
    conf = ctx.airflow
    aws_session = session
    session = requests.Session()
    password = ParamBunch.try_decrypt(conf.password, session=aws_session)
    session.auth = (conf.username, password)
    base_url = f'{conf.base_url}/api/v1/connections'
    response = session.get(base_url)
    data = response.json()
    connections = conf.connections
    existing_connections = data['connections']
    connection_ids = { x['connection_id'] for x in existing_connections }
    for connection_id in connections.keys():
        if key and key != connection_id:
            continue
        found = connection_id in connection_ids
        if found:
            fn = session.patch
            url = f'{base_url}/{connection_id}'
            notice(f'patching {connection_id}')
        else:
            fn = session.post
            url = base_url
            notice(f'creating {connection_id}')
        x = connections[connection_id]
        x = dict(traverse_and_decrypt(x, aws_session))
        body = dict(
            conn_type=x.get('conn_type') or '',
            host=x.get('host') or '',
            login=x.get('login') or '',
            password=password,
            schema=x.get('schema') or '',
            port=x.get('port') or None,
            extra=x.get('extra') or ''
        )
        response = fn(url, json=body)
        notice_end(response.text)


@task(klass=AwsTask)
def setup_local_variables(ctx, session=None, **kwargs):
    """
    installs variables on your local airflow running in docker compose
    """
    from murmuration import kms_wrapped
    import requests
    variables = get_context_value(ctx, 'airflow.variables')
    if not variables:
        print('nothing to be done')
        return
    conf = ctx.airflow
    try:
        password = kms_wrapped.decrypt(conf.password, session=session)
    except:
        password = conf.password
    api_session = requests.Session()
    api_session.auth = (conf.username, password)
    base_url = f'{conf.base_url}/api/v1/variables'
    response = api_session.get(base_url)
    data = response.json()
    existing_variables = { x['key'] for x in data['variables'] }
    for key, value in variables.items():
        found = key in existing_variables
        if found:
            fn = api_session.patch
            url = f'{base_url}/{key}'
            notice(f'patching {key}')
        else:
            fn = api_session.post
            url = base_url
            notice(f'creating {key}')
        body = dict(key=key, value=value)
        fn(url, json=body)
        notice_end()


@task
def clear_queue(ctx, filename=None):
    """
    clears the celery queue to prevent weird errors
    `TypeError: unsupported operand type(s) for +: 'float' and 'str'`
    """
    from redis import Redis
    filename = filename or ctx.airflow.config
    p = ConfigParser()
    p.read(filename)
    notice('looking up broker url')
    broker_url = p['celery'].get('broker_url')
    if not broker_url:
        cmd = p['celery'].get('broker_url_cmd')
        if cmd:
            result = ctx.run(cmd)
            broker_url = result.stdout.strip()
    if not broker_url:
        notice_end('not found')
        return
    notice_end()
    notice('clearing default queue')
    client = Redis(broker_url)
    client.delete('default')
    notice_end()
