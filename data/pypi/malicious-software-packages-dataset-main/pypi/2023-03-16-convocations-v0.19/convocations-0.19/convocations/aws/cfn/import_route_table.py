from raft import task
from ..base import AwsTask


@task(klass=AwsTask)
def route_table_to_yaml(ctx, logical_name=None, route_table_id=None,
                        session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for a security group
    """
    ec2 = session.resource('ec2')
    table = ec2.RouteTable(route_table_id)
    properties = dict(
        VpcId=table.vpc_id,
        Tags=table.tags,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::EC2::RouteTable',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        from convocations.base.utils import dump_yaml
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def import_route_table(ctx, logical_name, route_table_id, filename,
                       skip_review=False, session=None, prefix=None,
                       **kwargs):
    """
    creates a yaml template for a route table and imports it into cloudformation

    if skip_review is set, we will immediately try to execute the change set
      in cloudformation
    """
    from .import_resource_to_cfn import import_resource_to_cfn
    data = route_table_to_yaml(
        ctx, logical_name, route_table_id, session=session, quiet=True)
    resources_to_import = [dict(
        ResourceType='AWS::EC2::RouteTable',
        LogicalResourceId=list(data.keys())[0],
        ResourceIdentifier=dict(RouteTableId=route_table_id),
    )]
    import_resource_to_cfn(
        data, resources_to_import,
        filename, None, skip_review, session, prefix)
