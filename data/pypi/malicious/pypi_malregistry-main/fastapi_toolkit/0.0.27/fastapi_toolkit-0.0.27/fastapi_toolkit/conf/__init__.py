import importlib
import os

from pydantic.tools import lru_cache

from fastapi_toolkit.conf.global_settings import GlobalSettings

__all__ = (
    'settings',
)

from fastapi_toolkit.logging import set_up_logging


class Settings:
    ENVIRONMENT_VARIABLE = 'SETTINGS_MODULE'

    @classmethod
    @lru_cache
    def load(cls, *args, **kwargs):
        settings_module = os.environ.get(cls.ENVIRONMENT_VARIABLE)
        if settings_module:
            module = importlib.import_module(settings_module)
            application_settings_class = getattr(module, 'Settings')
            _settings = application_settings_class(*args, **kwargs)
        else:
            _settings = GlobalSettings(*args, **kwargs)
        set_up_logging(_settings)
        return _settings


settings = Settings.load()
