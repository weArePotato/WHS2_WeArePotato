import posixpath
from datetime import datetime
from datetime import timedelta

from raft import task

from ...base.utils import notice, notice_end, print_table
from ..base import AwsTask


@task(klass=AwsTask, help={
    'name': 'the application name in code deploy',
    'group_name': 'the deployment group name; if left unspecified, we use the app_name',
    'lookback_window': 'the number of days in which we will look for deploys',
})
def recent_deployments(ctx, name, group_name=None,
                       lookback_window=30,
                       session=None, profile=None, **kwargs):
    """
    shows the most recent deploys and their statuses
    """
    client = session.client('codedeploy')
    notice('getting deployment group')
    result = client.batch_get_deployment_groups(
        applicationName=name,
        deploymentGroupNames=[group_name or name],
    )
    group_id = None
    if result:
        group_id = result['deploymentGroupsInfo'][0]['deploymentGroupId']
    notice_end(group_id)
    notice('getting deployments')
    end_date = datetime.today() + timedelta(days=1)
    start_date = end_date - timedelta(days=lookback_window + 1)
    result = client.list_deployments(
        applicationName=name,
        deploymentGroupName=group_name or name,
        createTimeRange=dict(
            start=start_date,
        )
    )
    notice_end(len(result['deployments']))
    values = [ ]
    deployment_ids = result['deployments'][-25:]
    result = client.batch_get_deployments(deploymentIds=deployment_ids)
    deployments = result['deploymentsInfo']
    for x in deployments:
        row = [
            x['deploymentId'] or '',
            x['status'].lower(),
            x['createTime'].isoformat(' ', 'seconds') if 'createTime' in x else '',
            x['startTime'].isoformat(' ', 'seconds') if 'startTime' in x else '',
            x['completeTime'].isoformat(' ', 'seconds') if 'completeTime' in x else '',
        ]
        values.append(row)
    header = [ 'id', 'status', 'created', 'started', 'ended']
    print_table(header, values)


@task(klass=AwsTask, help={
    'name': 'the application name in code deploy',
    'group_name': 'the deployment group name; if left unspecified, we use the app_name',
    's3_location': 'the s3 url for the deployment bundle',
})
def code_deploy(ctx, name, s3_location, group_name=None,
           session=None, profile=None, **kwargs):
    """
    kicks off the deploy name for the specified app and deployment group
    """
    group_name = group_name or name
    if s3_location.startswith('s3://'):
        s3_location = s3_location[5:]
    npos = s3_location.index('/')
    bucket = s3_location[:npos]
    key = s3_location[npos + 1:]
    _, ext = posixpath.splitext(key)
    ext = ext[1:].lower()
    types = dict(
        json='JSON',
        yml='YAML',
        yaml='YAML',
        zip='zip',
        tar='tar',
        tgz='tgz',
    )
    client = session.client('codedeploy')
    notice('starting deploy')
    client.create_deployment(
        applicationName=name,
        deploymentGroupName=group_name or name,
        revision=dict(
            revisionType='S3',
            s3Location=dict(
                bucket=bucket,
                key=key,
                bundleType=types[ext],
            )
        )
    )
    notice_end()

