import logging

from management.common.query_filter import QueryFilter, HighScopeFilter
from management.mgmtsdk_v2.endpoints import DV_V2_GET_EVENT_TYPES, DV_V2_GET_ALL_EVENTS, \
    DV_V2_GET_EVENTS_BY_TYPE, DV_V2_GET_DISTINCT_FIELDS_DATA, DV_V2_CREATE_QUERY, DV_V2_GET_RECENT_QUERIES, \
    DV_V2_GET_QUERY_STATUS, DV_V2_GET_AGENTS, DV_V2_GET_PROCESSES, DV_V2_GET_SINGLE_EVENT, DV_V2_GET_TREE, \
    DV_V2_GET_ALL_EVENTS_IN_PROCESS_TREE, DV_V2_CREATE_PROCESS_TREE_QUERY, DV_V2_GET_PROCESS_TREE_EVENTS_BY_TYPE, \
    WATCHLIST_RULES, WATCHLIST_RULES_ENABLE, WATCHLIST_RULES_DISABLE, DV_V2_FETCH_FILE, STAR_GET_FILTERS_COUNT, \
    DV_V2_GET_ALL_PROCESSES, STAR_AVAILABLE_ACTIONS, DV_V2_CANCEL_RUNNING_QUERY, DV_V2_CREATE_POWER_QUERY, DV_V2_PING_POWER_QUERY
from management.mgmtsdk_v2.entities.deep_visibility_v2 import Event, BasicQuery, QueryStatus, StarAlert, Rule
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import STAR_ALERTS, STAR_ANALYST_VERDICT, STAR_INCIDENT

logger = logging.getLogger('Deep-Visibility')


class ProcessTreeQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'childrenDepth': ['eq'],
        'fetchAllChildren': ['eq'],
        'queryId': ['eq'],
        'selectedEventId': ['eq'],
        'subQuery': ['eq'],
        'withParents': ['eq'],
        'withParentsChildren': ['eq'],
        'siteId': ['eq']
    }

    def __init__(self):
        super(ProcessTreeQueryFilter, self).__init__()


class AgentsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'limit': ['eq'],
        'name': ['like'],
        'queryId': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
    }

    def __init__(self):
        super(AgentsQueryFilter, self).__init__()


class ProcessesQueryFilter(QueryFilter):
    QUERY_ARGS = {

        'agentUuid': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'limit': ['eq'],
        'name': ['like'],
        'queryId': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
    }

    def __init__(self):
        super(ProcessesQueryFilter, self).__init__()


class ProcessTreeEventsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'eventType': ['eq'],
        'filters': ['eq'],
        'limit': ['eq'],
        'pivotQuery': ['eq'],
        'queryId': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'subQuery': ['eq'],
    }

    def __init__(self):
        super(ProcessTreeEventsQueryFilter, self).__init__()


class DeepVisibilityQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'cursor': ['eq'],
        'groupId': ['in'],
        'fromDate': ['eq'],
        'limit': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'tenant': ['eq'],
        'toDate': ['eq'],
    }

    def __init__(self):
        super(DeepVisibilityQueryFilter, self).__init__()


class EventsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'cursor': ['eq'],
        'eventType': ['eq'],
        'filters': ['eq'],
        'groupIds': ['eq'],
        'limit': ['eq'],
        'pivotQuery': ['eq'],
        'queryId': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(EventsQueryFilter, self).__init__()


class DistinctQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'cursor': ['eq'],
        'eventType': ['eq'],
        'fieldId': ['eq'],
        'fieldName': ['eq'],
        'fieldSearchQuery': ['eq'],
        'filters': ['eq'],
        'groupIds': ['eq'],
        'limit': ['eq'],
        'pivotQuery': ['eq'],
        'query': ['eq'],
        'queryId': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(DistinctQueryFilter, self).__init__()


class BasicQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'limit': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(BasicQueryFilter, self).__init__()


class RuleQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'tenant': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(RuleQueryFilter, self).__init__()


class AlertsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'ids': ['eq'],
        'createdAt': ['gte', 'lte', 'gt', 'lt'],
        'reportedAt': ['gte', 'lte', 'gt', 'lt'],
        'ruleName': ['contains'],
        'origAgentOsName': ['in'],
        'origAgentOsRevision': ['contains'],
        'origAgentVersion': ['contains'],
        'origAgentUuid': ['contains'],
        'origAgentName': ['contains'],
        'origAgentMachineType': ['in'],
        'analystVerdict': ['eq'],
        'incidentStatus': ['eq'],
        'sourceProcessName': ['contains'],
        'sourceProcessStoryline': ['contains'],
        'sourceProcessCommandline': ['contains'],
        'sourceProcessFileHashSha1': ['contains'],
        'sourceProcessFileHashSha256': ['contains'],
        'sourceProcessFileHashMd5': ['contains'],
        'sourceProcessFilePath': ['contains'],
        'sourceProcessPid': ['contains'],
        'k8sCluster': ['contains'],
        'k8sNode': ['contains'],
        'k8sNamespace': ['contains'],
        'k8sNamespaceName': ['contains'],
        'k8sNamespaceLabels': ['contains'],
        'k8sControllerName': ['contains'],
        'k8sControllerLabelsStr': ['contains'],
        'k8sControllerLabels': ['contains'],
        'k8sPod': ['contains'],
        'k8sPodLabels': ['contains'],
        'k8sContainerName': ['contains'],
        'k8sContainerImage': ['contains'],
        'k8sContainerLabels': ['contains'],
        'osType': ['eq'],
        'machineType': ['eq'],
        'containerName': ['contains'],
        'containerImageName': ['contains'],
        'containerLabels': ['contains'],
        'limit': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
        'siteIds': ['eq'],
        'accountIds': ['eq'],
    }

    def __init__(self):
        super(AlertsQueryFilter, self).__init__()


