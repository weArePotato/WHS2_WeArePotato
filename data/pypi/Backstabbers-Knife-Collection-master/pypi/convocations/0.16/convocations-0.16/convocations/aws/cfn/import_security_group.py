import copy

from raft import task
from ...base.utils import print_table, notice, notice_end
from ..base import AwsTask


def rule_to_yaml(rule, prefix='Source'):
    data = dict(IpProtocol=rule['IpProtocol'])
    if rule['IpProtocol'] != '-1':
        data['FromPort'] = rule.get('FromPort', -1)
        data['ToPort'] = rule.get('ToPort', -1)
        if rule['IpProtocol'].startswith('icmp') and data['FromPort'] == 0:
            data['FromPort'] = -1
    ipv4_ranges = rule.get('IpRanges') or []
    for x in ipv4_ranges:
        d = copy.copy(data)
        cidr = x.get('CidrIp')
        if cidr:
            d['CidrIp'] = cidr
        description = x.get('Description')
        if description:
            d['Description'] = description
        yield d
    ipv6_ranges = rule.get('Ipv6Ranges') or []
    for x in ipv6_ranges:
        d = copy.copy(data)
        cidr = x.get('CidrIpv6')
        if cidr:
            d['CidrIpv6'] = cidr
        description = x.get('Description')
        if description:
            d['Description'] = description
            yield d
    pairs = rule.get('UserIdGroupPairs') or []
    for pair in pairs:
        d = copy.copy(data)
        description = pair.get('Description')
        if description:
            d['Description'] = description
        d[f'{prefix}SecurityGroupId'] = pair['GroupId']
        owner_id = pair.get('UserId')
        if owner_id and prefix == 'Source':
            d[f'{prefix}SecurityGroupOwnerId'] = owner_id
        yield d


@task(klass=AwsTask)
def security_group_to_yaml(ctx, logical_name=None, group_id=None,
                           session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for a security group
    """
    ec2 = session.resource('ec2')
    group = ec2.SecurityGroup(group_id)
    ingress, egress = [], []
    for x in group.ip_permissions:
        data = rule_to_yaml(x)
        ingress.extend(data)
    for x in group.ip_permissions_egress:
        data = rule_to_yaml(x, 'Destination')
        egress.extend(data)
    properties = dict(
        GroupDescription=group.description,
        GroupName=group.group_name,
        VpcId=group.vpc_id,
        Tags=group.tags,
        SecurityGroupIngress=ingress,
        SecurityGroupEgress=egress,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::EC2::SecurityGroup',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        from convocations.base.utils import dump_yaml
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def import_security_group(ctx, logical_name, group_id, filename,
                          skip_review=False, session=None, prefix=None,
                          **kwargs):
    """
    creates a yaml template for a security group and imports it into cloudformation

    if skip_review is set, we will immediately try to execute the change set
      in cloudformation
    """
    from .import_resource_to_cfn import import_resource_to_cfn
    data = security_group_to_yaml(
        ctx, logical_name, group_id, session=session, quiet=True)
    resources_to_import = [dict(
        ResourceType='AWS::EC2::SecurityGroup',
        LogicalResourceId=list(data.keys())[0],
        ResourceIdentifier=dict(GroupId=group_id),
    )]
    import_resource_to_cfn(
        data, resources_to_import,
        filename, None, skip_review, session, prefix)


@task(klass=AwsTask)
def security_groups(ctx, session=None, **kwargs):
    from ..ec2 import get_tag
    notice('loading security groups')
    ec2 = session.client('ec2')
    paginator = ec2.get_paginator('describe_security_groups')
    groups = []
    for page in paginator.paginate():
        groups += page['SecurityGroups']
    notice_end()
    header = [ 'id', 'name', 'tag_name', 'description' ]
    rows = []
    for group in groups:
        row = [
            group['GroupId'], group.get('GroupName', '')[:30],
            get_tag(group, 'name') or '', group.get('Description', '')[:30],
        ]
        rows.append(row)
    rows.sort(key=lambda lx: (lx[1] or lx[2]))
    print_table(header, rows)
