import logging

from management.mgmtsdk_v2.endpoints import GET_INSIGHT_TYPES
from management.mgmtsdk_v2.exceptions import raise_from_response

from management.mgmtsdk_v2.entities.insight_type import \
    InsightType

INSIGHT_TYPE_QUERY_ARGS = ['groupIds', 'forceUpdate', 'siteIds', 'accountIds']

logger = logging.getLogger('InsightType')


class InsightTypes(object):

    def __init__(self, client):
        self.client = client

    def get(self, **insight_type_args):
        """
        :optional: list of query filters
        :return: List of InsightType objects
        """
        validate_params(insight_type_args)
        ret = []
        res = self.client.get(endpoint=GET_INSIGHT_TYPES, params=insight_type_args)
        if res.status_code != 200:
            logger.warning("Failed to get insight_types, response_code: {}".format(res.status_code))
            raise_from_response(res)
        insight_types = res.data["insightTypes"]
        for insight_type in insight_types:
            ret.append(InsightType(**insight_type))
        res.data = ret
        return res


def validate_params(kwargs):
    for arg in list(kwargs):
        if arg not in INSIGHT_TYPE_QUERY_ARGS:  # TODO: Handle with exception
            raise ValueError("{} not in insight_type args")