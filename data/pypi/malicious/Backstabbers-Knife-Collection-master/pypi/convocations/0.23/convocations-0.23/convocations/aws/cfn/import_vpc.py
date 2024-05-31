from raft import task
from ...base.utils import print_table, notice, notice_end, dump_yaml
from ..base import AwsTask, yielder


@task(klass=AwsTask)
def vpc_to_yaml(
        ctx, logical_name=None, vpc_id=None,
        session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for a vpc
    """
    ec2 = session.resource('ec2')
    vpc = ec2.Vpc(vpc_id)
    properties = dict(
        CidrBlock=vpc.cidr_block,
        InstanceTenancy=vpc.instance_tenancy,
        Tags=vpc.tags,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::EC2::VPC',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def import_vpc(
        ctx, logical_name, vpc_id, filename,
        skip_review=False, session=None, prefix=None,
        **kwargs):
    """
    creates a yaml template for a vpc and imports it into cloudformation

    if skip_review is set, we will immediately try to execute the change set
      in cloudformation
    """
    from .import_resource_to_cfn import import_resource_to_cfn
    data = vpc_to_yaml(
        ctx, logical_name, vpc_id, session=session, quiet=True)
    resources_to_import = [dict(
        ResourceType='AWS::EC2::VPC',
        LogicalResourceId=list(data.keys())[0],
        ResourceIdentifier=dict(VpcId=vpc_id),
    )]
    import_resource_to_cfn(
        data, resources_to_import,
        filename, None, skip_review, session, prefix)


@task(klass=AwsTask)
def vpcs(ctx, session=None, raw=False, **kwargs):
    from ..ec2 import get_tag
    notice('loading vpcs')
    ec2 = session.client('ec2')
    rg_vpcs = list(yielder(ec2, 'describe_vpcs'))
    notice_end()
    if raw:
        dump_yaml(rg_vpcs, quiet=False)
    else:
        header = [ 'id', 'name', 'cidr', 'cidr6', ]
        rows = []
        for x in rg_vpcs:
            ipv4 = x.get('CidrBlockAssociationSet') or []
            ipv4 = [ cidr['CidrBlock'] for cidr in ipv4 ]
            ipv4 = ipv4 or [ x.get('CidrBlock') ]
            row = [
                x['VpcId'], get_tag(x, 'name') or '', ipv4[0],
            ]
            ipv6 = x.get('Ipv6CidrBlockAssociationSet')
            row.append((ipv6 or [{}])[0].get('Ipv6CidrBlock', ''))
            rows.append(row)
            for cidr in ipv4[1:]:
                rows.append([ '', '', cidr, '' ])
        print_table(header, rows)
