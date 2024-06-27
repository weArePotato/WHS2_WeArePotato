from raft import Collection
from ..aws.codebuild import build
from ..aws.open_id import sso_login
from . import deploy
from . import codebuild


tundra_collection = Collection()
tundra_collection.add_tasks(build)
tundra_collection.add_task(sso_login)
tundra_collection.add_collection(Collection.from_module(deploy), 'deploy')
tundra_collection.add_collection(Collection.from_module(codebuild), 'codebuild')
