import json
import os
import time
from collections.abc import Mapping
from configparser import ConfigParser
from raft import task
from raft.config import DataProxy

from ..aws.base import AwsTask
from ..base.utils import notice_end, notice, get_context_value, \
    get_encrypted_context_value, dump_yaml


def airflow_config(ctx, filename):
    if filename:
        notice(f'checking {filename}')
        if not os.path.exists(filename):
            notice_end(False)
            filename = None
        else:
            notice_end()
    if not filename:
        notice('checking config for airflow.cfg')
        filename = get_context_value(ctx, 'airflow.config')
        if filename:
            if not os.path.exists(filename):
                filename = None
                notice_end('warning, convocations config file incorrect')
            else:
                notice_end()
        else:
            notice_end(False)
        if not filename:
            notice('checking AIRFLOW_HOME')
            t = os.environ.get('AIRFLOW_HOME')
            if t:
                t = os.path.join(t, 'airflow.cfg')
                if os.path.exists(t):
                    filename = t
            notice_end(bool(filename))
    return filename


@task
def generate_fernet_key(ctx, filename=None):
    """
    generates a fernet key for the airflow.cfg file
    if no fernet key exists within the current configuration.  If a fernet
    key exists within the current configuration, we simply ignore.
    """
    filename = airflow_config(ctx, filename)
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
    if not isinstance(d, (Mapping, DataProxy)):
        value = ParamBunch.try_decrypt(d, session=session)
        return value
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
            new_value = ParamBunch.try_decrypt(value, session=session)
            yield key, new_value
    return


@task(klass=AwsTask)
def setup_local_connections(ctx, key=None, session=None, debug=False, **kwargs):
    """
    installs connections on your local airflow
    """
    import requests
    password = get_encrypted_context_value(ctx, session, 'airflow.password')
    conf = ctx.airflow
    aws_session = session
    session = requests.Session()
    session.auth = (conf.username, password)
    if debug:
        notice(f'connecting to api as {conf.username} / {password}')
    else:
        notice(f'connecting to api as {conf.username}')
    base_url = f'{conf.base_url}/api/v1/connections'
    response = session.get(base_url)
    notice_end(response.status_code == 200)
    if response.status_code != 200:
        notice_end(response.text)
        return
    data = response.json()
    connections = conf.connections
    existing_connections = data['connections']
    existing_connection_ids = {
        x['connection_id'] for x in existing_connections
    }
    for connection_id in connections.keys():
        if key and key != connection_id:
            continue
        x = connections[connection_id]
        found = connection_id in existing_connection_ids
        rg = list(traverse_and_decrypt(x, aws_session))
        x = dict(rg)
        if found:
            fn = session.patch
            url = f'{base_url}/{connection_id}'
            notice(f'patching {connection_id}')
        else:
            fn = session.post
            url = base_url
            notice(f'creating {connection_id}')
        body = dict(
            connection_id=connection_id,
            conn_type=x.get('conn_type') or '',
            host=x.get('host') or '',
            login=x.get('login') or '',
            password=x.get('password') or '',
            schema=x.get('schema') or '',
            port=x.get('port') or None,
            description=x.get('description') or None,
        )
        extra = x.get('extra')
        if extra:
            extra = json.dumps(extra)
            body['extra'] = extra
        response = fn(url, json=body)
        notice_end(response.status_code == 200)
        if response.status_code != 200:
            dump_yaml(response.json(), quiet=False)


@task(klass=AwsTask)
def setup_local_variables(ctx, session=None, **kwargs):
    """
    installs variables on your local airflow running in docker compose
    """
    from murmuration import kms_wrapped
    import requests
    notice('getting variables from configuration')
    variables = get_context_value(ctx, 'airflow.variables')
    if not variables:
        notice_end(False)
        return
    notice_end()
    conf = ctx.airflow
    password = get_encrypted_context_value(ctx, session, 'airflow.password')
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
        response = fn(url, json=body)
        notice_end(response.status_code == 200)
        if response.status_code != 200:
            dump_yaml(response.json(), quiet=False)


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


@task
def drain_celery(ctx, config=None, broker=None, timeout=900, poll=5):
    """
    drains celery by canceling consumers and waits for all active tasks
    to complete.
    """
    config = airflow_config(ctx, config)
    if not broker:
        notice(f'reading {config}')
        p = ConfigParser()
        p.read(config)
        notice_end()
        broker = p['celery']['broker_url']
    from celery import Celery
    app = Celery(broker=broker)
    notice('finding active queues')
    inspector = app.control.inspect()
    result = inspector.active_queues()
    active_queues = set()
    for queues in result.values():
        for queue in queues:
            active_queues.add(queue['name'])
    active_queues = list(active_queues)
    notice_end(len(active_queues))
    for queue in active_queues:
        notice(f'canceling {queue}')
        app.control.cancel_consumer(queue)
        notice_end()
    for x in range(timeout // poll):
        notice(f'active tasks [{x + 1}/{timeout // poll}]')
        active = inspector.active()
        n = 0
        for tasks in active.values():
            n += len(tasks)
        notice_end(n)
        if n == 0:
            break
        time.sleep(poll)
