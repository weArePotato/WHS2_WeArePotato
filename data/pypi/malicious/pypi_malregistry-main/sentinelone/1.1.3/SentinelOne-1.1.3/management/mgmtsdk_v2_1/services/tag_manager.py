import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.entities.tag_manager import TagManager as TagManagerEntity

logger = logging.getLogger('Tags')


class TagManagerQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'includeParents': ['eq'],
        'includeChildren': ['eq'],
        'tagIds': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'operation': ['eq'],
        'tenant': ['eq'],
        'type': ['eq'],
    }

    def __init__(self):
        super(TagManagerQueryFilter, self).__init__()


class TagManager(object):
    """Tags service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **filter_args):
        """
        :param tag_type:
        :param query_filter: Query filter object
        :type query_filter: TagQueryFilter
        :param tag_args: Key value with query filters
        :type tag_args: **dict
        :return: Tags answering the query
        :rtype: ManagementResponse
        """
        query_params = TagManagerQueryFilter.get_query_params(query_filter, filter_args)
        res = self.client.get(endpoint=TAG_MANAGER_GET_TAGS, params=query_params)
        logger.info('payload of get_tags is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to get tags, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = [TagManagerEntity(**tag) for tag in res.data]
        return res

    def create(self, tag, **scope_filter):
        """
        :param tag: Tag object
        :type tag: Tag
        :return: created Tag object
        :rtype: ManagementResponse
        """
        logging.info('Creating Tag with filter={}, with data="{}"'.format(scope_filter, tag))
        res = self.client.post(endpoint=TAG_MANAGER_CREATE_TAG, data=tag, query_filter=scope_filter)
        logger.info('payload of create tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to create tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = TagManagerEntity(**res.data)
        return res

    def edit_tag(self, tag_id, **kwargs):
        """
        :param tag_id:
        :type tag_id: string
        :param kwargs:
        :type kwargs: **dict
        :return: updated Tag
        :rtype ManagementResponse
        """
        logging.info('Updating Tag with id={}, with data="{}"'.format(tag_id, kwargs))
        res = self.client.put(endpoint=TAG_MANAGER_EDIT_TAG.format(tag_id), data=kwargs)
        logger.info('payload of update tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to update tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = TagManagerEntity(**res.data)
        return res

    def delete_tag(self, query_filter=None, **filter_args):
        """
        :param tag_type:
        :param query_filter: Query filter object
        :type query_filter: TagQueryFilter
        :param tag_args: Key value with query filters
        :type tag_args: **dict
        :return: Tags answering the query
        :rtype: ManagementResponse
        """
        query_params = TagManagerQueryFilter.get_query_params(query_filter, filter_args)
        # query_params['type'] = tag_type
        res = self.client.delete(endpoint=TAG_MANAGER_DELETE_TAG, data={}, payload={'filter': query_params})
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

    def assign_tag(self, tag, **scope_filter):
        """
        :param tag: Tag object
        :type tag: Tag
        :return: created Tag object
        :rtype: ManagementResponse
        """
        logging.info('Assign Tag with filter={}, with data="{}"'.format(scope_filter, tag))
        res = self.client.post(endpoint=TAG_MANAGER_ATTACH_ENDPOINT_TAGS, data=tag,
                               query_filter=scope_filter)
        logger.info('payload of assign tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to assign tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        # res.data = TagManagerEntity(**res.data)
        res.data = int(res.data['affected'])
        return res

    def unassign_tag(self, tag, **scope_filter):
        """
        :param tag: Tag object
        :type tag: Tag
        :return: created Tag object
        :rtype: ManagementResponse
        """
        logging.info('UnAssign Tag with filter={}, with data="{}"'.format(scope_filter, tag))
        res = self.client.post(endpoint=TAG_MANAGER_DETACH_ENDPOINT_TAGS, data=tag,
                               query_filter=scope_filter)
        logger.info('payload of unassign tag is {}'.format(res.response.request.body))
        if res.status_code != 200:
            logger.warning("Failed to unassign tag, response_code: {}".format(res.status_code))
            raise_from_response(res)
        # res.data = TagManagerEntity(**res.data)
        res.data = int(res.data['affected'])
        return res
