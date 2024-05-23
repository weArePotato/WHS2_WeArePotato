from raft.collection import Collection
from .layers import layers
from .objects import group
from .services import services, service_group
from .services import service
from .versions import api_version


ns = Collection(
    layers,
    services,
    api_version,
    service,
    service_group,
    group,
)
