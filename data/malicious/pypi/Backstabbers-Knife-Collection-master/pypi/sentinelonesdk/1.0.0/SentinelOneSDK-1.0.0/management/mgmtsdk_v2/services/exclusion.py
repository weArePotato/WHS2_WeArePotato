import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.exclusion import Exclusion

from management.mgmtsdk_v2.exceptions import raise_from_response, SentinelBaseException

logger = logging.getLogger('Exclusion')


class ExclusionQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'osTypes': ['eq'],
        'types': ['eq'],
        'osType': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
        'type': ['eq'],
        'unified': ['eq'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte'],
        'userIds': ['eq'],
        'includeChildren': ['eq'],
        'includeParents': ['eq'],
        'value': ['eq'],
    }

    def __init__(self):
        super(ExclusionQueryFilter, self).__init__()


class Exclusions(object):

    def __init__(self, client):
        self.client = client

    def get_black(self, query_filter=None, **excl_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ExclusionQueryFilter
        :param excl_args: Key value with query filters
        :type excl_args: **dict
        :return: Black Exclusions answering the query
        :rtype: ManagementResponse
        """
        query_params = ExclusionQueryFilter.get_query_params(query_filter, excl_args)
        ret = list()
        res = self.client.get(endpoint=RESTRICTIONS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get black, response_code: {}".format(res.json))
            raise_from_response(res)
        blacks = res.data
        for black in blacks:
            ret.append(Exclusion(**black))
            res.data = ret
        return res

    def create_black(self, exclusion, query_filter=None, **excl_args):
        """
        :param exclusion: black exclusion to create
        :type exclusion: Exclusion
        :param query_filter: Query filter object
        :type query_filter: ExclusionQueryFilter
        :param excl_args: Key value with query filters
        :type excl_args: **dict
        :return: created black exclusion
        :rtype: ManagementResponse
        """
        ret = list()
        query_params = ExclusionQueryFilter.get_query_params(query_filter, excl_args)
        res = self.client.post(endpoint=RESTRICTIONS, data=exclusion.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        blacks = res.data
        for black in blacks:
            ret.append(Exclusion(**black))
            res.data = ret
        return res

    def update_black(self, exclusion_id, excl_type, tenant=False, accountIds=None, siteIds=None, groupIds=None, **kwargs):
        """
        :param accountIds:
        :param excl_type:
        :param tenant:
        :param siteIds:
        :param groupIds:
        :param exclusion_id:
        :type exclusion_id: string
        :return: updated black exclusion
        :rtype: ManagementResponse
        """
        ret = list()
        if siteIds:
            exclusions = self.get_black(ids=exclusion_id, type=excl_type, siteIds=siteIds).data
        elif accountIds:
            exclusions = self.get_black(ids=exclusion_id, type=excl_type, accountIds=accountIds).data
        elif groupIds:
            exclusions = self.get_black(ids=exclusion_id, type=excl_type, groupIds=groupIds).data
        elif tenant is True:
            exclusions = self.get_black(ids=exclusion_id, type=excl_type, tenant=True).data
        else:
            raise SentinelBaseException('Scope info not provided')
        if not exclusions:
            raise SentinelBaseException("Exclusion not found according to the user's permissions")
        exclusion = exclusions[0]
        for key, val in kwargs.items():
            exclusion.__setattr__(key, val)
        res = self.client.put(endpoint=RESTRICTIONS, data=exclusion.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update black, response_code: {}".format(res.json))
            raise_from_response(res)
        blacks = res.data
        for black in blacks:
            ret.append(Exclusion(**black))
            res.data = ret
        return res

    def delete_black(self, type, ids):
        """
        :param type: black exclusion type
        :type type: string
        :param ids: black exclusion ids to delete
        :type ids: list
        :return: number of affected exclusions
        :rtype: ManagementResponse
        """
        data = {'type': type, 'ids': ','.join(ids)}
        res = self.client.delete(endpoint=RESTRICTIONS, data=data)
        if res.status_code != 200:
            logger.warning("Failed to delete black, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def get_white(self, query_filter=None, **excl_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ExclusionQueryFilter
        :param excl_args: Key value with query filters
        :type excl_args: **dict
        :return: White Exclusions answering the query
        :rtype: ManagementResponse
        """
        ret = list()
        query_params = ExclusionQueryFilter.get_query_params(query_filter, excl_args)
        res = self.client.get(endpoint=EXCLUSIONS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get white, response_code: {}".format(res.json))
            raise_from_response(res)
        whites = res.data
        for white in whites:
            ret.append(Exclusion(**white))
        res.data = ret
        return res

    def create_white(self, exclusion, query_filter=None, **excl_args):
        """
        :param exclusion: white exclusion to create
        :type exclusion: Exclusion
        :param query_filter: Query filter object
        :type query_filter: ExclusionQueryFilter
        :param excl_args: Key value with query filters
        :type excl_args: **dict
        :return: created white exclusion
        :rtype: ManagementResponse
        """
        ret = list()
        query_params = ExclusionQueryFilter.get_query_params(query_filter, excl_args)
        res = self.client.post(endpoint=EXCLUSIONS, data=exclusion.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create white, response_code: {}".format(res.json))
            raise_from_response(res)
        whites = res.data
        for white in whites:
            ret.append(Exclusion(**white))
        res.data = ret
        return res

    def update_white(self, exclusion_id, excl_type, tenant=False, accountIds=None, siteIds=None, groupIds=None, **kwargs):
        """
        :param accountIds:
        :param excl_type:
        :param tenant:
        :param siteIds:
        :param groupIds:
        :param exclusion_id:
        :type exclusion_id: string
        :return: updated white exclusion
        :rtype: ManagementResponse
        """
        ret = list()
        if siteIds:
            exclusions = self.get_white(ids=exclusion_id, type=excl_type, siteIds=siteIds).data
        elif accountIds:
            exclusions = self.get_white(ids=exclusion_id, type=excl_type, accountIds=accountIds).data
        elif groupIds:
            exclusions = self.get_white(ids=exclusion_id, type=excl_type, groupIds=groupIds).data
        elif tenant is True:
            exclusions = self.get_white(ids=exclusion_id, type=excl_type, tenant=True).data
        else:
            raise SentinelBaseException('Scope info not provided')
        if not exclusions:
            raise SentinelBaseException("Exclusion not found according to the user's permissions")
        exclusion = exclusions[0]
        for key, val in kwargs.items():
            exclusion.__setattr__(key, val)
        res = self.client.put(endpoint=EXCLUSIONS, data=exclusion.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update white, response_code: {}".format(res.json))
            raise_from_response(res)
        whites = res.data
        for white in whites:
            ret.append(Exclusion(**white))
        res.data = ret
        return res

    def delete_white(self, type, ids):
        """
        :param type: white exclusion type
        :type type: string
        :param ids: white exclusion ids to delete
        :type ids: list
        :return: number of affected exclusions
        :rtype: ManagementResponse
        """
        data = {'type': type, 'ids': ','.join(ids)}
        res = self.client.delete(endpoint=EXCLUSIONS, data=data)
        if res.status_code != 200:
            logger.warning("Failed to delete white, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def validate_exclusions(self, exclusion_type, os_type_enum, value):
        """
        Validate exclusions
        """
        body = {
            "exclusionType": exclusion_type,
            "osType": os_type_enum,
            "value": value
        }
        # query_params = ExclusionQueryFilter.get_query_params(query_filter, excl_args)
        res = self.client.post(endpoint=EXCLUSIONS_VALIDATION, data=body, query_filter=None)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def validate_restrictions(self, os_type, value):
        """
        validate black list
        """
        body = {
            "osType": os_type,
            "value": value
        }
        res = self.client.post(endpoint=RESTRICTIONS_VALIDATION, data=body, query_filter=None)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_black_hash_filter(self, text, siteIds=None, groupIds=None):
        """
        validate black hash filter
        """
        ret = list()
        link =f'{text}&type=black_hash&unified=false'
        if  siteIds != None:
            link += f'&siteIds={siteIds}'
        elif  groupIds != None:
            link += f'&groupIds={groupIds}'
        res = self.client.get(f'private/restrictions/filters-autocomplete?key=value__contains&text={link}')
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_exclusion_filter(self, text, type, siteIds=None, groupIds=None):
        """
        validate exclusions filter
        """
        ret = list()
        link =f'{text}&type={type}&unified=false'
        if  siteIds != None:
            link += f'&siteIds={siteIds}'
        elif  groupIds != None:
            link += f'&groupIds={groupIds}'
        res = self.client.get(f'private/exclusions/filters-autocomplete?key=value__contains&text={link}')
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def exclusion_filter_count(self, type, siteIds=None, file_type=None):
        """
        validate exclusions counter filter
        """
        ret = list()
        link = f'private/exclusions/filters-count?type={type}'
        if siteIds != None:
            link += f'&siteIds={siteIds}'
        if file_type != None:
            link += f'&file_type={file_type}'
        res = self.client.get(link)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def export_restrictions(self, query_filter=None, **kwargs):
        """
        export black list to CSV file
        """
        query_params = ExclusionQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=EXPORT_RESTRICTIONS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def export_exclusions(self, query_filter=None, **kwargs):
        """
        export exclusions to CSV file
        """
        query_params = ExclusionQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=EXPORT_EXCLUSIONS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create black, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
