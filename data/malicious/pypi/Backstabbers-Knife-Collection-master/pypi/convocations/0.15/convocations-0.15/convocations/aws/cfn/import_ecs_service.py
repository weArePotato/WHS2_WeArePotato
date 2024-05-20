from raft import task
from convocations.base.utils import notice, notice_end
from convocations.base.utils import print_table, dump_yaml
from ..base import AwsTask, yielder


def get_service(ctx, name, cluster, session):
    """
    gets a service by name, case-insensitve
    """
    ecs = session.client('ecs')
    notice(f'looking for ecs service [{name}]')
    found_services = ecs_services(ctx, name, cluster, session=session, quiet=True)
    if not found_services:
        notice_end('nothing found')
        return None
    notice_end(len(found_services))
    name = name.lower()
    cluster, service = None, None
    if len(found_services) > 1:
        for x, y in found_services:
            if y.lower() == name:
                cluster, service = x, y
                break
    if not cluster:
        cluster, service = found_services[0]
    response = ecs.describe_services(cluster=cluster, services=[ service ])
    services = response.get('services')
    if services:
        notice_end()
        return services[0]
    notice_end('not found')
    return None


def get_cluster(name, session):
    notice(f'looking up {name}')
    ecs = session.client('ecs')
    response = ecs.describe_clusters(clusters=[ name ], include=[
        'ATTACHMENTS', 'CONFIGURATIONS', 'SETTINGS', 'TAGS',
    ])
    clusters = response['clusters']
    if not clusters:
        notice_end('not found')
        return None
    return clusters[0]


def get_task_definition(name, session):
    """
    gets a task definition given the  name of the task definition.

    if just the family name for the ecs task is provided, we will
    get the definition for the highest-numbered, active task definition.
    to get a particular task definition, send in the `family_name:version`
    formatted name.
    """
    ecs = session.client('ecs')
    notice(f'describing [{name}]')
    response = ecs.describe_task_definition(taskDefinition=name)
    t_def = response.get('taskDefinition')
    arn = t_def['taskDefinitionArn']
    notice_end(arn.rsplit('/', 1)[-1])
    return t_def


