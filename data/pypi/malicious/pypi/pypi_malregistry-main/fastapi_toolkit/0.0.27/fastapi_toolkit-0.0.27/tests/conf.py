from pydantic import AnyUrl

from fastapi_toolkit.conf.global_settings import GlobalSettings


class Settings(GlobalSettings):
    project: str = 'test_project'
    # TODO: fix database settings
    database_dsn: AnyUrl = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/test_fastapi_toolkit'  # noqa
