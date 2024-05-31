from raft import Program
from raft import Collection
from ..version import version
from . import template

ns = Collection(template)
program = Program(version=version, namespace=ns)
