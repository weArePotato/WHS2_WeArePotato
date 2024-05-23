
from raft import Context
from raft.tasks import Task


class Api:
    def __init__(self, client_id, client_secret):
        from onelogin.api_client import ApiClient as OneLoginClient
        self.client = OneLoginClient(client_id, client_secret)


class OneLoginTask(Task):
    def __call__(self, *args, **kwargs):
        ctx = args[0]
        api = kwargs.get('api')
        if api is None and isinstance(ctx, Context):
            try:
                client_id = ctx.client_id
                client_secret = ctx.client_secret
                api = Api(client_id, client_secret)
            except AttributeError:
                pass
        kwargs['api'] = api
        return super().__call__(*args, **kwargs)
