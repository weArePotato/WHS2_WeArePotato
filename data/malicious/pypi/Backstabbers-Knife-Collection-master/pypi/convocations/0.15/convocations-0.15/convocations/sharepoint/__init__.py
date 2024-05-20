from raft.collection import Collection
from raft.program import Program
from .files import upload_files
from .permissions import grant_access
from .permissions import check_access
from ..version import version


ns = Collection(grant_access, check_access, upload_files)
program = Program(version=version, namespace=ns)
