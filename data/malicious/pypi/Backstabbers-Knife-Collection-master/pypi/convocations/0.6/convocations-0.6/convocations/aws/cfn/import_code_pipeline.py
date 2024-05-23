from raft import task

from convocations.base.utils import notice_end, notice, print_table, dump_yaml
from ..base import AwsTask, yielder
from .import_resource_to_cfn import sync_resource


@task(klass=AwsTask)
def pipelines(ctx, name=None, **kwargs):
    """
    lists the code pipelines available in an account / region

    name: an optional substring, case-insensitive matcher (non-regex)
    """
    notice('getting pipelines')
    session = kwargs.pop('session')
    cp = session.client('codepipeline')
    response = list(yielder(cp, 'list_pipelines'))
    notice_end()
    rows = []
    name = (name or '').lower()
    for x in response:
        if name in x['name'].lower():
            rows.append([ x['name'], x['updated'].strftime('%Y-%m-%d') ])
    header = [ 'name', 'updated' ]
    print()
    print_table(header, rows)
    print()


@task(klass=AwsTask)
def code_build_projects(ctx, name=None, **kwargs):
    """
    lists the code projects available in an account / region

    name: an optional substring, case-insensitive matcher (non-regex)
    """
    notice('getting projects')
    session = kwargs.pop('session')
    cp = session.client('codebuild')
    response = list(yielder(cp, 'list_projects', sortBy='NAME'))
    notice_end()
    rows = []
    name = (name or '').lower()
    for x in response:
        if name in x.lower():
            rows.append([ x ])
    header = [ 'name' ]
    print()
    print_table(header, rows)
    print()


@task(klass=AwsTask)
def sync_pipeline(ctx, name, filename, logical_name=None, **kwargs):
    """
    prints the cloudformation for the current version of the pipeline
    named name so that we can remove drift from cloudformation

    :param str name: the name of the code pipeline in aws
    :param str filename: the yaml filename of the template without the `profile/cfn` prefix
    :param str logical_name: the logical name of the resource in the cloudformation template
    :param Context ctx: the convocation context
    """
    from .import_resource_to_cfn import to_pascal_case
    session = kwargs['session']
    cp = session.client('codepipeline')
    response = cp.get_pipeline(name=name)
    pline = response['pipeline']
    logical_name = logical_name or ''.join(map(lambda lx: lx.title(), name.split('-')))
    properties = dict(
        ArtifactStore=to_pascal_case(pline.get('artifactStore')) or None,
        ArtifactStores=to_pascal_case(pline.get('artifactStores')) or None,
        DisableInboundStageTransitions=None,
        Name=pline['name'],
        RestartExecutionOnUpdate=False,
        RoleArn=pline.get('roleArn'),
        Stages=to_pascal_case(pline.get('stages')),
        Tags=None,
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::CodePipeline:Pipeline',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    sync_resource(filename, logical_name, data)


@task(klass=AwsTask)
def code_build_project_yaml(ctx, name, quiet=False, **kwargs):
    """
    prints the cloudformation for the current version of the pipeline
    named name so that we can remove drift from cloudformation

    :param str name: the name of the code pipeline in aws
    :param bool quiet: set this flag to prevent output to stdout / stderr and return the yaml dictionary
    :param Context ctx: the convocation context
    """
    from .import_resource_to_cfn import to_pascal_case, filtered_tags
    session = kwargs['session']
    cb = session.client('codebuild')
    response = cb.batch_get_projects(names=[ name ])
    project = response['projects'][0]
    logical_name = ''.join(map(lambda lx: lx.title(), name.split('-')))
    tags = filtered_tags(project)
    properties = dict(
        Name=project['name'],
        Description=project.get('description'),
        Source=to_pascal_case(project['source']),
        SecondarySources=to_pascal_case(project.get('secondarySources')) or None,
        SourceVersion=project.get('sourceVersion'),
        SecondarySourceVersions=to_pascal_case(project.get('secondarySourceVersions')) or None,
        Artifacts=to_pascal_case(project.get('artifacts')) or None,
        SecondaryArtifacts=to_pascal_case(project.get('secondaryArtifacts')) or None,
        Cache=to_pascal_case(project.get('cache')) or None,
        Environment=to_pascal_case(project.get('environment')) or None,
        ServiceRole=project.get('serviceRole'),
        TimeoutInMinutes=project.get('timeoutInMinutes'),
        QueuedTimeoutInMinutes=project.get('queuedTimeoutInMinutes'),
        EncryptionKey=project.get('encryptionKey'),
        Tags=to_pascal_case(tags) or None,
        VpcConfig=project.get('vpcConfig') or None,
        BadgeEnabled=project.get('badge', {}).get('badgeEnabled'),
        LogsConfig=project.get('logsConfig') or None,
        FileSystemLocations=project.get('fileSystemLocations') or None,
        BuildBatchConfig=project.get('buildBatchConfig') or None,
        ConcurrentBuildLimit=project.get('concurrentBuildLimit'),
        ResourceAccessRole=project.get('resourceAccessRole'),
        Triggers=None,
        Visibility=project.get('projectVisibility'),
    )
    properties = { k: v for k, v in properties.items() if v is not None }
    data = {
        logical_name: dict(
            Type='AWS::CodeBuild::Project',
            DeletionPolicy='Retain',
            Properties=properties,
        ),
    }
    print()
    dump_yaml(data)
    print()
