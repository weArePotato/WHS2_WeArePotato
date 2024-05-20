import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import GET_EVENT_SEEN_ON_NETWORK, \
    GET_PROCESS_BY_UNIQUE_KEY, GET_EVENTS, \
    GET_AGENTS_BREAKDOWN, GET_PROCESS_BY_AGENT, GET_AGENT_SEEN_ON_NETWORK, \
    GET_EVENTS_BY_PROCESS
from management.mgmtsdk_v2.entities.deep_visibility import SeenOnNetwork, \
    Process, DVEvent, AgentBreakdown

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Deep-Visibility')


class DeepVisibilityQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'cursor': ['eq'],
        'fromDate': ['eq'],
        'groupId': ['in'],
        'limit': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'tenant': ['eq'],
        'toDate': ['eq'],
    }

    def __init__(self):
        super(DeepVisibilityQueryFilter, self).__init__()


class DeepVisibility(object):
    def __init__(self, client):
        self.client = client

    def get_event_seen_on_network(self, query_filter=None, **dv_args):
        """
        Gets a ``SeenOnNetwork`` object for an ``Event`` from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: SeenOnNetwork object answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)

        res = self.client.get(endpoint=GET_EVENT_SEEN_ON_NETWORK, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get event seen on network, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SeenOnNetwork(**res.data)
        return res

    def get_agent_seen_on_network(self, uuid, query_filter=None, **dv_args):
        """
        Gets a ``SeenOnNetwork`` object for an ``Agent`` from the console by filters, default filter is empty

        :param uuid: agent uuid
        :type uuid: string
        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: SeenOnNetwork object answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)
        query_params['uuid'] = uuid
        res = self.client.get(endpoint=GET_AGENT_SEEN_ON_NETWORK.format(uuid), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get agent seen on network, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SeenOnNetwork(**res.data)
        return res

    def get_process_by_unique_key(self, query_filter=None, **dv_args):
        """
        Gets a ``Process`` object from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: Process object answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)

        res = self.client.get(endpoint=GET_PROCESS_BY_UNIQUE_KEY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Process(**res.data)
        return res

    def get_events(self, query_filter=None, **dv_args):
        """
        Gets a list of ``DVEvents`` from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: list of DVEvent object answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)

        res = self.client.get(endpoint=GET_EVENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get deep visibility events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [DVEvent(**dve) for dve in res.data['results']]
        return res

    def get_agents_breakdown(self, query_filter=None, **dv_args):
        """
        Gets a breakdown of agents from the console by filters, default filter is empty
        Result appears in ``data`` field as a ``AgentBreakdown`` object

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: AgentBreakdown objects answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)

        res = self.client.get(endpoint=GET_AGENTS_BREAKDOWN, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get agent breakdown, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [AgentBreakdown(**ab) for ab in res.data['results']]
        return res

    def get_unique_process_by_agent(self, uuid, query_filter=None, **dv_args):
        """
        Gets a list of ``DVEvents`` ralated to a unique process from the console by agent uuid,
        filters, default filter is empty

        :param uuid: agent uuid
        :type uuid: string
        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: DVEvent objects answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)
        query_params['uuid'] = uuid
        res = self.client.get(endpoint=GET_PROCESS_BY_AGENT.format(uuid), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [DVEvent(**ab) for ab in res.data['results']]
        return res

    def get_events_by_process(self, process_unique_key, query_filter=None, **dv_args):
        """
        Gets a list of ``DVEvents`` raleted to a unique process from the console by process_unique_key,
        filters, default filter is empty

        :type process_unique_key: string
        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: DVEvent objects answering the query
        :rtype: ManagementResponse
        """
        query_params = DeepVisibilityQueryFilter.get_query_params(query_filter, dv_args)
        query_params['process_unique_key'] = process_unique_key
        res = self.client.get(endpoint=GET_EVENTS_BY_PROCESS.format(process_unique_key), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [DVEvent(**ab) for ab in res.data['results']]
        return res
