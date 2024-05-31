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
        'sesame_meow_cat/__init__.py',
        'sesame_meow_cat/version.txt',
        'test/__init__.py',
        'test/conftest.py',
    ]
    new_project(
        ctx, name, path, source_dir, boo,
        templates, package='convocations.pypi')
    # from jinja2.environment import Environment
    # from jinja2.loaders import PackageLoader
    # print(f'checking for existence of {path}')
    # if not os.path.exists(path):
    #     os.makedirs(path, exist_ok=True)
    # print(f'cding to {path}')
    # os.chdir(path)
    # os.makedirs(name, exist_ok=True)
    # source_dir = source_dir or name
    # root_dir = name
    # base_dir = os.path.join(root_dir, source_dir)
    # test_dir = os.path.join(root_dir, 'test')
    # print(f'base_dir: [{base_dir}]')
    # print(f'test_dir: [{test_dir}]')
    # os.makedirs(base_dir, exist_ok=True)
    # os.makedirs(test_dir, exist_ok=True)
    # loader = PackageLoader('convocations.pypi', 'templates')
    # env = Environment(loader=loader)
    # context = dict(name=name)
    # files = [
    #     ('.bumpversion.cfg.j2', root_dir, '.bumpversion.cfg'),
    #     ('.coveragerc.j2', root_dir, '.coveragerc'),
    #     ('.gitignore.j2', root_dir, '.gitignore'),
    #     ('empty_init.py.j2', base_dir, '__init__.py'),
    #     ('version.txt.j2', base_dir, 'version.txt'),
    #     ('makefile.j2', root_dir, 'Makefile'),
    #     ('dev.txt.j2', root_dir, 'dev.txt'),
    #     ('requirements.txt.j2', root_dir, 'requirements.txt'),
    #     ('MANIFEST.in.j2', root_dir, 'MANIFEST.in'),
    #     ('pytest.ini.j2', root_dir, 'pytest.ini'),
    #     ('conftest.py.j2', root_dir, 'test', 'conftest.py'),
    #     ('empty_init.py.j2', root_dir, 'test', '__init__.py'),
    #     ('README.md.j2', root_dir, 'README.md'),
    #     ('setup.py.j2', root_dir, 'setup.py'),
    # ]
    # for source, *paths in files:
    #     filename = os.path.join(*paths)
    #     if not os.path.exists(filename):
    #         print(f'rendering {source} => {filename}')
    #         render(env, source, filename, context)
    # with ctx.cd(root_dir):
    #     ctx.run('make setup')


ns = Collection(template)
