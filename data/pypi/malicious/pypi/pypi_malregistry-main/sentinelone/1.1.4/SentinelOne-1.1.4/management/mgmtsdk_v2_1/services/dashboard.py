import logging

from management.mgmtsdk_v2_1.entities.dashboard import Dashboard

from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import GET_DASHBOARD

DASHBOARD_QUERY_ARGS = ['accountIds', 'groupIds', 'siteIds']

logger = logging.getLogger('Dashboard')


class Dashboards(object):

    def __init__(self, client):
        self.client = client

    def get(self, **dashboard_args):
        """
        :optional: list of query filters
        :return: Dashboard object
        """
        validate_params(dashboard_args)
        res = self.client.get(endpoint=GET_DASHBOARD, params=dashboard_args)
        if res.status_code != 200:
            logger.warning("Failed to get dashboards, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Dashboard(**res.data)
        return res


def validate_params(kwargs):
    for arg in list(kwargs):
        if arg not in DASHBOARD_QUERY_ARGS:
            raise ValueError("{} not in dashboard args")