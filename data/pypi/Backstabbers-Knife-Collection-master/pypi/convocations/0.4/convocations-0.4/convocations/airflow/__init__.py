from configparser import ConfigParser
from raft import task
from ..base.utils import notice_end, notice


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


@task
def setup_local_connections(ctx, key=None):
    """
    installs connections on your local airflow
    """
    import requests
    conf = ctx.airflow
    session = requests.Session()
    session.auth = (conf.username, conf.password)
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
        body = dict(
            conn_type=x.get('conn_type') or '',
            host=x.get('host') or '',
            login=x.get('login') or '',
            password=x.get('password') or '',
            schema=x.get('schema') or '',
            port=x.get('port') or None,
            extra=x.get('extra') or ''
        )
        response = fn(url, json=body)
        notice_end(response.text)


@task
def setup_local_variables(ctx):
    """
    installs variables on your local airflow running in docker compose
    """
    import requests
    conf = ctx.airflow
    variables = conf.variables
    if not variables:
        print('nothing to be done')
        return
    session = requests.Session()
    session.auth = (conf.username, conf.password)
    base_url = f'{conf.base_url}/api/v1/variables'
    response = session.get(base_url)
    data = response.json()
    existing_variables = { x['key'] for x in data['variables'] }
    for key, value in variables.items():
        found = key in existing_variables
        if found:
            fn = session.patch
            url = f'{base_url}/{key}'
            notice(f'patching {key}')
        else:
            fn = session.post
            url = base_url
            notice(f'creating {key}')
        body = dict(key=key, value=value)
        fn(url, json=body)
        notice_end()


@task
def clear_queue(ctx, filename):
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
