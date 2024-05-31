from datetime import datetime
import time
from typing import Any

import pytz
from halo import Halo
from raft.tasks import task
from termcolor import cprint
from ...base.utils import notice, notice_end, get_context_value
from ...base.utils import print_table
from ..base import AwsTask


__all__ = [
    'build',
    'build_status',
    'build_logs',
    'stop_build',
    'running_builds',
    'show_phases',
    'recent_builds',
]


def as_bool(st: Any) -> bool:
    """
    converts a string or int to a boolean true / false value.  accepts
    `yes`, `true`, and `1` as true
    """
    if isinstance(st, str):
        return st.lower() in ( 'yes', 'true', '1' )
    return bool(st)


def yield_projects(client=None, session=None):
    if not client:
        client = session.client('codebuild')
    paginator = client.get_paginator('list_projects')
    for x in paginator.paginate():
        yield from x['projects']


def project_exists(project, client=None, session=None):
    notice(f'checking {project}')
    projects = list(yield_projects(client, session))
    if project in projects:
        notice_end()
        return True
    notice_end('not found')
    return False


@task(klass=AwsTask, help={
    'project': 'the name of the codebuild project',
    'branch': 'the git branch name that we want to build',
    'follow': 'specify this flag to follow the build after we kick it off',
    'verbose': 'specify this flag for more verbose output',
})
def build(ctx, project=None, branch='master', follow=True, verbose=False,
          session=None, **kwargs):
    """
    Kicks off a build of the specified project for the given branch

    e.g.,  convoke aws.build project1 -b branch1

    :param project:  the name of the codebuild project
    :param branch:   the branch name in git or bitbucket
    :param follow:   tail the build logs after kicking off
    :param verbose:  verbose build log output
    :param session:  don't fill this out, it will be filled in for us by
        `AwsTask`
    """
    client = session.client('codebuild')
    project = project or get_context_value(ctx, 'codebuild.project')
    if not project:
        notice_end('please specify a project')
        return
    if project_exists(project, client):
        notice('kicking off build')
        client.start_build(
            projectName=project,
            sourceVersion=branch,
        )
        notice_end()
    if as_bool(follow):
        notice('waiting 10 seconds for build to start')
        time.sleep(10)
        notice_end()
        build_logs(ctx, project, verbose=verbose, session=session)


def latest_build(project, client=None, session=None):
    notice('getting latest build id')
    client = client or session.client('codebuild')
    result = client.list_builds_for_project(
        projectName=project, sortOrder='DESCENDING')
    for x in result['ids']:
        notice_end(f'{x}')
        return x
    notice_end('waiting for godot')
    return None


def get_running_builds(project, client=None, session=None, **kwargs):
    notice('checking running builds')
    client = client or session.client('codebuild')
    result = client.list_builds_for_project(
        projectName=project, sortOrder='DESCENDING')
    build_ids = result['ids']
    result = client.batch_get_builds(ids=build_ids)
    running_build_ids = []
    for x in result['builds']:
        if x['buildStatus'] == 'IN_PROGRESS':
            running_build_ids.append(x['id'])
    if running_build_ids:
        n = len(running_build_ids)
        notice_end(f'{n} running build{"s" if n != -1 else ""}')
        return running_build_ids
    notice_end('waiting for godot')
    return []


@task(klass=AwsTask, help={
    'project': 'the codebuild project name',
    'n_max': 'the maximum number of recent builds to list',
})
def recent_builds(ctx, project=None, n_max=10, client=None,
                  session=None, **kwargs):
    """
    shows the n_max most recent builds in codebuild for this project
    """
    project = project or get_context_value(ctx, 'codebuild.project')
    if not project:
        notice_end('please specify a project')
        return
    notice('checking recent builds')
    client = client or session.client('codebuild')
    result = client.list_builds_for_project(
        projectName=project,
        sortOrder='DESCENDING')
    notice_end()
    build_ids = result['ids'][:n_max]
    notice('getting build details')
    result = client.batch_get_builds(ids=build_ids)
    notice_end()
    notice('keys')
    rows = []
    for i, x in enumerate(result['builds'], 1):
        if i == 1:
            notice_end(x.keys())
        rows.append((
            x['id'],
            x['buildStatus'],
            x['startTime'].isoformat(' ', 'seconds')))
    print_table([ 'build_id', 'status', 'started'], rows)


