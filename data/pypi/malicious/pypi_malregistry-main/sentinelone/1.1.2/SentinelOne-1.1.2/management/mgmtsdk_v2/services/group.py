import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import GET_GROUPS, COUNT_GROUPS, \
    GET_GROUP_BY_ID, GET_DEFAULT_GROUP, GET_GROUP_POLICY, UPDATE_GROUP_POLICY, \
    UPDATE_RANKS, CREATE_GROUP, MOVE_AGENTS, DELETE_GROUP, REVERT_GROUP_POLICY, REGENERATE_GROUP_KEY
from management.mgmtsdk_v2.entities.group import Group, GroupCount
from management.mgmtsdk_v2.entities.policy import Policy

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Group')


class GroupQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountId': ['eq'],
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gte', 'lte'],
        'cursor': ['eq'],
        'domains': ['eq'],
        'filterId': ['eq'],
        'frequency': ['eq'],
        'fromDate': ['eq'],
        'groupIds': ['eq', 'in'],
        'id': ['eq', 'in'],
        'ids': ['eq'],
        'isDefault': ['eq'],
        'interval': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'osTypes': ['eq'],
        'query': ['eq'],
        'rank': ['eq'],
        'registeredAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'registrationToken': ['eq'],
        'scheduleType': ['eq'],
        'scope': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'taskId': ['eq'],
        'toDate': ['eq'],
        'type': ['eq'],
        'uuid': ['eq'],
        'uuids': ['eq'],
    }

    def __init__(self):
        super(GroupQueryFilter, self).__init__()


class Groups(object):
    """Groups service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **group_args):
        """
        Get list of ``Groups`` from the console by filters, default filter is empty

        :type query_filter: GroupQueryFilter
        :type group_args: **dict
        :return: Groups answering the query
        :rtype: ManagementResponse
        """
        query_params = GroupQueryFilter.get_query_params(query_filter, group_args)
        res = self.client.get(endpoint=GET_GROUPS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get groups, response_code: {}".format(res.status_code))
            raise_from_response(res)

        res.data = [Group(**group) for group in res.data]
        return res

    def get_by_id(self, id):
        """
        Get a ``Group`` object by its id

        :type id: string
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_GROUP_BY_ID.format(id))
        if res.status_code != 200:
            logger.warning("Failed to get group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Group(**res.data)
        return res

    def count(self, query_filter=None, **group_args):
        """
        Counts ``Groups`` from the console by filters, default filter is empty
        Result is grouped by ``dynamic`` and ``static`` group types

        :type query_filter: GroupQueryFilter
        :type group_args: **dict
        :rtype: ManagementResponse
        """
        query_params = GroupQueryFilter.get_query_params(query_filter, group_args)
        res = self.client.get(endpoint=COUNT_GROUPS, params=query_params)

        if res.status_code != 200:
            logger.warning("Failed to count groups, response_code: {}".format(res.status_code))
            raise_from_response(res)

        res.data = GroupCount(**res.data)
        return res

    def get_default(self, query_filter=None, **group_args):
        """
        Get the default ``Group`` from the console by filters, default filter is empty
        In the given query_filter, exactly a single 1 siteId must be set

        :type query_filter: GroupQueryFilter
        :type group_args: **dict
        :rtype: ManagementResponse
        """
        query_params = GroupQueryFilter.get_query_params(query_filter, group_args)
        if query_params['siteIds'] is None or len(query_params['siteIds']) != 1:
            raise ValueError("send exactly 1 siteId to get default group")
        res = self.client.get(endpoint=GET_DEFAULT_GROUP, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get default group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Group(**res.data)
        return res

    def update_ranks(self, data, query_filter=None, **group_args):
        """
        Get ranks of a ``Group`` from the console by filters, default filter is empty
        Returns ManagementResponse if ``Group`` updated successfully, raises an exception otherwise

        :param data: Dict of parameters to update
        :type data: dict
        :type query_filter: GroupQueryFilter
        :type group_args: **dict
        :rtype: ManagementResponse
        """
        query_params = GroupQueryFilter.get_query_params(query_filter, group_args)
        res = self.client.put(endpoint=UPDATE_RANKS, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update ranks, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def create(self, group):
        """
        Creates an new ``Group`` with given data
        Returns True if Group created successfully, raises an exception otherwise

        :param group: Group object to create
        :type group: Group
        :return: ManagementResponse

        """
        res = self.client.post(endpoint=CREATE_GROUP, data=group.to_json())
        if res.status_code != 200:
            logger.warning("Failed to create group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Group(**res.data)
        return res

    def regenerate_key(self, group_id):
        """
        :param group_id:
        :return: new registration token
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=REGENERATE_GROUP_KEY.format(group_id))
        if res.status_code != 200:
            logger.warning("Failed to regenerate key for group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['registrationToken']
        return res

    def revert_policy(self, group_id):
        """
        Reverts a policy of a ``Group`` with given id
        :param group_id: id of group of whose policy to revert
        :type group_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=REVERT_GROUP_POLICY.format(group_id))
        if res.status_code != 200:
            logger.warning("Failed to revert policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update_policy(self, group_id, **kwargs):
        """
        Updates a policy of a ``Group`` with given id and parameters

        :type group_id: string
        :type kwargs: parameters to update
        :rtype: ManagementResponse
        """
        policy = self.get_policy(group_id).data
        policy_dict = policy.to_json()
        policy_dict.update(kwargs)
        res = self.client.put(endpoint=UPDATE_GROUP_POLICY.format(group_id), data=policy_dict)
        if res.status_code != 200:
            logger.warning("Failed to update group policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get_policy(self, group_id):
        """
        Gets the ``Policy`` of a given group id

        :type group_id:
        :return: policy of group by given site_id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_GROUP_POLICY.format(group_id))
        if res.status_code != 200:
            logger.warning("Failed to get site policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def move_agents(self, group_id, query_filter=None, **group_args):
        """
        Moves agents from one ``Group`` to another
        Returns the number of agents actually moved

        :type group_id: string
        :type query_filter: GroupQueryFilter
        :type group_args: **dict
        :rtype: ManagementResponse
        """
        query_params = GroupQueryFilter.get_query_params(query_filter, group_args)
        res = self.client.put(endpoint=MOVE_AGENTS.format(group_id), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to move agents, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data["agentsMoved"]
        return res

    def delete(self, group_id):
        """
        Deletes a ``Group`` by its id
        Returns True if Group deleted successfully, raises an exception otherwise
        :type group_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_GROUP.format(group_id))
        if res.status_code != 200:
            logger.warning("Failed to delete group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update(self, group_id, **data):
        """
        Updates an existing ``Group`` of given id, with given parameters
        Returns updated Group if updated successfully, raises an exception otherwise
        :param data: Dict of parameters to update
        :type data: dict
        :param group_id: id of group to update
        :type group_id: string
        :param: group data object
        :return: updated group
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=DELETE_GROUP.format(group_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to update group, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Group(**res.data)
        return res
