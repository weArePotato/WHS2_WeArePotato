from raft.tasks import task
from ..base import AwsTask
from ...base.utils import print_table, notice, notice_end


@task(klass=AwsTask)
def run_posh(ctx, name, filename, session=None, **kwargs):
    """
    runs a command on the specified windows instance using ssm run command
    :param ctx: the raft / convoke context
    :param str name: the name or instance id of the ec2 instance
    :param str filename: the /path/to the .ps1 script that you want to run
    :param session: leave this blank
    """
    from ..ec2 import yield_instances
    from ..base import get_tag
    notice(f'loading {filename}')
    with open(filename, 'rt') as f:
        commands = f.readlines()
    instances = list(yield_instances(name, session))
    instance_ids = [ x['InstanceId'] for x in instances ]
    header = [ 'instance_id', 'name' ]
    rows = []
    for x in instances:
        rows.append([ x['InstanceId'], get_tag(x, 'name') ])
    print()
    print_table(header, rows)
    print()
    notice(f'running command on {len(rows)} instances')
    ssm = session.client('ssm')
    result = ssm.send_command(
        InstanceIds=instance_ids,
        DocumentName='AWS-RunPowerShellScript',
        Parameters=dict(commands=commands)
    )
    result = result['Command']
    command_id = result['CommandId']
    notice_end(command_id)
    waiter = ssm.get_waiter('command_executed')
    for instance_id in instance_ids:
        notice(f'waiting for {instance_id}')
        waiter.wait(
            CommandId=command_id,
            InstanceId=instance_id,
            WaiterConfig=dict(Delay=15))
        notice_end()
        x = ssm.get_command_invocation(CommandId=command_id, InstanceId=instance_id)
        print(x['StandardOutputContent'])
        print(x['StandardErrorContent'])
