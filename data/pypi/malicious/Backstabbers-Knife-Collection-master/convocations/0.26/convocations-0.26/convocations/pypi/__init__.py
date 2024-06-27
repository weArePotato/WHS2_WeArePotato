from raft import task
from raft.collection import Collection


def render(env, source, destination, context=None):
    """
    :param jinja2.Environment env:
    :param str source:
    :param str destination:
    :param dict[Any, Any] context:
    """
    t = env.get_template(source)
    context = context or {}
    body = t.render(**context)
    with open(destination, 'w') as f:
        f.write(body)


@task(help=dict(
    name='the name of the project',
    path='the parent directory in which {name} will be created',
    source_dir='the name of the source directory within our project, for '
               'most projects, leave this blank so that the value defaults '
               'to {name}',
    skip_setup='if this flag is specified, we will not create a virtual '
               'environment and install base requirements as part of '
               'kicking off the new directory',
))
def template(ctx, name, path='.', source_dir=None, skip_setup=False):
    """
    creates a template for a pypi project using our standard defaults
    """
    from ..base.projects import new_project
    boo = not skip_setup
    templates = [
        '.bumpversion.cfg',
        '.coveragerc',
        '.gitignore',
        'dev.txt',
        'Makefile',
        'MANIFEST.in',
        'pytest.ini',
        'README.md',
        'requirements.txt',
        'setup.py',
        'conf/convocations.yml'
        'sesame_meow_cat/__init__.py',
        'sesame_meow_cat/version.txt',
        'tasks/__init__.py'
        'test/__init__.py',
        'test/conftest.py',
    ]
    new_project(
        ctx, name, path, source_dir, boo,
        templates, package='convocations.pypi')


ns = Collection(template)
