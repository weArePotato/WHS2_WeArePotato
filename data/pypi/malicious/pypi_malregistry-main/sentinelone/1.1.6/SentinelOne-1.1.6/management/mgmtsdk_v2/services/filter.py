import logging

from management.common.query_filter import QueryFilter, BaseScopeFilter, HighScopeFilter, FullScopeFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.filter import Filter

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Filter')


class FilterQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'includeGlobal': ['eq'],
        'includeParents': ['eq'],
        'limit': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(FilterQueryFilter, self).__init__()


class Filters(object):

    def __init__(self, client):
        self.client = client

    def save(self, filter_to_save, query_filter=None, **filter_args):
        """
        :param filter_to_save: filter to save
        :type filter_to_save: Filter
        :param query_filter: Query filter object
        :type query_filter: QueryFilter
        :return: saved filter
        :rtype: ManagementResponse
        """
        query_params = HighScopeFilter.get_query_params(query_filter, filter_args)
        res = self.client.post(endpoint=SAVE_FILTER, data=filter_to_save.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed save filter, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Filter(**res.data)
        return res

    def get(self, query_filter=None, **filter_args):
        """
        :param query_filter: Query filter object
        :type query_filter: FilterQueryFilter
        :param filter_args: Key value with query filters
        :type filter_args: **dict
        :return: Filters answering the query
        :rtype: ManagementResponse
        """
        query_params = FilterQueryFilter.get_query_params(query_filter, filter_args)
        ret = list()
        res = self.client.get(endpoint=GET_FILTERS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get filters, response_code: {}".format(res.json))
            raise_from_response(res)
        filters = res.data
        for current in filters:
            ret.append(Filter(**current))
        res.data = ret
        return res

    def update(self, filter):
        """
        :param filter: filter to update
        :type filter: Filter
        :return: updated filter
        :rtype: ManagementResponse
        """
        filter.siteId = None
        res = self.client.put(endpoint=UPDATE_FILTER.format(filter.id), data=filter.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update filter, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Filter(**res.data)
        return res

    def delete(self, filter_id):
        """
        :param filter_id:
        :type filter_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_FILTER.format(filter_id))
        if res.status_code != 200:
            logger.warning("Failed to delete filter, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_dv(self, query_filter=None, **filter_args):
        """
        :param query_filter: Query filter object
        :type query_filter: FilterQueryFilter
        :param filter_args: Key value with query filters
        :type filter_args: **dict
        :return: Filters answering the query
        :rtype: ManagementResponse
        """
        query_params = FilterQueryFilter.get_query_params(query_filter, filter_args)
        ret = list()
        res = self.client.get(endpoint=GET_DV_FILTER, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get DV filter, response_code: {}".format(res.json))
            raise_from_response(res)
        filters = res.data
        for current in filters:
            ret.append(Filter(**current))
        res.data = ret
        return res

    def save_dv(self, filter_to_save, scope_filter=None, **scope_args):
        """
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :param filter_to_save: filter to save
        :type filter_to_save: Filter
        :return: saved filter
        :rtype: ManagementResponse
        """
        query_params = FullScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.post(endpoint=SAVE_DV_FILTER, data=filter_to_save.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to save DV filter, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def update_dv(self, filter_to_update, scope_filter=None, **scope_args):
        """
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :param filter_to_update: filter to update
        :type filter_to_update: Filter
        :return: updated filter
        :rtype: ManagementResponse
        """
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=UPDATE_DV_FILTER.format(filter_to_update.id),
                              data=filter_to_update.to_json(),
                              query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to upodate DV filter, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Filter(**res.data)
        return res

    def delete_dv(self, filter_id):
        """
        :param filter_id:
        :type filter_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_DV_FILTER.format(filter_id))
        if res.status_code != 200:
            logger.warning("Failed to delete DV filter, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def filters_with_metadata(self, query_filter=None, **filter_args):
        """
        :param query_filter: Query filter object
        :type query_filter: FilterQueryFilter
        :param filter_args: Key value with query filters
        :type filter_args: **dict
        :return: Filters answering the query
        :rtype: ManagementResponse
        """
        query_params = FilterQueryFilter.get_query_params(query_filter, filter_args)
        ret = list()
        res = self.client.get(endpoint=FILTERS_WITH_METADATA, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get filters with metadata, response_code: {}".format(res.json))
            raise_from_response(res)
        filters = res.data
        for current in filters:
            ret.append(Filter(**current))
        res.data = ret
        return res
