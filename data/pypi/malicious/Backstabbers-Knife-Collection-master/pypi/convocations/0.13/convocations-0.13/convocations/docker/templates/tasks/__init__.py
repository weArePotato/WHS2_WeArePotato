from raft import Collection
from .build import build, bump_version, tag, publish


ns = Collection(build, bump_version, tag, publish)
