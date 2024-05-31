import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.activity import Activity, ActivityType

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Activity')


class ActivitiesFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'agentIds': ['eq'],
        'activityTypes': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['eq', 'gt', 'gte', 'lt', 'lte', 'between'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'includeHidden': ['eq'],
        'limit': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'skipCount': ['eq'],
        'threatIds': ['eq'],
        'userEmails': ['eq'],
        'userIds': ['eq'],
        'rowsLimit': ['eq'],
        'createdAt__lte': ['eq'],
        'createdAt__lt': ['eq'],
        'createdAt__gte': ['eq'],
        'createdAt__gt': ['eq'],
        'alertIds': ['eq'],
        'createdAt__between': ['eq'],
        'ruleIds': ['eq'],
    }

    def __init__(self):
        super(ActivitiesFilter, self).__init__()


class Activities(object):

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **activity_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ActivitiesFilter
        :param activity_args: Key value with query filters
        :type activity_args: **dict
        :return: Activities answer the query
        :rtype: ManagementResponse
        """
        query_params = ActivitiesFilter.get_query_params(query_filter, activity_args)
        ret = list()
        res = self.client.get(endpoint=ACTIVITIES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get activities, response_code: {}".format(res.json))
            raise_from_response(res)
        activities = res.data
        for activity in activities:
            ret.append(Activity(**activity))
        res.data = ret
        return res

    def export(self, query_filter=None, **activity_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ActivitiesFilter
        :param activity_args: Key value with query filters
        :type activity_args: **dict
        :return: export activity
        :rtype: ManagementResponse
        """
        query_params = ActivitiesFilter.get_query_params(query_filter, activity_args)
        res = self.client.get(endpoint=EXPORT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get activities, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_types(self):
        """
        :return: activities types
        :rtype: ManagementResponse
        """
        ret = list()
        res = self.client.get(endpoint=ACTIVITY_TYPES)
        if res.status_code != 200:
            logger.warning("Failed to get activities, response_code: {}".format(res.json))
            raise_from_response(res)
        activity_types = res.data
        for activity_type in activity_types:
            ret.append(ActivityType(**activity_type))
        res.data = ret
        return res
