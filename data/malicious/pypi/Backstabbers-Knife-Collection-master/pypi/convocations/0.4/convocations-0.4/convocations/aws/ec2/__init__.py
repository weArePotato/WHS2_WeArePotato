from math import ceil
import time

from halo import Halo
from raft.tasks import task
from ..base import AwsTask, name_tag, yielder, get_tag
from ...base.utils import notice, notice_end, print_table, confirm


def aws_filter(name, *values):
    return {
        'Name': name,
        'Values': values
    }


def instance_state(instance):
    return instance['State']['Name'].lower()


@task(klass=AwsTask)
def recycle_instances(ctx, name, profile=None, session=None):
    instance_ids = []
    for x in yield_instances(session=session):
        i_name = name_tag(x)
        state = instance_state(x)
        if name in i_name and state == 'running':
            instance_ids.append(x['InstanceId'])
    response = confirm(
        f'You are about to delete the following '
        f'[{len(instance_ids)}] instances: '
        f'{", ".join(instance_ids)}')
    if response:
        ec2 = session.client('ec2')
        ec2.terminate_instances(InstanceIds=instance_ids)


def yield_instances(name=None, session=None):
    if name:
        name = name.lower()
    for data in yielder('ec2', 'describe_instances', session=session):
        if name:
            for x in data['Instances']:
                value = get_tag(x, 'Name') or ''
                value = value.lower()
                if name in value.lower():
                    yield x
                if x['InstanceId'] == name:
                    yield x
        else:
            yield from data['Instances']


def yield_instances_by_id(session, instance_ids):
    gn = yielder(
        'ec2', 'describe_instances',
        session=session, InstanceIds=instance_ids)
    for data in gn:
        yield from data['Instances']


@task(klass=AwsTask)
def instances(ctx, name=None, session=None, profile=None, **kwargs):
    """
    summary of instances with `name` in their `Name` tag."
    """
    header = [ 'name', 'id', 'type', 'private', 'public', 'status' ]
    rows = []
    matching_instances = []
    for x in yield_instances(name, session):
        if x['State']['Name'] == 'terminated':
            continue
        interfaces = x['NetworkInterfaces']
        public_ip = private_ip = None
        if interfaces:
            private_ip = interfaces[0]['PrivateIpAddress']
            public_ip = interfaces[0].get('PublicIpAddress', '')
        if not private_ip:
            private_ip = x.get('PrivateIpAddress', '')
        if not public_ip:
            public_ip = x.get('PublicIpAddress', '')
        rows.append([
            get_tag(x, 'name'),
            x['InstanceId'],
            x['InstanceType'],
            private_ip,
            public_ip,
            x['State']['Name'],
        ])
        matching_instances.append(x)
    rows.sort(key=lambda lx: lx[0])
    if not rows:
        print()
        print(f'nothing found matching {name}')
    else:
        print_table(header, rows)
    return matching_instances


def tag(key, value):
    return {
        'Key': key,
        'Value': value,
    }


def instance_by_name(ctx, name, session=None, prefix=None):
    notice(f'looking for {name}')
    matching_instances = list(yield_instances(name, session))
    matching_instances = [
        x for x in matching_instances
        if instance_state(x) != 'terminated'
    ]
    if not matching_instances:
        notice_end('nothing found, please halp')
    elif len(matching_instances) > 1:
        notice_end('multiple instances found')
        for instance in matching_instances:
            instance_id = instance['InstanceId']
            if name.lower() == name_tag(instance) or name.lower() == instance_id:
                ec2 = session.resource('ec2')
                x = ec2.Instance(instance_id)
                return x
        instances(ctx, name, session, prefix=prefix)
        return None
    instance = matching_instances[0]
    instance_id = instance['InstanceId']
    notice_end(instance_id)
    notice(f'loading instance {instance_id}')
    ec2 = session.resource('ec2')
    x = ec2.Instance(instance_id)
    notice_end()
    return x


