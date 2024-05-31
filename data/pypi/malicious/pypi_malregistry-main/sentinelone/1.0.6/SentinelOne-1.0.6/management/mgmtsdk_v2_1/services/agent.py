import logging

from management.common.query_filter import QueryFilter, NoTenantScopeFilter
from management.mgmtsdk_v2_1.endpoints import GET_AGENTS, COUNT_AGENTS, \
    COUNT_AGENTS_BY_FILTERS, \
    AGENTS_COUNT_SUMMARY, GET_APPLICATIONS, GET_PASSPHRASES, GET_PROCESSES, \
    EXPORT_LOGS, AGENTS_FILTERS_AUTOCOMPLETE
from management.mgmtsdk_v2_1.entities.agent import Agent, AgentCountSummary, \
    Application, Process

from management.mgmtsdk_v2.exceptions import raise_from_response


logger = logging.getLogger('Agent')


class AgentQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'activeThreats': ['eq', 'gt'],
        'adQuery': ['eq', 'contains'],
        'adUserName': ['contains'],
        'adUserMember': ['contains'],
        'adComputerName': ['contains'],
        'adComputerMember': ['contains'],
        'adUserQuery': ['contains'],
        'adComputerQuery': ['contains'],
        'agentVersion': ['in'],
        'agentVersions': ['eq'],
        'computerName': ['eq', 'like', 'contains'],
        'countOnly': ['eq'],
        'coreCount': ['gte', 'lte', 'gt', 'lt', 'between'],
        'cpuCount': ['gte', 'lte', 'gt', 'lt', 'between'],
        'createdAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'cursor': ['eq'],
        'domain': ['in'],
        'encryptedApplication': ['in'],
        'externalIp': ['contains'],
        'filterId': ['eq'],
        'groupIds': ['eq'],
        'id': ['eq'],
        'ids': ['eq'],
        'infected': ['eq'],
        'isActive': ['eq'],
        'isDecommissioned': ['eq'],
        'isPendingUninstall': ['eq'],
        'isUninstalled': ['eq'],
        'isUpToDate': ['eq'],
        'lastActiveDate': ['gte', 'lte', 'gt', 'lt', 'between'],
        'lastLoggedInUserName': ['contains'],
        'limit': ['eq'],
        'localConfiguration': ['eq'],
        'machineType': ['in'],
        'mitigationMode': ['eq'],
        'mitigationModeSuspicious': ['eq'],
        'networkInterfaceInet': ['contains'],
        'networkInterfacePhysical': ['contains'],
        'networkStatuses': ['eq'],
        'osName': ['contains'],
        'osRevision': ['contains'],
        'osVersion': ['contains'],
        'osArch': ['eq'],
        'osTypes': ['eq'],
        'query': ['eq'],
        'registeredAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'scanStatus': ['eq', 'in'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'totalMemory': ['gte', 'lte', 'gt', 'lt', 'between'],
        'threatContentHash': ['eq'],
        'threatCreatedAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'threatHidden': ['eq'],
        'threatMitigationStatus': ['eq'],
        'threatResolved': ['eq'],
        'userActionsNeeded': ['eq'],
        'uuid': ['eq', 'in', 'contains'],
        'externalId': ['contains'],
        'installerTypes': ['eq'],
        'operationalStates': ['eq'],
        'tagsData': ['eq'],
        'hasTags': ['eq'],
    }

    def __init__(self):
        super(AgentQueryFilter, self).__init__()


class Agents(object):
    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **agent_args):
        """
        Get list of ``Agent`` from the console by filters, default filter is empty

        :type query_filter: AgentQueryFilter
        :type agent_args: dict
        :rtype: ManagementResponse
        """
        query_params = AgentQueryFilter.get_query_params(query_filter, agent_args)
        res = self.client.get(endpoint=GET_AGENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get agents, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Agent(**agent) for agent in res.data]
        return res

    def count(self, query_filter=None, **agent_args):
        """
        Count number of ``Agents`` from the console by filter, 
        default filter is empty 
        
        :type query_filter: AgentQueryFilter
        :type agent_args: dict
        :rtype: ManagementResponse
        """
        query_params = AgentQueryFilter.get_query_params(query_filter, agent_args)
        res = self.client.get(endpoint=COUNT_AGENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to count agents, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['total'])
        return res

    def count_by_filters(self, query_filter=None, **agent_args):
        """
        Get count of ``Agents`` from the console by filter value, 
        default filter is empty 

        Returns filtered count of agents
        
        :type query_filter: AgentQueryFilter
        :type agent_args: dict
        :rtype: ManagementResponse
        """
        query_params = AgentQueryFilter.get_query_params(query_filter, agent_args)
        res = self.client.get(endpoint=COUNT_AGENTS_BY_FILTERS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to count agents, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = {fc['key']: {fcv['title']: fcv['count'] for fcv in fc['values']} for fc in res.data}
        return res

    def filters_auto_complete(self, key, text, query_filter=None, **agent_args):
        query_params = AgentQueryFilter.get_query_params(query_filter, agent_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=AGENTS_FILTERS_AUTOCOMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get autocomplete, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def count_summary(self, query_filter=None, **agent_args):
        """
        Summary of agents by numbers
        :type query_filter: AgentQueryFilter
        :type agent_args: dict
        :rtype: ManagementResponse
        """
        query_params = NoTenantScopeFilter.get_query_params(query_filter, agent_args)
        res = self.client.get(endpoint=AGENTS_COUNT_SUMMARY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get count summary, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = AgentCountSummary(**res.data)
        return res

    def get_applications(self, agentIds):
        """
        Retrieve running applications for a specific agent
    
        :type agentIds: list
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_APPLICATIONS, params={'ids': agentIds})
        if res.status_code != 200:
            logger.warning("Failed to get applications, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Application(**app) for app in res.data]
        return res

    def get_processes(self, agentIds):
        """
        Retrieve running processes for a specific agent
        
        :type agentIds: list
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_PROCESSES, params={'ids': agentIds})
        if res.status_code != 200:
            logger.warning("Failed to get applications, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Process(**proc) for proc in res.data]
        return res

    def get_passphrases(self, query_filter=None, **agent_args):
        """
        Get passphrases of ``Agents`` from the console by filter value, 
        default filter is empty 
        
        :type query_filter: AgentQueryFilter
        :type agent_args: dict
        :rtype: ManagementResponse
        """
        query_params = AgentQueryFilter.get_query_params(query_filter, agent_args)
        res = self.client.get(endpoint=GET_PASSPHRASES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get passphrases, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = {entry['id']: entry['passphrase'] for entry in res.data}
        return res

    def export_logs(self, agent_id, activity_id):
        """
        Export ``agent`` logs by ``activity`` id
        
        :type agent_id: string
        :type activity_id: string
        :return: list
        """
        res = self.client.get(endpoint=EXPORT_LOGS.format(agent_id, activity_id), use_raw=True, stream=True)
        if res.status_code != 200:
            logger.warning("Failed to export logs, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
