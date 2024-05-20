from raft import Collection
from .save_config import save_config
from .save_config import export_config
from .upgrade import upgrade
from .weird import remove_hip_profiles
from .certificates import install_cert


panos = Collection(
    save_config,
    export_config,
    upgrade,
    remove_hip_profiles,
    install_cert,
)
