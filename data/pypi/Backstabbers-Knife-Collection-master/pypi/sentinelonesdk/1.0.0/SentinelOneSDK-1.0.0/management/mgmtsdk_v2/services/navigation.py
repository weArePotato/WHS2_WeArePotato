import logging

from management.mgmtsdk_v2.entities.navigation import NavigationObj
from management.mgmtsdk_v2.exceptions import raise_from_response

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *

logger = logging.getLogger('Location')


class TopLevelEndpointsQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'scope': ['eq'],
        'scopeId': ['eq'],
    }

    def __init__(self):
        super(TopLevelEndpointsQueryFilter, self).__init__()


class GetScopesQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'groupIds': ['eq'],
        'parentId': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(GetScopesQueryFilter, self).__init__()


class SearchForScopeQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'query': ['eq'],
        'scope': ['eq'],
        'scopeId': ['eq'],
        'searchByType': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(SearchForScopeQueryFilter, self).__init__()


class SingleAccountQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'groupIds': ['eq'],
        'parentId': ['eq'],
        'scopeId': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(SingleAccountQueryFilter, self).__init__()


class SingleScopeQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'scopeId': ['eq'],
    }

    def __init__(self):
        super(SingleScopeQueryFilter, self).__init__()


class Navigation(object):
    """Navigation service"""

    def __init__(self, client):
        self.client = client

    def get_top_level_endpoints(self, query_filter=None, **nav_args):
        query_params = TopLevelEndpointsQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_TOP_LEVEL_ENDPOINTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get top level endpoints, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = NavigationObj(**res.data)
        return res

    def get_accounts(self, query_filter=None, **nav_args):
        query_params = GetScopesQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_ACCOUNTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get accounts for navigation response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [NavigationObj(**obj) for obj in res.data]
        return res

    def get_groups(self, query_filter=None, **nav_args):
        query_params = GetScopesQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_GROUPS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get groups for navigation, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [NavigationObj(**obj) for obj in res.data]
        return res

    def search_for_scope_objects(self, query_filter=None, **nav_args):
        query_params = SearchForScopeQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_SEARCH_FOR_SCOPE_OBJECTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to search for scope objects, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [NavigationObj(**obj) for obj in res.data]
        return res

    def get_total_endpoints(self, scope, ids):
        params = {'scope': scope, 'ids': ids}
        res = self.client.get(endpoint=NAVIGATION_GET_TOTAL_ENDPOINTS, params=params)
        if res.status_code != 200:
            logger.warning("Failed to get total endpoints, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [NavigationObj(**obj) for obj in res.data]
        return res

    def get_sites(self, query_filter=None, **nav_args):
        query_params = GetScopesQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_SITES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get sites for navigation, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [NavigationObj(**obj) for obj in res.data]
        return res

    def get_single_account(self, scope_id, query_filter=None, **nav_args):
        query_params = SingleAccountQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_SINGLE_ACCOUNT.format(scope_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get single account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = NavigationObj(**res.data)
        return res

    def get_single_group(self, scope_id, query_filter=None, **nav_args):
        query_params = SingleScopeQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_SINGLE_GROUP.format(scope_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get single group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = NavigationObj(**res.data)
        return res

    def get_single_site(self, scope_id, query_filter=None, **nav_args):
        query_params = SingleScopeQueryFilter.get_query_params(query_filter, nav_args)
        res = self.client.get(endpoint=NAVIGATION_GET_SINGLE_SITE.format(scope_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get single site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = NavigationObj(**res.data)
        return res
