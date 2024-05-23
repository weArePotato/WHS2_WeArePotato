from contextlib import asynccontextmanager
from typing import Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from fastapi_toolkit.conf import settings
from fastapi_toolkit.db.base_class import BaseModel

__all__ = (
    'create_session',
    'BaseModel',
    'init_db',
    'create_engine',
)


_engine: Optional[AsyncEngine] = None
_Session: Optional[sessionmaker] = None


def create_engine() -> AsyncEngine:
    global _engine

    if not _engine:
        _engine = create_async_engine(
            settings.database_dsn,
            pool_pre_ping=True
        )

    return _engine


def init_db():
    global _Session
    create_engine()

    if not _Session:
        _Session = sessionmaker(
            # autocommit=False,
            # autoflush=False,
            bind=_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )


@asynccontextmanager
async def create_session(session=None, **kwargs):
    init_db()
    if session:
        yield session
        return

    async with _Session(**kwargs) as session:  # noqa
        yield session
