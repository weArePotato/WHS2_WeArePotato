import time
from raft import task
from ..base import AwsTask


__all__ = [
    'launch_test_instance',
]


@task(klass=AwsTask)
def launch_test_instance(ctx, source_server, profile=None, session=None, **kwargs):
    """
    launches a source server in test mode
    """
    from boto3.session import Session
    from ...base.utils import notice, notice_end, print_table
    session = session or Session(profile_name=profile)
    mgn = session.client('mgn')
    paginator = mgn.get_paginator('describe_source_servers')
    source_servers = {}
    source_server = source_server.lower()
    notice('loading source servers')
    for page in paginator.paginate():
        for x in page['items']:
            name = x['sourceProperties']['identificationHints']['hostname']
            st_id = x['sourceServerID']
            source_servers[name.lower()] = st_id
    if source_server not in source_servers:
        notice_end(f'{source_server} was not found')
        header = [ 'name', 'id' ]
        rows = [ [ key, value ] for key, value in source_servers.items() ]
        print_table(header, rows)
        return
    st_id = source_servers[source_server]
    notice_end(st_id)
    notice(f'starting test of {st_id}')
    response = mgn.start_test(sourceServerIDs=[ st_id ])
    job_id = response['job']['jobID']
    notice_end(job_id)
    token = None
    conversion_server_id = None
    for y in range(11):
        notice(f'wait {y + 1}')
        response = mgn.describe_job_log_items(jobID=job_id, nextToken=token)
        token = response['nextToken']
        for x in response['items']:
            conversion_server_id = x['eventData'].get('conversionServerID')
            if conversion_server_id:
                break
        if conversion_server_id:
            break
        notice_end()
        time.sleep(15)
    if conversion_server_id:
        notice('modifying termination')
        ec2 = session.client('ec2')
        ec2.modify_instance_attribute(
            Attribute='disableApiTermination',
            DisableApiTermination=dict(Value=True),
            InstanceId=conversion_server_id,
        )
        notice_end()
