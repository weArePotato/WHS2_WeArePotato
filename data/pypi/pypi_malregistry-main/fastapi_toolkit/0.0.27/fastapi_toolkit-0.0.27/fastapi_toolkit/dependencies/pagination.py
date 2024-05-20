import abc

from fastapi import Query

__all__ = (
    'BasePagination',
    'PageNumberPagination',
    'LimitOffsetPagination',
)

from fastapi_toolkit.schemas.pagination import (
    LimitOffsetPagination as LimitOffsetPaginationSchema,
    PageNumberPagination as PageNumberPaginationSchema,
)


class BasePagination:
    @property
    @abc.abstractmethod
    def database_params(self) -> dict:
        ...

    @property
    @abc.abstractmethod
    def params(self) -> dict:
        ...

    @property
    @abc.abstractmethod
    def schema(self):
        ...

    @staticmethod
    def _get_param(value: int, default: int = None):
        return value if value > 0 else default


class PageNumberPagination(BasePagination):
    def __init__(
            self,
            page: int = Query(1),
            page_size: int = Query(10)
    ):
        self.page = page
        self.page_size = page_size

    @property
    def database_params(self) -> dict:
        return {
            'offset': self._get_param((self.page - 1) * self.page_size, 0),
            'limit': self._get_param(self.page_size)
        }

    @property
    def params(self) -> dict:
        return {
            'page': self.page,
            'page_size': self.page_size
        }

    @property
    def schema(self):
        return PageNumberPaginationSchema


class LimitOffsetPagination(BasePagination):
    def __init__(
            self,
            offset: int = Query(0),
            limit: int = Query(10)
    ):
        self.offset = offset
        self.limit = limit

    @property
    def database_params(self):
        return {
            'offset': self._get_param(self.offset, 0),
            'limit': self._get_param(self.limit)
        }

    @property
    def params(self):
        return self.database_params

    @property
    def schema(self):
        return LimitOffsetPaginationSchema
