import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.entities.tag import Tag

logger = logging.getLogger('Tags')


class TagQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'disablePagination': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'kind': ['eq'],
        'limit': ['eq'],
        'name': ['contains'],
        'onlyParents': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tagScope': ['eq'],
        'tenant': ['eq'],
        'type': ['eq'],
    }

    def __init__(self):
        super(TagQueryFilter, self).__init__()


class Tags(object):
    """Tags service"""

    def __init__(self, client):
        self.client = client
        super(Tags, self).__init__()

    def get(self, tag_type, query_filter=None, **tag_args):
        """
        :param tag_type:
        :param query_filter: Query filter object
        :type query_filter: TagQueryFilter
        :param tag_args: Key value with query filters
        :type tag_args: **dict
        :return: Tags answering the query
        :rtype: ManagementResponse
        """
        query_params = TagQueryFilter.get_query_params(query_filter, tag_args)
        query_params['type'] = tag_type
        res = self.client.get(endpoint=TAGS, params=query_params)
        logger.info('payload of get_tags is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to get tags, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = [Tag(**tag) for tag in res.data]
        return res

    def create(self, tag, **scope_filter):
        """
        :param tag: Tag object
        :type tag: Tag
        :return: created Tag object
        :rtype: ManagementResponse
        """
        data = tag.to_json()
        logging.info('Creating Tag with filter={}, with data="{}"'.format(scope_filter, data))
        res = self.client.post(endpoint=TAGS, data=data, query_filter=scope_filter)
        logger.info('payload of create tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to create tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Tag(**res.data)
        return res

    def update(self, tag_id, **kwargs):
        """
        :param tag_id:
        :type tag_id: string
        :param kwargs:
        :type kwargs: **dict
        :return: updated Tag
        :rtype ManagementResponse
        """
        logging.info('Updating Tag with id={}, with data="{}"'.format(tag_id, kwargs))
        res = self.client.put(endpoint=SPECIFIC_TAG.format(tag_id), data=kwargs)
        logger.info('payload of update tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to update tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Tag(**res.data)
        return res

    def delete(self, tag_type, query_filter=None, **tag_args):
        """
        :param tag_type:
        :param query_filter: Query filter object
        :type query_filter: TagQueryFilter
        :param tag_args: Key value with query filters
        :type tag_args: **dict
        :return: Tags answering the query
        :rtype: ManagementResponse
        """
        query_params = TagQueryFilter.get_query_params(query_filter, tag_args)
        query_params['type'] = tag_type
        res = self.client.delete(endpoint=TAGS, data={}, payload={'filter': query_params})
        logger.info('payload of delete_tags is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to delete tags, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def delete_by_id(self, tag_id):
        """
        :param tag_id:
        :type tag_id: string
        :return: Tag with provided id
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=SPECIFIC_TAG.format(tag_id))
        logger.info('payload of delete_tag_by_id is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to delete tag by id, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res
