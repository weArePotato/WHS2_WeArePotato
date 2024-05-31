from raft.tasks import task
from ..base.projects import new_project as base_new_project


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
    starts a new project for a docker container using the slytherin standard template

    this will include the following:
      * setup and build via Makefile / make or convocations
      * Dockerfile
      * publishing to docker.io as default
    """
    jinja_templates = [
        'README.md',
        'tasks/build.py',
        'templates/buildspec.yml',
    ]
    base_new_project(
        ctx, name, dir_name, setup=setup,
        jinja_templates=jinja_templates, package=__package__)
