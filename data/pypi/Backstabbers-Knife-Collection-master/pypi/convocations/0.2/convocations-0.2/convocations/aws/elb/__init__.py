from raft.tasks import task
from ...base.utils import notice, notice_end, print_table
from ..base import yielder, AwsTask, name_tag, get_path
from ..ec2 import get_tag, yield_instances, yield_instances_by_id
from ..wait_helpers import wait


__all__ = [
    'register',
    'deregister',
    'lb_health',
]


def yield_lbs(name='', exact=False, session=None, prefix=None):
    """
    Yields all ec2 classic load balancers that have the `Name` that
    matches the provided name.  If `exact` is `True`, the
    instance's name must match the `name` parameter exactly.
    All matching is case-insensitive
    """
    from botocore.exceptions import ClientError

    if name:
        name = name.lower()
    for x in yielder('elb', 'describe_load_balancers', session=session):
        x['name'] = x['LoadBalancerName']
        l_name = x['name'].lower()
        if not name:
            yield x
        elif name in l_name:
            if not exact or name == l_name:
                yield x
    try:
        for x in yielder('elbv2', 'describe_target_groups', session=session):
            x['name'] = x['TargetGroupName']
            l_name = x['name'].lower()
            if not name:
                yield x
            elif name in l_name:
                if not exact or name == l_name:
                    yield x
    except ClientError as ex:
        if ex.response['Error']['Code'] != 'TargetGroupNotFound':
            raise


def yield_target_groups(name='', exact=True, session=None, prefix=None):
    """
    Yields all target groups that have `Name` that
    matches the provided name.  If `exact` is `True`, the
    instance's name must match the `name` parameter exactly.
    All matching is case-insensitive
    """
    if name:
        name = name.lower()
    client = session.client('elbv2')
    for x in yielder('elbv2', 'describe_target_groups', session=session):
        x['name'] = target_group = x['TargetGroupName'].lower()
        if not name:
            yield x
        elif name in target_group:
            if not exact or name == target_group:
                yield x
        arn = x['TargetGroupArn']
        tags = client.describe_tags(ResourceArns=[arn])
        if tags['TagDescriptions']:
            tags = tags['TagDescriptions'][0]
            x['name'] = target_group = name_tag(tags)
            if name in target_group:
                yield x


def _deregister(lb, instances, session=None):
    is_target_group = 'TargetGroupArn' in lb
    client = 'elbv2' if is_target_group else 'elb'
    elb = session.client(client)
    lb_name = lb['name']
    names = [ get_tag(instance, 'name') for instance in instances ]
    notice(f"disabling {','.join(names)} on {lb_name}")
    if is_target_group:
        arn = lb['TargetGroupArn']
        instance_ids = [{ 'Id': x['InstanceId'] } for x in instances ]
        kwargs = dict(
            TargetGroupArn=arn,
            Instances=instance_ids,)
        elb.deregister_targets(**kwargs)
    else:
        instance_ids = [{ 'InstanceId': x['InstanceId'] } for x in instances ]
        kwargs = dict(
            LoadBalancerName=lb_name,
            Instances=instance_ids,)
        elb.deregister_instances_from_load_balancer(**kwargs)
    notice_end()
    waiter = 'target' if is_target_group else 'instance'
    waiter = elb.get_waiter(f'{waiter}_deregistered')
    wait(waiter, 'instances to deregister', **kwargs)


def _register(lb_or_target_group, instances, session=None):
    is_target_group = 'TargetGroupName' in lb_or_target_group
    client = session.client('elbv2' if is_target_group else 'elb')
    name = lb_or_target_group['name']
    arn = lb_or_target_group.get('TargetGroupArn')
    names = [ get_tag(instance, 'name') for instance in instances ]
    notice(f"enabling {','.join(names)} on {name}")
    if is_target_group:
        instance_ids = [{ 'Id': x['InstanceId'] } for x in instances ]
        kwargs = dict(
            TargetGroupArn=arn,
            Targets=instance_ids,
        )
        client.register_targets(**kwargs)
    else:
        instance_ids = [{ 'InstanceId': x['InstanceId'] } for x in instances ]
        kwargs = dict(
            LoadBalancerName=name,
            Instances=instance_ids,)
        client.register_instances_with_load_balancer(**kwargs)
    notice_end()
    if is_target_group:
        waiter = client.get_waiter('target_in_service')
    else:
        waiter = client.get_waiter('instance_in_service')
    wait(waiter, 'new instances to come into service', **kwargs)


