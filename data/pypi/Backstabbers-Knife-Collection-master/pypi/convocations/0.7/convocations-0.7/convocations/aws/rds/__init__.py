from raft import task
from ...base.utils import print_table
from ..base import AwsTask


@task(klass=AwsTask)
def rds_instances(ctx, session=None, profile=None, **kwargs):
    """
    shows all rds instances and their endpoints
    """
    rds = session.client('rds')
    instances = rds.describe_db_instances()
    instances = instances['DBInstances']
    header = [ 'name', 'engine', 'endpoint', 'status', ]
    rows = []
    for x in instances:
        rows.append([
            x['DBInstanceIdentifier'],
            f"{x['Engine']} {x['EngineVersion']}",
            f"{x['Endpoint']['Address']}:{x['Endpoint']['Port']}",
            x['DBInstanceStatus'],
        ])
    rows.sort(key=lambda lx: lx[0])
    print_table(header, rows)

