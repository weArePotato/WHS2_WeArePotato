import os
import shutil
import sys
from importlib.resources import files


def new_project(ctx, name, dir_name='.', source_dir=None,
                setup=False, jinja_templates=None, package=None):
    """
    all templates and filenames will have the text `sesame_meow_cat` replaced
    with the user-provided source_dir
    """
    from jinja2.environment import Environment
    from jinja2.loaders import PackageLoader
    current = os.getcwd()
    os.chdir(dir_name)
    os.makedirs(name, exist_ok=True)
    os.chdir(name)
    source_dir = source_dir or name
    meow_cat = 'sesame_meow_cat'
    env = Environment(loader=PackageLoader(package))
    templates = files(package).joinpath('templates')
    templates_dir = templates.as_posix()
    jinja_templates = [ x.replace(meow_cat, source_dir) for x in jinja_templates ]
    for x in templates.glob('**/*'):
        filename = x.relative_to(templates_dir).as_posix()
        print(filename)
        if '__pycache__' in filename or filename.endswith('.pyc'):
            continue
        template_name = filename
        filename = filename.replace(meow_cat, source_dir)
        if x.is_dir():
            print(f'creating dir {filename}')
            os.makedirs(filename, exist_ok=True)
            continue

        if template_name in jinja_templates:
            print(f'templating {filename}')
            t = env.get_template(template_name)
            contents = t.render(name=name)
            with open(filename, 'w') as f:
                f.write(contents)
        else:
            print(f'copying {x.as_posix()} => {filename}')
            shutil.copy2(x.as_posix(), filename)
    if setup and sys.platform == 'linux':
        ctx.run('make setup')
    os.chdir(current)
