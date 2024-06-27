from raft import Collection
from .validator import validate_chain


cert_tasks = Collection(
    validate_chain,
)
