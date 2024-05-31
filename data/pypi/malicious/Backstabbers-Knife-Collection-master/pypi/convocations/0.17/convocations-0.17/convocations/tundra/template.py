from raft.tasks import task
from ..base.projects import new_project as base_project


@task(help={
    'name': 'the name of the new project, a new directory '
            'called <name> will be created in <dir_name>',
    'dir_name': 'the /path/to the directory in which the new '
                'project will be created',
    'setup': 'if specified, we will try to run the setup steps '
             'after creating the directory from the project template'
})
def new_project(ctx, name, dir_name='.', setup=False):
    """
    starts a new tundra-style project using the slytherin standard template

    this will include the following:
      * setup via Makefile / make
      * tundra convocations
      * setup.py to create the tundra on raft executable
      * base deploy via ansible
      * base buildspec.yml for codebuild
      * Dockerfile
    """
    jinja_templates = [
        'README.md',
        'Makefile',
    ]
    base_project(ctx, name, dir_name, setup, jinja_templates, 'convocations.tundra')
