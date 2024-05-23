import time

from raft import task

from convocations.aws.base import AwsTask
from convocations.base.utils import notice, notice_end


@task(klass=AwsTask)
def task_logs(ctx, session, cluster_name, task_name, task_id):
    from ..cloudwatch import yield_logs
    logs = session.client('logs')
    ecs = session.client('ecs')
    start_time = None
    group_name = cluster_name
    stream_name = f'{cluster_name}/{task_name}/{task_id}'
    try:
        for n in range(0, 600):
            try:
                lines = list(
                    yield_logs(logs, group_name, stream_name, start_time)
                )
                lines.sort(key=lambda lx: lx['timestamp'])
                for x in lines:
                    print(x['message'])
                if lines:
                    start_time = lines[-1]['timestamp']
                if n % 5 == 4:
                    response = ecs.describe_tasks(
                        cluster=cluster_name, tasks=[task_id]
                    )
                    response = response['tasks'][0]
                    status = response['lastStatus']
                    print(f'task status: {status}')
                    if status == 'STOPPED':
                        break
                time.sleep(1)
            except logs.exceptions.ResourceNotFoundException:
                time.sleep(1)
    except KeyboardInterrupt:
        pass


@task(klass=AwsTask)
def get_latest_revision(ctx, task_name, session=None, quiet=False, **kwargs):
    """
    prints out the latest task revision for a task
    :param ctx:
    :param task_name: the name of the task
    :param session: the session passed in from `AwsTask`
    :param quiet: if this flag is set, output is repressed
    :param kwargs:
    :return:
    """
    talkative = not quiet
    if talkative:
        notice('getting task definition')
    ecs = session.client('ecs')
    result = ecs.describe_task_definition(taskDefinition=task_name)
    x = result['taskDefinition']
    result = f"{task_name}:{x['revision']}"
    if talkative:
        notice_end(result)
    return result