@task(klass=AwsTask, help={
    'project': 'name of the codebuild project',
    'session': 'do not use',
})
def running_builds(ctx, project=None, session=None, **kwargs):
    """
    prints a list of running build ids for a codebuild project
    """
    try:
        project = project or ctx.codebuild.project
    except AttributeError:
        notice_end('please specify a project to build')
        return
    build_ids = get_running_builds(project, session=session)
    if build_ids:
        print_table([ 'build_id' ], [ build_ids ])
    else:
        cprint('blue', 'no running builds\n')


@task(klass=AwsTask, help={
    'project': 'name of the codebuild project, optional',
    'build_id': 'the id of the build if you have it handy',
    'session': 'do not use',
})
def show_phases(ctx, project=None, build_id=None, client=None, session=None,
                **kwargs):
    """
    Shows the phases and their timings for a particular codebuild build
    :param str project: the name of the codebuild project
    :param raft.context.Context ctx: the convocation context
    :param str build_id: the build id of the codebuild build
    :param client: the boto3 codebuild client, if you have it handy
    :param boto3.Session session: the boto3 session, if you have it handy
    """
    client = client or session.client('codebuild')
    if not build_id:
        project = project or get_context_value(ctx, 'codebuild.project')
        if not project:
            notice_end('please specify a project')
            return
    build_id = build_id or latest_build(project, client, session)
    if build_id is None:
        notice_end('nothing to be done')
        return
    notice('getting build details')
    result = client.batch_get_builds(ids=[ build_id ])
    data = result['builds'][0]
    notice_end()
    phases = data['phases']
    fields = [ 'phaseType', 'phaseStatus', 'durationInSeconds' ]
    header = [ 'type', 'status', 'time' ]
    total_time = 0
    rows = []
    for x in phases:
        rows.append([ f'{x.get(field)}'.lower() for field in fields ])
        total_time += x.get('durationInSeconds', 0)
    rows.append([ '-----', '------', '-----' ])
    rows.append([ 'total time', '', f'{total_time}' ])
    print_table(header, rows)


def is_done(build_id, client, session=None) -> bool:
    """
    returns true if the codebuild build is done
    :param build_id: the build id in codebuild
    :param client: the boto3 codebuild client if we have it handy
    :param session: the boto3 session
    """
    client = client or session.client('codebuild')
    result = client.batch_get_builds(ids=[ build_id ])
    data = result['builds'][0]
    return data['buildStatus'] != 'IN_PROGRESS'


def format_log_line(message, verbose=False):
    if message.startswith('[Container]'):
        message = message[12:]
        dt = message[:19].strip()
        dt = datetime.strptime(dt, '%Y/%m/%d %H:%M:%S')
        dt = dt.replace(tzinfo=pytz.UTC)
        dt = dt.astimezone(pytz.timezone('CST6CDT'))
        message = message[20:]
        if message.startswith('Running command '):
            cprint('cyan', f"[{dt.strftime('%Y-%m-%d %H:%M:%S')}] ")
            message = f'----- {message[16:].strip()} -----'
            cprint('magenta', message)
            print()
        elif verbose:
            cprint('cyan', f"[{dt.strftime('%Y-%m-%d %H:%M:%S')}] ")
            print(message.strip())
        return
    print(message, end='')


