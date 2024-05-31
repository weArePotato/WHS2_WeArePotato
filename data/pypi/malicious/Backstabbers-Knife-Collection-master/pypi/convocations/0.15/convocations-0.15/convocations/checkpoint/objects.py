from raft.tasks import task
from convocations.base.utils import print_table, notice, notice_end
from .base import CheckpointTask


@task(klass=CheckpointTask)
def group(ctx, name, client=None, host=None, **kwargs):
    """
    shows information about the network group `named`
    """
    from cpapi.api_response import APIResponse
    notice('getting group')
    response: APIResponse = client.api_call('show-group', payload={
        'name': name,
    })
    data = response.data
    notice_end(data.get('name') or data.get('message'))
    members = [ [ x['name'] ] for x in data['members'] ]
    print_table([ 'name' ], members)
    return data
