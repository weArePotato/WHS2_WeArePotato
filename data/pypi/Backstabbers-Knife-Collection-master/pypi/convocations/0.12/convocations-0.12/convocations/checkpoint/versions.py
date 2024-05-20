from raft.tasks import task
from convocations.base.utils import notice, notice_end
from .base import CheckpointTask


@task(klass=CheckpointTask)
def api_version(ctx, client=None, host=None, **kwargs):
    """
    lists the current api version
    """
    from cpapi import APIResponse
    result: APIResponse = client.api_call('show-api-versions')
    notice('checkpoint api version')
    notice_end(result.data['current-version'])