def move_volume(
        ctx, from_name, to_name, volume_id=None,
        device_name='/dev/xvdf',
        session=None, prefix=None):
    """
    moves volume to a forensic instance for analysis
    """
    from_instance = instance_by_name(ctx, from_name)
    if not from_instance:
        return
    to_instance = instance_by_name(ctx, to_name)
    if not to_instance:
        return
    rg_volumes = from_instance.block_device_mappings
    if len(rg_volumes) > 1 and not volume_id:
        print(f'{from_name} has {len(rg_volumes)} volumes; '
              f'we don\'t know what to do')
        return
    volume_id = volume_id or rg_volumes[0]['Ebs']['VolumeId']
    notice('loading volume')
    ec2 = session.resource('ec2')
    volume = ec2.Volume(volume_id)
    volume.load()
    current_name = name_tag(volume)
    if not current_name:
        volume.create_tags(Tags=[tag('Name', name_tag(from_instance))])
    volume.load()
    current_name = name_tag(volume)
    notice_end(f'{current_name}')
    notice(f'detaching {volume_id}')
    volume.detach_from_instance()
    notice_end()
    with Halo('detaching volume', spinner='dots') as h:
        for x in range(20):
            time.sleep(1)
            volume.load()
            if volume.state == 'available':
                h.succeed('finished')
    volume.load()
    notice(f'attaching {volume_id} to {to_instance.instance_id}')
    volume.attach_to_instance(
        Device=device_name,
        InstanceId=to_instance.instance_id)
    notice_end()


def move_back_volume(
        ctx, from_name, to_name,
        device_name='/dev/sda1',
        session=None, prefix=None):
    """
    Puts the volume back on the original instance it came from now that
    we're done with forensics.
    """
    from_name = from_name.lower()
    from_instance = instance_by_name(ctx, from_name, session, prefix)
    if not from_instance:
        return
    to_name = to_name.lower()
    to_instance = instance_by_name(ctx, to_name, session, prefix)
    if not to_instance:
        return
    rg_volumes = from_instance.block_device_mappings
    current_name = 'not-a-real-name'
    volume, volume_id = None, None
    for x in rg_volumes:
        volume_id = x['Ebs']['VolumeId']
        notice(f'loading {volume_id}')
        ec2 = session.resource('ec2')
        volume = ec2.Volume(volume_id)
        volume.load()
        current_name = name_tag(volume)
        if current_name == to_name:
            notice_end('found!')
            break
        volume = None
        notice_end('not it')
    if current_name != to_name:
        notice_end('nothing to be done')
        return
    notice(f'detaching {volume_id}')
    volume.detach_from_instance()
    notice_end()
    with Halo('detaching volume', spinner='dots') as h:
        for x in range(20):
            time.sleep(1)
            volume.load()
            if volume.state == 'available':
                h.succeed('finished')
                break
    volume.load()
    notice(f'attaching {volume_id} to {to_instance.instance_id}')
    volume.attach_to_instance(
        Device=device_name,
        InstanceId=to_instance.instance_id)
    notice_end()
    notice('modifying instance')
    to_instance.load()
    to_instance.modify_attribute(
        Attribute='blockDeviceMapping',
        BlockDeviceMappings=[{
            'DeviceName': device_name,
            'Ebs': {
                'DeleteOnTermination': True,
            }
        }]
    )
    notice_end('done')


def rename_instance(ctx, old_name, new_name, session=None, prefix=None):
    notice(f'looking for {old_name}')
    matching_instances = list(yield_instances(old_name, session))
    if not matching_instances:
        notice_end('nothing found, please halp')
    elif len(matching_instances) > 1:
        notice_end('multiple instances found')
        instances(old_name, session, prefix=prefix)
    else:
        instance = matching_instances[0]
        instance_id = instance['InstanceId']
        notice_end(instance_id)
        notice(f'loading instance {instance_id}')
        ec2 = session.resource('ec2')
        x = ec2.Instance(instance_id)
        notice_end()
        # the create_tags api call will create a new tag *or update*
        # an existing tag.
        notice(f'changing name to {new_name}')
        x.create_tags(Tags=[tag('Name', new_name)])
        notice_end()


@task(klass=AwsTask, help={
    'name': 'the matching name of the instance(s) to start',
    'wait': 'specify this flag to wait for the command to finish',
    'force': 'specify this flag to force stop the instances, as '
             'opposed to a graceful shutdown',
})
def stop_instances(ctx, name, force=False, wait=True, session=None, prefix=None):
    """
    stops all instances with `name` in their `Name` tag.
    """
    matching_instances = instances(name, session)
    notice(f'looking for {name}')
    matching_instances = [
        x for x in matching_instances
        if instance_state(x) == 'running' ]
    notice_end(f'found {len(matching_instances)}')
    if not matching_instances:
        notice_end('no running instances to stop')
        return

    proceed = confirm(f'Stopping {len(matching_instances)} running instance(s)')
    if not proceed:
        return

    instance_ids = [ x['InstanceId'] for x in matching_instances ]
    client = session.client('ec2')
    client.stop_instances(InstanceIds=instance_ids, Force=force)
    if not wait:
        return
    with Halo(text='waiting', spinner='dots') as h:
        waiter = client.get_waiter('instance_stopped')
        waiter.config.delay = 15
        waiter.config.max_attempts = 40
        waiter.wait(InstanceIds=instance_ids)
        h.succeed('✔')


