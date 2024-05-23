import time

from raft.tasks import task


@task
def wait_for_mysql(ctx, service_name='db'):
    from mysql.connector import connect
    from mysql.connector.errors import OperationalError
    import yaml
    with open('docker-compose.yml', 'r') as f:
        compose = yaml.load(f, Loader=yaml.SafeLoader)
        db_port = compose['services'][service_name]['ports'][0].split(':')[1]
    n_max = 40
    for x in range(1, n_max + 1):
        try:
            print(f'checking for mysql on port {db_port} attempt #{x}')
            conn = connect(host='127.0.0.1', user='root', password='', port=db_port)
            cursor = conn.cursor()
            cursor.execute('select now()')
            data = cursor.fetchall()
            print(f'{data}')
            cursor.close()
            break
        except OperationalError:
            time.sleep(2)
        except Exception as ex:  # pylint: disable=broad-except
            print(f'{ex.__module__}.{ex.__class__.__name__}')
            time.sleep(0.5)


@task
def wait_for_redis(ctx, service_name='redis'):
    from redis import Redis
    from redis.exceptions import RedisError
    import yaml
    with open('docker-compose.yml', 'r') as f:
        compose = yaml.load(f, Loader=yaml.SafeLoader)
        redis_port = compose['services'][service_name]['ports'][0].split(':')[1]
    n_max = 40
    for x in range(1, n_max + 1):
        try:
            print(f'checking for redis on port {redis_port} attempt #{x}')
            r = Redis(host='127.0.0.1', port=redis_port)
            r.get('hello')
            break
        except RedisError:
            print('error connecting to redis')
            time.sleep(0.5)
