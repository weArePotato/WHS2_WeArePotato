# pylint: disable=redefined-builtin
from raft.tasks import task

from ...base.utils import print_table
from ..base import AwsTask
from . import get_tag


@task(klass=AwsTask, help=dict(
    id='[optional] a comma delimited list of ids',
))
def route_tables(ctx, name=None, ids=None, session=None, **kwargs):
    """
    prints a table of all routes in the route tables matching the `ids` argument.
    route tables can be specified as a comma-delimited list.  if no ids
    are specified, we will display all routes in all route tables.

    as an alternative to an id, you may specify the name of the route table
    as identified by the `Name` tag.  we will include any route tables where
    the specified name is a substring of the tag value.
    """
    ec2 = session.client('ec2')
    if ids:
        ids = ids.split(',')
        rg = ec2.describe_route_tables(RouteTableIds=ids)
    else:
        rg = ec2.describe_route_tables()
    name = (name or '').lower()
    header = [ 'id', 'name', 'dest', 'next_hop', ]
    rows = []
    for x in rg['RouteTables']:
        route_table_name = (get_tag(x, 'Name') or '').lower()
        if name not in route_table_name:
            continue
        for route in x['Routes']:
            rows.append([
                x['RouteTableId'],
                route_table_name,
                route.get('DestinationCidrBlock') or route.get('DestinationIpv6CidrBlock') or '',
                route.get('GatewayId') or route.get('InstanceId') or
                route.get('NetworkInterfaceId') or route.get('TransitGatewayId') or
                route.get('VpcPeeringConnectionId') or ''
            ])
    print_table(header, rows)
