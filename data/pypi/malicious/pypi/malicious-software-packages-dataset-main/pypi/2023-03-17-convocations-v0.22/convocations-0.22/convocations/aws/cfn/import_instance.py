from raft import task
from ..base import AwsTask
from ..ec2 import instance_by_name
from ..ec2 import get_tag


def get_instance(ctx, name, instance_id, session, instance=None):
    if not instance:
        if name and not instance_id:
            instance = instance_by_name(ctx, name, session, None)
        elif instance_id:
            ec2 = session.resource('ec2')
            instance = ec2.Instance(instance_id)
    if not instance:
        return None, None
    name = get_tag(instance, 'name')
    return name, instance


@task(klass=AwsTask)
def instance_to_yaml(ctx, name=None, instance_id=None, instance=None,
                     session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for an instance
    """
    name, instance = get_instance(ctx, name, instance_id, session, instance)
    logical_name = ''.join(map(lambda lx: lx.title(), name.split('-')))
    volumes = [dict(
        Device=x['DeviceName'],
        VolumeId=x['Ebs']['VolumeId'],
    ) for x in instance.block_device_mappings]
    network_interfaces = [dict(
        DeviceIndex=n,
        NetworkInterfaceId=x.network_interface_id,
    ) for n, x in enumerate(instance.network_interfaces, 1)]
    security_group_ids = [ x['GroupId'] for x in instance.security_groups ]
    profile_name = (instance.iam_instance_profile or {}).get('Arn', '')
    profile_name = profile_name.rsplit('/', 1)[-1]
    properties = dict(
        EbsOptimized=instance.ebs_optimized,
        IamInstanceProfile=profile_name or None,
        ImageId=instance.image_id,
        InstanceType=instance.instance_type,
        KeyName=instance.key_name,
        NetworkInterfaces=network_interfaces,
        SecurityGroupIds=security_group_ids,
        SourceDestCheck=instance.source_dest_check,
        SubnetId=instance.subnet_id,
        Tags=instance.tags,
        Volumes=volumes,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::EC2::Instance',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        from convocations.base.utils import dump_yaml
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def import_instance(ctx, name=None, instance_id=None, filename=None,
                    skip_review=False, session=None, prefix=None, **kwargs):
    """
    creates a yaml template for an instance and imports it into cloudformation

    you can provide either the name of the instance or its instance id.
    if you specify both, the name will be ignored.
    if you specify the name, the instance id will be looked up based
      on a case-insensitive match with the name
    the filename is the name of the file and stack we will create

    if skip_review is set, we will immediately try to execute the change set
      in cloudformation
    """
    from .import_resource_to_cfn import import_resource_to_cfn
    name, instance = get_instance(ctx, name, instance_id, session)
    if not instance:
        return
    data = instance_to_yaml(
        ctx, None, None, instance,
        session=session, quiet=True)
    resources_to_import = [dict(
        ResourceType='AWS::EC2::Instance',
        LogicalResourceId=list(data.keys())[0],
        ResourceIdentifier=dict(InstanceId=instance.id),
    )]
    import_resource_to_cfn(
        data, resources_to_import,
        filename, name, skip_review, session, prefix)