@task(klass=AwsTask)
def service_to_yaml(ctx, name=None, cluster=None, session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for an ecs service
    """
    from .import_resource_to_cfn import to_pascal_case
    service = get_service(ctx, name, cluster, session)
    if not service:
        return None
    logical_name = ''.join(map(lambda lx: lx.title(), name.split('-')))
    load_balancers = to_pascal_case(service['loadBalancers'])
    service_registries = to_pascal_case(service.get('serviceRegistries'))
    capacity_provider_strategy = to_pascal_case(service.get('capacityProviderStrategy'))
    properties = dict(
        CapacityProviderStrategy=capacity_provider_strategy,
        Cluster=service['clusterArn'].split('/', 1)[-1],
        DeploymentConfiguration=to_pascal_case(service.get('deploymentConfiguration')),
        DeploymentController=None,
        DesiredCount=service['desiredCount'],
        EnableECSManagedTags=service.get('enableECSManagedTags'),
        EnableExecuteCommand=service.get('enableExecuteCommand'),
        HealthCheckGracePeriodSeconds=service.get('healthCheckGracePeriodSeconds'),
        LaunchType=service['launchType'],
        LoadBalancers=load_balancers or None,
        NetworkConfiguration=to_pascal_case(service.get('networkConfiguration')) or None,
        PlacementConstraints=to_pascal_case(service.get('placementConstraints')) or None,
        PlacementStrategies=to_pascal_case(service.get('placementStrategy')) or None,
        PlatformVersion=service.get('platformVersion'),
        PropagateTags=service.get('propagateTags'),
        Role=service.get('roleArn'),
        SchedulingStrategy=service.get('schedulingStrategy') or None,
        ServiceConnectConfiguration=None,
        ServiceName=service['serviceName'],
        ServiceRegistries=service_registries or None,
        Tags=to_pascal_case(service.get('tags')) or None,
        TaskDefinition=service['taskDefinition'].split('/', 1)[-1],
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::ECS::Service',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def cluster_to_yaml(ctx, name=None, session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for an ecs service
    """
    from .import_resource_to_cfn import to_pascal_case
    cluster = get_cluster(name, session)
    if not cluster:
        return None
    logical_name = ''.join(map(lambda lx: lx.title(), name.split('-')))
    properties = dict(
        CapacityProviders=cluster.get('capacityProviders') or None,
        ClusterName=cluster['clusterName'],
        ClusterSettings=to_pascal_case(cluster.get('settings')) or None,
        Configuration=to_pascal_case(cluster.get('configuraiton')) or None,
        DefaultCapacityProviderStrategy=to_pascal_case(cluster.get('defaultCapacityProviderStrategy')) or None,
        ServiceConnectDefaults=to_pascal_case(cluster.get('serviceConnectDefaults')) or None,
        Tags=to_pascal_case(cluster.get('tags')) or None,
    )

    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::ECS::Cluster',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def task_definition_to_yaml(ctx, name=None, session=None, quiet=False, **kwargs):
    """
    generates the cloudformation yaml for an ecs task definition
    """
    from .import_resource_to_cfn import to_pascal_case
    t_def = get_task_definition(name, session)
    if not t_def:
        return None
    logical_name = ''.join(map(lambda lx: lx.title(), name.split('-')))
    properties = dict(
        ContainerDefinitions=to_pascal_case(t_def['containerDefinitions'], exclude=['Options']),
        Cpu=t_def.get('cpu'),
        EphemeralStorage=to_pascal_case(t_def.get('ephemeralStorage')) or None,
        ExecutionRoleArn=t_def.get('executionRoleArn'),
        Family=t_def.get('family'),
        InferenceAccelerators=to_pascal_case(t_def.get('inferenceAccelerators')) or None,
        IpcMode=t_def.get('ipcMode'),
        Memory=t_def.get('memory'),
        NetworkMode=t_def.get('networkMode'),
        PidMode=t_def.get('pidModer'),
        PlacementConstraints=to_pascal_case(t_def.get('placementsConstraints')) or None,
        ProxyConfiguration=to_pascal_case(t_def.get('proxyConfiguration')) or None,
        RequiresCompatibilities=t_def.get('requiresCompatabilities') or None,
        RuntimePlatform=to_pascal_case(t_def.get('runtimePlatform')) or None,
        Tags=to_pascal_case(t_def.get('tags')) or None,
        TaskRoleArn=t_def.get('taskRoleArn'),
        Volumes=to_pascal_case(t_def.get('volumes')) or None,
    )

    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::ECS::TaskDefinition',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    if not quiet:
        dump_yaml(data)
    return data


@task(klass=AwsTask)
def ecs_clusters(ctx, name=None, session=None, quiet=False, **kwargs):
    """
    lists all ecs clusters that contain `name` in their name or name tag
    """
    rows = []
    clusters = []
    if not quiet:
        notice('listing clusters')
    for x in yielder('ecs', 'list_clusters', session=session):
        short_name = x.rsplit('/', 1)[-1]
        if not name or name.lower() in short_name.lower():
            clusters.append(short_name)
            rows.append([ short_name ])
    if not quiet:
        notice_end(len(clusters))
    if not quiet:
        rows.sort(key=lambda lx: lx[0])
        print()
        print_table([ 'name' ], rows)
        print()
    clusters.sort()
    return clusters


@task(klass=AwsTask)
def ecs_services(ctx, name=None, cluster=None, session=None, quiet=False, **kwargs):
    """
    lists all ecs services that contain `name` in their name or name tag

    * searches across all clusters
    """
    rows = []
    clusters = ecs_clusters(ctx, cluster, session=session, quiet=quiet)
    if not clusters:
        return []
    services = []
    for k in clusters:
        if not quiet:
            notice(f'listing cluster {k}')
        params = dict(cluster=k)
        service_rows = []
        for x in yielder('ecs', 'list_services', **params, session=session):
            short_name = x.rsplit('/', 1)[-1]
            if not name or name.lower() in short_name.lower():
                service_rows.append([ short_name, k ])
                services.append([ k, short_name ])
        rows += service_rows
        if not quiet:
            notice_end(len(service_rows))
    if not quiet:
        print()
        print_table([ 'name', 'cluster' ], rows)
        print()
    return services