class DeepVisibilityV2(object):
    def __init__(self, client):
        self.client = client

    def get_event_types(self, query_id, query_filter=None, **dv_args):
        """
        """
        query_params = HighScopeFilter.get_query_params(query_filter, dv_args)
        query_params['queryId'] = query_id
        res = self.client.get(endpoint=DV_V2_GET_EVENT_TYPES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to fetch events for query_id {}, response_code: {}".format(query_id, res.status_code))
            raise_from_response(res)
        return res

    def get_distinct_fields_data(self, query_filter=None, **dv_args):
        """
        Gets a ``Process`` object from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: Process object answering the query
        :rtype: ManagementResponse
        """
        query_params = DistinctQueryFilter.get_query_params(query_filter, dv_args)

        res = self.client.get(endpoint=DV_V2_GET_DISTINCT_FIELDS_DATA, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_all_events(self, query_filter=None, **dv_args):
        """
        Gets a list of ``DVEvents`` from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: list of DVEvent object answering the query
        :rtype: ManagementResponse
        """
        query_params = EventsQueryFilter.get_query_params(query_filter, dv_args)
        ret = list()
        res = self.client.get(endpoint=DV_V2_GET_ALL_EVENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get deep visibility events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def get_all_processes(self, query_filter=None, **dv_args):
        """
        Gets a list of ``DVProcesses`` from the console by filters, default filter is empty

        :type query_filter: UpdateQueryFilter
        :type dv_args: **dict
        :return: list of DVProcess object answering the query
        :rtype: ManagementResponse
        """
        query_params = EventsQueryFilter.get_query_params(query_filter, dv_args)
        ret = list()
        res = self.client.get(endpoint=DV_V2_GET_ALL_PROCESSES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get deep visibility events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def get_events_by_type(self, event_type, query_filter=None, **dv_args):
        query_params = EventsQueryFilter.get_query_params(query_filter, dv_args)
        ret = list()
        res = self.client.get(endpoint=DV_V2_GET_EVENTS_BY_TYPE.format(event_type), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get agent breakdown, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def create_query(self, dv_query):
        """
        :type dv_query: DvQuery
        :return:
        """
        payload = dv_query.to_json()
        logging.info('The payload is: {}'.format(payload))
        res = self.client.post(endpoint=DV_V2_CREATE_QUERY, payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['queryId']
        return res

    def create_power_query(self, query, from_date, to_date, account_ids=None, limit=None, site_ids=None):
        """
        :type query: string
        :type from_date: string
        :type to_date: string
        :type account_ids: string []
        :type limit: int
        :type site_ids: string []
        """
        payload = {
            "query": query,
            "fromDate": from_date,
            "toDate": to_date
        }

        if account_ids:
            payload["accountIds"] = account_ids
        if site_ids:
            payload["siteIds"] = site_ids
        if limit:
            payload["limit"] = limit

        logging.info('The payload is: {}'.format(payload))
        res = self.client.post(endpoint=DV_V2_CREATE_POWER_QUERY, payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to create_power_query, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_ping_power_query(self, query_id):
        res = self.client.get(endpoint=DV_V2_PING_POWER_QUERY, params={'queryId': query_id})
        if res.status_code != 200:
            logger.warning("Failed to get_ping_power_query, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Event(**res.data)
        return res

    def cancel_query(self, query_id):
        """
        :type int: cancel_query
        :return:
        """
        payload = {
            "queryId": query_id
        }
        logging.info('The payload is: {}'.format(payload))
        res = self.client.post(endpoint=DV_V2_CANCEL_RUNNING_QUERY, payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to cancel_query, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res.data['success']

    def get_recent_queries(self, query_filter=None, **dv_args):
        ret = list()
        query_params = BasicQueryFilter.get_query_params(query_filter, dv_args)
        res = self.client.get(endpoint=DV_V2_GET_RECENT_QUERIES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(BasicQuery(**current))
        res.data = ret
        return res

    def get_query_status(self, query_id, query_filter=None, **dv_args):
        query_params = HighScopeFilter.get_query_params(query_filter, dv_args)
        query_params['queryId'] = query_id
        res = self.client.get(endpoint=DV_V2_GET_QUERY_STATUS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get query status for query_id {}, response is: {}".format(query_id, res.response))
            logger.warning("Failed to get query status for query_id {}, response_code: {}".format(query_id, res.status_code))
            raise_from_response(res)
        res.data = QueryStatus(**res.data)
        return res

    def get_agents(self, query_filter=None, **agents_args):
        ret = list()
        query_params = AgentsQueryFilter.get_query_params(query_filter, agents_args)
        res = self.client.get(endpoint=DV_V2_GET_AGENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def get_single_event(self, event_id, query_id):
        res = self.client.get(endpoint=DV_V2_GET_SINGLE_EVENT,
                              params={'eventId': event_id, 'queryId': query_id})
        if res.status_code != 200:
            logger.warning("Failed to get deep visibility events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Event(**res.data)
        return res

    def get_processes(self, query_filter=None, **processes_args):
        ret = list()
        query_params = ProcessesQueryFilter.get_query_params(query_filter, processes_args)
        res = self.client.get(endpoint=DV_V2_GET_PROCESSES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def get_tree(self, query_filter=None, **tree_args):
        query_params = ProcessTreeQueryFilter.get_query_params(query_filter, tree_args)
        res = self.client.get(endpoint=DV_V2_GET_TREE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_all_events_in_process_tree(self, query_filter=None, **pt_args):
        ret = list()
        query_params = ProcessTreeEventsQueryFilter.get_query_params(query_filter, pt_args)
        res = self.client.get(endpoint=DV_V2_GET_ALL_EVENTS_IN_PROCESS_TREE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def create_process_tree_query(self, process_tree_query):
        res = self.client.post(endpoint=DV_V2_CREATE_PROCESS_TREE_QUERY, payload=process_tree_query.to_json())
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['queryId']
        return res

    def get_process_tree_events_by_type(self, event_type, query_filter=None, **pt_events_args):
        ret = list()
        query_params = DV_V2_GET_PROCESS_TREE_EVENTS_BY_TYPE.get_query_params(query_filter, pt_events_args)
        res = self.client.get(endpoint=DV_V2_GET_PROCESS_TREE_EVENTS_BY_TYPE.format(event_type), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get process, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for current in res.data:
            ret.append(Event(**current))
        res.data = ret
        return res

    def create_rule(self, rule, query_filter=None, **rule_args):
        query_params = RuleQueryFilter.get_query_params(query_filter, rule_args)
        if not query_params:
            query_params = {'tenant': 'true'}
        res = self.client.post(endpoint=WATCHLIST_RULES, data=rule.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create rule, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        rule.id = res.data['id']
        return res.data['id']

    def get_rules(self, **query_filter):
        res = self.client.get(endpoint=WATCHLIST_RULES, params=query_filter)
        if res.status_code != 200:
            logger.warning("Failed to get rules, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        rules = list()
        for rule in res.json['data']:
            rules.append(Rule(**rule))
        return rules

    def available_actions(self, ids):
        res = self.client.get(endpoint=STAR_AVAILABLE_ACTIONS, params={'ids': ids})
        if res.status_code != 200:
            logger.warning("Failed to get available actions, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']

    def edit_rule(self, rule_id, rule, query_filter=None, **rule_args):
        query_params = RuleQueryFilter.get_query_params(query_filter, rule_args)
        if not query_params:
            query_params = {'tenant': 'true'}
        res = self.client.put(endpoint=f'{WATCHLIST_RULES}/{rule_id}', data=rule.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to edit rule, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return Rule(**res.json['data'])

    def enable_rule(self, rule_id):
        res = self.client.put(endpoint=WATCHLIST_RULES_ENABLE, query_filter={'ids': rule_id})
        if res.status_code != 200:
            logger.warning("Failed to activate rule, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']['affected']

    def disable_rule(self, rule_id):
        res = self.client.put(endpoint=WATCHLIST_RULES_DISABLE, query_filter={'ids': rule_id})
        if res.status_code != 200:
            logger.warning("Failed to activate rule, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']['affected']

    def delete_rule(self, rule_id):
        res = self.client.delete(endpoint=WATCHLIST_RULES, data={}, payload={'filter': {'ids': rule_id}})
        if res.status_code != 200:
            logger.warning("Failed to delete rule, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']['affected']

    def get_alerts(self, query_filter=None, **alert_args):
        query_params = AlertsQueryFilter.get_query_params(query_filter, alert_args)
        res = self.client.get(endpoint=STAR_ALERTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get alerts, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        alerts = list()
        for alert in res.json['data']:
            alerts.append(StarAlert(**alert))
        return alerts

    def star_analyst_verdict(self, ids, verdict, **query_filter):
        res = self.client.post(endpoint=STAR_ANALYST_VERDICT, data={'analystVerdict': verdict},
                               query_filter={'ids': ids, **query_filter})
        if res.status_code != 200:
            logger.warning("Failed to set analyst verdict, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']['affected']

    def star_incident_status(self, ids, status, **query_filter):
        res = self.client.post(endpoint=STAR_INCIDENT, data={'incidentStatus': status},
                               query_filter={'ids': ids, **query_filter})
        if res.status_code != 200:
            logger.warning("Failed to set incident status, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res.json['data']['affected']

    def fetch_file(self, download_token):
        res = self.client.get(endpoint=DV_V2_FETCH_FILE, params={'downloadToken': download_token})
        if res.status_code != 200:
            logger.warning("Failed to fetch file, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)
        return res

    def get_star_rule_count(self):
        res = self.client.get(endpoint=STAR_GET_FILTERS_COUNT)
        if res.status_code != 200:
            logger.warning("Failed to get star rules count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