@task(klass=AwsTask, help={
    'name': 'the matching name of the instance(s) to start',
    'wait': 'specify this flag to wait for the command to finish'
})
def start_instances(ctx, name, wait=True, session=None, prefix=None):
    """
    starts all instances that have `name` in their `Name` tag.
    """
    matching_instances = instances(name, session)
    notice(f'looking for {name}')
    matching_instances = [
        x for x in matching_instances
        if instance_state(x) == 'stopped' ]
    notice_end(f'found {len(matching_instances)}')

    if not matching_instances:
        notice_end('no stopped instances to start')
        return

    proceed = confirm(f'Starting {len(matching_instances)} stopped instance(s)')
    if not proceed:
        return

    instance_ids = [ x['InstanceId'] for x in matching_instances ]
    client = session.client('ec2')
    client.start_instances(InstanceIds=instance_ids)
    if not wait:
        return
    with Halo(text='waiting', spinner='dots') as h:
        waiter = client.get_waiter('instance_running')
        waiter.config.delay = 3
        waiter.config.max_attempts = 200
        waiter.wait(InstanceIds=instance_ids)
        h.succeed('✔')


@task(klass=AwsTask, help={
    'n': 'the 1-based index of the volume we want to resize',
    'name': 'the name of the instance',
    'scale': 'the percent increase we want in the volume size, '
             'defaults to 100 (i.e., grow by 2x)',
})
def increase_volume_size(
        ctx, name, scale=100, index=0, session=None, prefix=None):
    """
    increases a volume by `scale` percent.
    """
    instance = instance_by_name(ctx, name, session, prefix)
    ec2 = session.resource('ec2')
    if not instance:
        return
    rg_volumes = instance.block_device_mappings
    for i, x in enumerate(rg_volumes, 1):
        notice(f'volume #{i}')
        volume_id = x['Ebs']['VolumeId']
        volume = ec2.Volume(volume_id)
        volume.load()
        x['volume'] = volume
        notice_end(f'{volume_id} / {volume.size} gb')
    if len(rg_volumes) > 1 and not index:
        print(f'{name} has {len(rg_volumes)} volumes; '
              f'we don\'t know what to do')
        return
    n = index or 1
    volume = rg_volumes[n - 1]['volume']
    volume_id = volume.volume_id
    new_size = volume.size * (1 + scale / 100)
    new_size = ceil(new_size)
    notice(f'increasing {volume_id} to {new_size} gb')
    client = session.client('ec2')
    client.modify_volume(VolumeId=volume_id, Size=new_size)
    notice_end('OK')


@task(klass=AwsTask, help={
    'name': 'the name of the instance as specified in a name tag or instance id'
})
def volumes(ctx, name, session=None, prefix=None):
    """
    lists all volumes attached to an instance
    """
    instance = instance_by_name(ctx, name, session, prefix)
    ec2 = session.resource('ec2')
    if not instance:
        return
    rg_volumes = instance.block_device_mappings
    header = [ 'volume_id', 'size', 'state', 'attachments ']
    rows = []
    for x in rg_volumes:
        volume_id = x['Ebs']['VolumeId']
        notice('volume')
        volume = ec2.Volume(volume_id)
        volume.load()
        notice_end(f'{volume_id} / {volume.size} gb')
        rows.append([
            volume_id, f'{volume.size}', volume.state,
            volume.attachments[0]['Device']
        ])
    print_table(header, rows)


@task(klass=AwsTask)
def eips(ctx, session=None, profile=None, **kwargs):
    """
    shows all eips in a given account
    """
    ec2 = session.client('ec2')
    addresses = ec2.describe_addresses()
    addresses = addresses['Addresses']
    header = [ 'name', 'ip_address', 'allocation_id' ]
    rows = []
    for x in addresses:
        rows.append([
            name_tag(x),
            x.get('PublicIp') or '',
            x['AllocationId'],
        ])
    print()
    print_table(header, rows)
