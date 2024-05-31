from collections import namedtuple

from fastapi_toolkit.filters.func import FILTERS_LIST

filter_type = namedtuple(
    'FilterType',
    ('field', 'operators', 'cast_type', 'query_param_type')
)


def _noop(x):
    return x


MAPPING = {
    func.__name__.strip('_'): func
    for func in FILTERS_LIST
}


def filter_(
        field,
        operators: tuple,
        cast_type=None,
        query_param_type=None,
):
    return filter_type(
        field=field,
        operators={func.__name__.strip('_'): func for func in operators},
        cast_type=cast_type or _noop,
        query_param_type=query_param_type,
    )
