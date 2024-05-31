from raft import task

from convocations.aws.base import AwsTask


@task(klass=AwsTask)
def start_task(ctx, task_name, command, cluster=None, tail=True, session=None, **kwargs):
    """
    kicks off a task in ecs

    ```yaml
    tundra:
      ecs:
        cluster: cluster1
        network_configuration:
          subnets:
            - subnet-0123456789
            - subnet-1234567890
          security_groups:
            - sg-0123456789
          assignPublicIp: DISABLED
    ```
    :param ctx:
    :param task_name: the name of the task
    :param command: the command to run inside the container
    :param cluster: the cluster name
    :param tail: if specified, we will tail the logs
    :param session:
    :param kwargs:

    :return:
    """
    from convocations.aws.ecs import get_latest_revision
    from convocations.aws.ecs import task_logs
    from convocations.base.utils import get_context_value, notice, notice_end
    x = get_latest_revision(ctx, task_name, session=session, quiet=True)
    ecs = session.client('ecs')
    command = command.split(' ')
    cluster = cluster or get_context_value(ctx, 'tundra.ecs.cluster')
    network = get_context_value(ctx, 'tundra.ecs.network_configuration')
    if network:
        network = dict(awsvpcConfiguration=network)
    notice(f'starting {x} on cluster {cluster}')
    result = ecs.run_task(
        cluster=cluster,
        taskDefinition=x,
        overrides={
            'containerOverrides': [{'name': task_name, 'command': command}]
        },
        launchType='FARGATE',
        networkConfiguration=network
    )
    result = result['tasks'][0]
    task_arn = result['taskArn']
    task_id = task_arn.rsplit('/', 1)[-1]
    notice_end(task_id)
    if tail:
        task_logs(ctx, cluster, task_name, task_id)
