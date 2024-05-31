from raft.collection import Collection
from .setup import setup, global_python
from .pytest import test, test_with_aws


python_collection = Collection(
    global_python,
    setup,
    test,
)
