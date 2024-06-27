import logging

from management.common.query_filter import QueryFilter, FullScopeFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.location import Location
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Location')


class LocationQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'name': ['contains'],
        'scopes': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(LocationQueryFilter, self).__init__()


class LocationByFiltersQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'name': ['contains'],
        'scopes': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(LocationByFiltersQueryFilter, self).__init__()


class LocationAutocompleteQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'scopes': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(LocationAutocompleteQueryFilter, self).__init__()


class Locations(object):
    """Locations service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **location_args):
        """
        Get list of ``Groups`` from the console by filters, default filter is empty

        :type query_filter: LocationQueryFilter
        :type location_args: **dict
        :return: Locations answering the query
        :rtype: ManagementResponse
        """
        query_params = LocationQueryFilter.get_query_params(query_filter, location_args)
        res = self.client.get(endpoint=LOCATIONS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get locations, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Location(**location) for location in res.data]
        return res

    def create(self, location, query_filter=None, **location_args):
        """
        :param query_filter:
        :param location: Location object to create
        :type location: Location
        :return: created location
        :rtype: ManagementResponse
        """
        query_params = FullScopeFilter.get_query_params(query_filter, location_args)
        res = self.client.post(endpoint=LOCATIONS, data=location.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create location, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Location(**res.data)
        return res

    def update(self, location_id, scope, scope_id, **kwargs):
        """
        :param location_id:
        :type location_id: string
        :param kwargs:
        :type kwargs: **dict
        :return: updated location
        :rtype ManagementResponse
        """
        params = {'ids': location_id}
        if scope == 'group':
            params['groupIds'] = scope_id
        elif scope == 'site':
            params['siteIds'] = scope_id
        elif scope == 'account':
            params['accountIds'] = scope_id

        loc = self.get(**params).data[0]
        for key, val in kwargs.items():
            loc.__setattr__(key, val)
        res = self.client.put(endpoint=UPDATE_LOCATION.format(location_id), data=loc.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update location, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Location(**res.data)
        return res

    def delete(self, location_ids):
        """
        :param location_ids:
        :type location_ids: list
        :return: number of affected locations
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=LOCATIONS, data={"ids": location_ids})
        if res.status_code != 200:
            logger.warning("Failed to delete location, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def count_by_filters(self, query_filter=None, **loc_args):
        """
        :param query_filter:
        :param loc_args:
        :return:
        """
        query_params = LocationByFiltersQueryFilter.get_query_params(query_filter, loc_args)
        res = self.client.get(endpoint=LOCATIONS_FILTER_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to count locations, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_free_text_filters(self):
        res = self.client.get(endpoint=LOCATIONS_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get free text filters for locations, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def filters_auto_complete(self, key, text, query_filter=None, **loc_args):
        query_params = LocationAutocompleteQueryFilter.get_query_params(query_filter, loc_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=LOCATIONS_FILTER_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get locations autocomplete, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
