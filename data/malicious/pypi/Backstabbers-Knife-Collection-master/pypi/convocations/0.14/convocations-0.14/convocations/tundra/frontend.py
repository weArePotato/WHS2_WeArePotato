"""
front-end client tasks for local development in tundra
"""
from raft import task


@task(default=True)
def client(ctx):
    """ runs the client watch """
    ctx.run('rm -rf client/static/*')
    ctx.run('. nenv/bin/activate && cd client && npm run client')


@task
def build(ctx):
    """ builds the client """
    ctx.run('rm -rf client/static/*')
    ctx.run('make setup_client')
    ctx.run('. nenv/bin/activate && cd client && npm run build')


@task
def build_docker(ctx):
    """ builds the client using a docker-compose cmd """
    ctx.run('rm -rf client/static/*')
    ctx.run('docker-compose -f client/docker-compose.yml up')