def lookup_load_balancers(lb_name, session):
    notice(f'looking for load balancers {lb_name}')
    rg = list(yield_lbs(lb_name, session=session))
    if not rg:
        notice_end('not found')
        notice(f'looking for target groups {lb_name}')
        rg = list(yield_target_groups(lb_name, session=session))
        if not rg:
            notice_end('nothing found')
            return []
    names = [ x['name'] for x in rg ]
    notice_end(','.join(names))
    return rg


@task(klass=AwsTask)
def register(ctx, lb_name, instance_name, session=None, prefix=None):
    """
    Registers an instance with a load balancer or a target group

    Args:
         lb_name -- the name of the load balancer or target group
         instance_name -- the value of the name tag on the instance
    """
    rg = lookup_load_balancers(lb_name, session)
    notice(f'finding {instance_name}')
    instances = list(yield_instances(instance_name, session))
    names = [ get_tag(x, 'Name') for x in instances ]
    notice_end(','.join(names))
    _register(rg[0], instances, session)


@task(klass=AwsTask)
def deregister(ctx, lb_name, instance_name, session=None, prefix=None):
    """
    Deregisters an instance from a load balancer

    Args:

        ctx (raft.context.Context): the convocation context
        lb_name (str): name of the load balancer
        instance_name (str): name of the instance
        session (boto3.Session): don't specify this
        prefix: don't specify this either
    """
    load_balancers = lookup_load_balancers(lb_name, session)
    notice(f'finding {instance_name}')
    instances = list(yield_instances(instance_name, session))
    names = [ x['InstanceId'] for x in instances ]
    notice_end(','.join(names))
    _deregister(load_balancers[0], instances, session)


@task(klass=AwsTask)
def lb_health(ctx, name, session=None, **kwargs):
    """
    Displays the health of the targets on a load balancer
    """
    load_balancers = lookup_load_balancers(name, session)
    if not load_balancers:
        return
    header = [ 'lb', 'name', 'id', 'state',  ]
    rows = []
    for load_balancer in load_balancers:
        name = load_balancer['name']
        is_target_group = 'TargetGroupArn' in load_balancer
        client_name = 'elbv2' if is_target_group else 'elb'
        notice(f'checking health of {name}')
        client = session.client(client_name)
        if is_target_group:
            health_response = client.describe_target_health(
                TargetGroupArn=load_balancer['TargetGroupArn'],
            )
            health_response = health_response['TargetHealthDescriptions']
            id_key = 'Target.Id'
            state_key = 'TargetHealth.State'
            reason_key = 'TargetHealth.Reason'
        else:
            health_response = client.describe_instance_health(
                LoadBalancerName=load_balancer['LoadBalancerName'],
            )
            health_response = health_response['InstanceStates']
            id_key = 'InstanceId'
            state_key = 'State'
            reason_key = 'ReasonCode'
        instance_ids, ips = [], []
        for x in health_response:
            value = get_path(x, id_key)
            if value.startswith('i-'):
                instance_ids.append(value)
            else:
                ips.append(value)
        notice_end()
        notice('looking up instances')
        instances = {
            x['InstanceId']: x
            for x in yield_instances_by_id(session, instance_ids)
        }
        for x in ips:
            instances[x] = x
        notice_end()
        for x in health_response:
            instance_id = get_path(x, id_key)
            if instance_id.startswith('i-'):
                instance = instances[instance_id]
                instance_name = get_tag(instance, 'Name')
            else:
                instance_name = instance_id
            rows.append([
                name,
                instance_name,
                instance_id,
                get_path(x, state_key, ''),
            ])
    print_table(header, rows)