def get_build_logs(project, build_id, start_time=None,
                   spinner=None, verbose=False, session=None):
    """
    codebuild stores logs in `/aws/codebuild/project`.  this function
    gets the build logs for the specified project and build_id from the
    specified start time, and formats the lines for output
    """
    from ..cloudwatch import yield_logs
    group_name = f'/aws/codebuild/{project}'
    stream_name = build_id.split(':')[-1]
    lines = list(yield_logs(group_name, stream_name, start_time, session))
    lines.sort(key=lambda lx: lx['timestamp'])
    for x in lines:
        if spinner:
            spinner.stop()
        format_log_line(x['message'], verbose)
    last_time = None
    if lines:
        last_time = lines[-1]['timestamp']
    return last_time


@task(klass=AwsTask, help=dict(
    build_id='optional, the build id of the codebuild project',
    project='optional, the name of the project',
), positional=[ 'project' ])
def build_status(ctx, project=None, build_id=None, session=None, **kwargs):
    """
    Shows the build status of the latest build of a codebuild project
    """
    client = session.client('codebuild')
    project = project or get_context_value(ctx, 'codebuild.project')
    if not project:
        notice_end('please specify a project')
        return
    build_id = build_id or latest_build(project, client)
    if build_id:
        show_phases(build_id, client)


@task(klass=AwsTask, help={
    'project': 'name of the codebuild project',
    'session': 'do not use',
})
def build_logs(ctx, project=None, build_id=None, verbose=False, session=None, **kwargs):
    """
    Tails the build logs of a codebuild project
    :param raft.context.Context ctx: the convocation context
    :param project: the name of the codebuild project
    :param build_id: the id of the codebuild build
    :param verbose: specify true / false for verbose logs
    :param session: don't fill this parameter in, it is injected
    """
    client = session.client('codebuild')
    project = project or get_context_value(ctx, 'codebuild.project')
    if not project:
        notice_end('please specify a project')
        return
    logs = session.client('logs')
    if isinstance(verbose, str) and verbose.lower() in [ 'yes', 'true' ]:
        verbose = True
    if not build_id:
        build_ids = get_running_builds(project, client)
        if build_ids:
            build_id = build_ids[0]
        else:
            build_id = latest_build(project, client)
            if not build_id:
                return
    start_time = None
    spinner = Halo('waiting')
    following = False
    for _ in range(6):
        try:
            if not spinner.spinner_id:
                spinner.start()
            while not is_done(build_id, client):
                next_time = get_build_logs(
                    project, build_id, start_time,
                    spinner, verbose, session)
                if not spinner.spinner_id:
                    spinner.start()
                start_time = next_time or start_time
                time.sleep(1)
                following = True
            if following:
                spinner.succeed('finished building')
                with Halo('waiting 5 seconds for cloudwatch cool down') as s:
                    time.sleep(5)
                    s.succeed()
            get_build_logs(
                project, build_id, start_time,
                None, verbose, session)
            break
        except logs.exceptions.ResourceNotFoundException:
            spinner.stop()
            notice_end('no build logs found')
            with Halo('waiting 3 seconds before retry'):
                time.sleep(3)


@task(klass=AwsTask, help={
    'project_or_build_id':
        'name of the codebuild project or the id of the codebuild'
        ' build that you want to stop',
    'session': 'do not use',
})
def stop_build(ctx, project_or_build_id=None, session=None, **kwargs):
    """
    stops the most running, still running build, if one exists

    :param raft.context.Context ctx: the convocation context
    :param str project_or_build_id: the name of the codebuild project
    :param session: don't fill this parameter in, it is injected
    """
    client = session.client('codebuild')
    try:
        project_or_build_id = project_or_build_id or ctx.codebuild.project
    except AttributeError:
        notice_end('please specify a project or build_id')
        return
    project, build_id = project_or_build_id, None
    if ':' in project:
        build_id = project
        project = project.split(':')[0]
    build_ids = get_running_builds(project, client)
    for x in build_ids:
        if build_id and x != build_id:
            continue
        notice(f'stopping {x}')
        client.stop_build(id=x)
        notice_end()
        break
