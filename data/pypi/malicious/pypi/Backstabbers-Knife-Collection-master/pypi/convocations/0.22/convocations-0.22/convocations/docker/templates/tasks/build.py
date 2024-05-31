import os
import posixpath

from raft import task


names = [ 'cscshared/{{ name }}', ]


def short_name():
    """
    returns the shortname for the docker image

    for example, the shortname for namespace/short_name:tag will be `short_name`
    """
    for name in names:
        name = posixpath.basename(name)
        name = name.split(':', 1)[0]
        return name


def local_tag():
    return f'{short_name()}:local'


@task
def build(ctx):
    """
    builds the docker image
    """
    ctx.run(f'docker build -t {local_tag()} .')


@task
def bump_version(ctx, which=None):
    """
    bumps the version for publishing
    """
    if 'CODEBUILD_BUILD_ID' in os.environ:
        print('in codebuild, skipping')
        return
    if not which:
        minor = version().rsplit('.', 2)[-1]
        which = 'major' if minor == '9' else 'minor'
    ctx.run(f'bumpversion {which}')
    ctx.run('git push --all')


def version():
    with open('version.txt', 'r') as f:
        st = f.read()
        st = st.strip()
    return st


def tags():
    for name in names:
        for x in [ version(), 'latest' ]:
            yield f'{name}:{x}'


@task
def tag(ctx):
    """
    tags the build with the appropriate version(s)
    """
    for image in tags():
        print(f'tagging {image}')
        ctx.run(f'docker tag {local_tag()} {image}')


def image_exists(ctx, image):
    """
    uses the docker manifest cli to determine if an image is available in the
    remote
    """
    result = ctx.run(f'docker manifest inspect {image}', warn=True, hide=True)
    return not bool(result.return_code)


@task()
def publish(ctx, profile=None, local=False):
    """
    publishes the image to docker hub and ecr as needed
    """
    if 'CODEBUILD_BUILD_ID' not in os.environ and not local:
        bump_version(ctx)
        return
    build(ctx)
    bump_version(ctx)
    tag(ctx)
    if local:
        profile_arg = f'--profile={profile}' if profile else ''
        d = os.getcwd()
        ctx.run(f"eval $({d}/venv/bin/aws "
                f"{profile_arg} ecr get-login --no-include-email)")
    for image in tags():
        if not image_exists(ctx, image):
            print(f'pushing {image}')
            ctx.run(f'docker push {image}')
