from raft.tasks import task
from raft.collection import Collection
from . import build as build_tasks


@task
def setup(ctx):
    """
    installs dependencies in the codebuild environment
    this installation is dead simple because we don't have
    to worry about python virtual environments
    """
    pip = 'pip install -q --user'
    ctx.run(f'{pip} -U wheel')
    ctx.run(f'{pip} -U setuptools raft pip')
    ctx.run(f'{pip} -r requirements.txt')


codebuild_collection = Collection('codebuild')
codebuild_collection.add_task(setup)
global_collection = Collection()
global_collection.add_tasks(build_tasks)
