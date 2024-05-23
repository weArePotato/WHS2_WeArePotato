import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.command import Command

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('AgentActions')


class CommandsFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'acknowledgedAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'agentId': ['eq'],
        'agentIds': ['eq'],
        'agentUuid': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'names': ['eq'],
        'sentAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'status': ['eq'],
        'statuses': ['eq'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'uuids': ['eq'],
    }

    def __init__(self):
        super(CommandsFilter, self).__init__()


class Commands(object):
    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **site_args):
        query_params = CommandsFilter.get_query_params(query_filter, site_args)
        ret = list()
        res = self.client.get(endpoint=GET_COMMANDS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get commands, response_code: {}".format(res.status_code))
            raise_from_response(res)
        commands = res.data
        for command in commands:
            ret.append(Command(**command))
        res.data = ret
        return res
