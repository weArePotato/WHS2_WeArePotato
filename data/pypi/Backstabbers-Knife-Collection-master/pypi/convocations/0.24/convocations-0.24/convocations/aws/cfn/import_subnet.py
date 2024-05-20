from raft import task
from ...base.utils import print_table, notice, notice_end, dump_yaml
from ..base import AwsTask


@task(klass=AwsTask)
def subnet_to_yaml(
        ctx, logical_name=None, subnet_id=None,
        session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for a security group
    """
    ec2 = session.resource('ec2')
    subnet = ec2.Subnet(subnet_id)
    properties = dict(
        AssignIpv6AddressOnCreation=subnet.assign_ipv6_address_on_creation,
        AvailabilityZone=subnet.availability_zone,
        CidrBlock=subnet.cidr_block,
        EnableDns64=subnet.enable_dns64,
        Ipv6CidrBlock=subnet.ipv6_cidr_block_association_set[0] if subnet.ipv6_cidr_block_association_set else None,
        Ipv6Native=subnet.ipv6_native,
        MapPublicIpOnLaunch=subnet.map_public_ip_on_launch,
        OutpostArn=subnet.outpost_arn,
        PrivateDnsNameOptionsOnLaunch=subnet.private_dns_name_options_on_launch,
        Tags=subnet.tags,
        VpcId=subnet.vpc_id,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    if 'Ipv6CidrBlock' not in properties:
        del properties['AssignIpv6AddressOnCreation']
    data = {
        logical_name: dict(
            Type='AWS::EC2::Subnet',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        dump_yaml(data, quiet=False)
    return data


@task(klass=AwsTask)
def import_subnet(ctx, logical_name, subnet_id, filename,
                  skip_review=False, session=None, prefix=None,
                  **kwargs):
    """
    creates a yaml template for a security group and imports it into cloudformation

    if skip_review is set, we will immediately try to execute the change set
      in cloudformation
    """
    from .import_resource_to_cfn import import_resource_to_cfn
    data = subnet_to_yaml(
        ctx, logical_name, subnet_id, session=session, quiet=True)
    resources_to_import = [dict(
        ResourceType='AWS::EC2::Subnet',
        LogicalResourceId=list(data.keys())[0],
        ResourceIdentifier=dict(SubnetId=subnet_id),
    )]
    import_resource_to_cfn(
        data, resources_to_import,
        filename, None, skip_review, session, prefix)


@task(klass=AwsTask)
def subnets(ctx, name=None, routes=False, session=None, **kwargs):
    from ..ec2 import get_tag
    from ..base import yielder
    notice('loading subnets')
    ec2 = session.client('ec2')
    rg_subnets = list(yielder(ec2, 'describe_subnets', session=session))
    notice_end()
    header = [ 'id', 'name', 'cidr', 'cidr6', ]
    if routes:
        notice('loading route tables')
        rg_tables = list(yielder(ec2, 'describe_route_tables', session=session))
        notice_end()
        mp_subnets = { x['SubnetId']: x for x in rg_subnets }
        for x in rg_tables:
            table_id = x['RouteTableId']
            name = get_tag(x, 'Name')
            for association in x['Associations']:
                subnet_id = association.get('SubnetId')
                if not subnet_id:
                    continue
                subnet = mp_subnets[subnet_id]
                subnet['route_table_id'] = table_id
                subnet['route_table'] = name
        header += [ 'route_table_id', 'route_table' ]
    rows = []
    name = (name or '').lower()
    for x in rg_subnets:
        subnet_name = get_tag(x, 'Name') or ''
        subnet_name = subnet_name.lower()
        if name not in subnet_name:
            continue
        row = [
            x['SubnetId'], get_tag(x, 'name') or '', x.get('CidrBlock'),
        ]
        ipv6 = x.get('Ipv6CidrBlockAssociationSet') or [{}]
        row.append(ipv6[0].get('Ipv6CidrBlock', ''))
        if routes:
            row.append(x.get('route_table_id', ''))
            row.append(x.get('route_table', ''))
        rows.append(row)
    rows.sort(key=lambda lx: lx[1])
    print_table(header, rows)
