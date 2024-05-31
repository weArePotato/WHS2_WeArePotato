import os
from raft.context import Context
from raft.tasks import Task


def connect(host):
    from pwinput import pwinput
    from cpapi import APIClient, APIClientArgs
    args = APIClientArgs(server=host)
    client = APIClient(args)
    default = os.environ.get('USER', os.environ.get('USERNAME'))
    username = input(f'checkpoint username (default: {default}): ') or default
    password = pwinput('checkpoint password: ')
    client.login(username, password, read_only=True)
    return client


class CheckpointTask(Task):
    def __call__(self, *args, **kwargs):
        client = kwargs.get('client')
        if client:
            return super().__call__(*args, **kwargs)

        host = kwargs.get('host')
        ctx = args[0]
        if host is None and isinstance(ctx, Context):
            try:
                host = ctx.checkpoint.host
            except AttributeError:
                pass
        client = connect(host)
        kwargs['client'] = client
        result = super().__call__(*args, **kwargs)
        client.close_connection()
        return result

