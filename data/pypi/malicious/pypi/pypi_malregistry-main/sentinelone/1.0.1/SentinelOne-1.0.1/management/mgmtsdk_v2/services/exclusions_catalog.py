import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.exclusions_catalog import ApplicationCatalog

from management.mgmtsdk_v2.exceptions import raise_from_response, SentinelBaseException

logger = logging.getLogger('ExclusionsCatalog')


class ExclusionsCatalogQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'tenant': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],

        'applicationName': ['eq'],
        'query': ['eq'],
        'types': ['eq'],
        'osTypes': ['eq'],
        'inAppInventory': ['eq'],
        'exclusionStatuses': ['eq'],

        'limit': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],

    }

    def __init__(self):
        super(ExclusionsCatalogQueryFilter, self).__init__()


class ExclusionsCatalog(object):

    def __init__(self, client):
        self.client = client

    def get_catalog(self, query_filter=None, **excl_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ExclusionsCatalogQueryFilter
        :return: Exclusions answering the query
        :rtype: ManagementResponse
        """

        query_params = ExclusionsCatalogQueryFilter.get_query_params(query_filter, excl_args)
        ret = list()
        res = self.client.get(endpoint=EXCLUSIONS_CATALOG, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get exclusions catalog, response_code: {}".format(res.json))
            raise_from_response(res)
        applications_catalog = res.data
        for app_object in applications_catalog:
            ret.append(ApplicationCatalog(**app_object))
            res.data = ret
        return res

    def add_exclusions_from_catalog(self, exclusion_ids=[], application_ids=[], add_all=False, query_filter=None, **excl_args):
        """
        :param exclusion_ids: exclusion ids from catalog
        :type exclusion_ids: List
        :param application_ids: application ids from catalog
        :type application_ids: List
        :param add_all: indicator to add all exclusions in the catalog
        :type add_all: Boolean
        :param query_filter: Query filter object
        :type query_filter: ExclusionCatalogQueryFilter
        :param excl_args: Key value with query filters
        :type excl_args: **dict
        :return: num of exclusions that were added
        :rtype: ManagementResponse
        """
        query_params = ExclusionsCatalogQueryFilter.get_query_params(query_filter, excl_args)
        data = {'exclusionIds': exclusion_ids,
                'applicationIds': application_ids,
                'addAll': add_all}
        res = self.client.post(endpoint=EXCLUSIONS_CATALOG, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to add exclusions from catalog, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res
