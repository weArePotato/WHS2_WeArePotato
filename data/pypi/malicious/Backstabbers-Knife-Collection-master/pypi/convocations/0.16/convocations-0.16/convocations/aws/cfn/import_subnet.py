from raft import task
from ...base.utils import print_table, notice, notice_end
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
        from convocations.base.utils import dump_yaml
        dump_yaml(data)
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
def subnets(ctx, session=None, **kwargs):
    from ..ec2 import get_tag
    notice('loading subnets')
    ec2 = session.client('ec2')
    paginator = ec2.get_paginator('describe_subnets')
    rg_subnets = []
    for page in paginator.paginate():
        rg_subnets += page['Subnets']
    notice_end()
    header = [ 'id', 'name', 'cidr', 'cidr6', ]
    rows = []
    for x in rg_subnets:
        row = [
            x['SubnetId'], get_tag(x, 'name') or '', x.get('CidrBlock'),
        ]
        ipv6 = x.get('Ipv6CidrBlockAssociationSet') or [{}]
        row.append(ipv6[0].get('Ipv6CidrBlock', ''))
        rows.append(row)
    rows.sort(key=lambda lx: lx[1])
    print_table(header, rows)
