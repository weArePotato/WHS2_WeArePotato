# pylint: disable=redefined-builtin
from raft.tasks import task

from ...base.utils import print_table
from ..base import AwsTask
from . import get_tag


@task(klass=AwsTask, help=dict(
    id='[optional] a comma delimited list of ids',
))
def route_tables(ctx, id=None, session=None, **kwargs):
    """
    prints a list of all routes in the route tables specified in the `id` argument.
    route tables can be specified as a comma-delimited list.  if no ids
    are specified, we will display all routes in all route tables.
    """
    ec2 = session.client('ec2')
    if id:
        id = id.split(',')
        rg = ec2.describe_route_tables(RouteTableIds=id)
    else:
        rg = ec2.describe_route_tables()
    header = [ 'id', 'name', 'dest', 'next_hop', ]
    rows = []
    for x in rg['RouteTables']:
        for route in x['Routes']:
            rows.append([
                x['RouteTableId'],
                get_tag(x, 'Name') or '',
                route.get('DestinationCidrBlock') or route.get('DestinationIpv6CidrBlock') or '',
                route.get('GatewayId') or route.get('InstanceId') or
                route.get('NetworkInterfaceId') or route.get('TransitGatewayId') or
                route.get('VpcPeeringConnectionId') or ''
            ])
    print_table(header, rows)
