from raft.tasks import task
from convocations.base.utils import print_table
from .base import CheckpointTask


@task(klass=CheckpointTask)
def layers(ctx, client=None, host=None, **kwargs):
    """
    lists all policy layers on the checkpoint by name
    """
    from cpapi import APIResponse
    result: APIResponse = client.api_call('show-access-layers')
    rg = result.data['access-layers']
    names = [ [ x['name'] ] for x in rg ]
    header = [ 'name' ]
    print_table(header, names)
    return rg
