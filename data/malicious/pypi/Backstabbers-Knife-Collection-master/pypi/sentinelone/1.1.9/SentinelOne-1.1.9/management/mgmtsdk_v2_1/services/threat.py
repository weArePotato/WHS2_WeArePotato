import logging

from typing import Iterable

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import WHITENING_OPTIONS
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2_1.entities.threat import Threat, ThreatGroup

logger = logging.getLogger('Threat_2.1')


class ThreatQueryFilter(QueryFilter):
    QUERY_ARGS = {

        'createdAt': ['gt', 'gte', 'lt', 'lte'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte'],
        'contentHashes': ['eq'],
        'displayName': ['eq'],
        'mitigationStatuses': ['eq'],
        'agentIds': ['eq'],
        'storylines': ['eq'],
        'ids': ['eq'],
        'collectionIds': ['eq'],
        'engines': ['eq'],
        'classifications': ['eq'],
        'classificationSources': ['eq'],
        'agentVersions': ['eq'],
        'agentMachineTypes': ['eq'],
        'osTypes': ['eq'],
        'osArchs': ['eq'],
        'osNames': ['eq'],
        'agentIsActive': ['eq'],
        'initiatedBy': ['eq'],
        'confidenceLevels': ['eq'],
        'analystVerdicts': ['eq'],
        'incidentStatuses': ['eq'],
        'noteExists': ['eq'],
        'failedActions': ['eq'],
        'rebootRequired': ['eq'],
        'pendingActions': ['eq'],
        'externalTicketExists': ['eq'],
        'externalTicketIds': ['eq'],
        'mitigatedPreemptively': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'limit': ['eq'],
        'orderBy': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'query': ['eq'],
        'contentHash': ['contains'],
        'threatDetails': ['contains'],
        'filePath': ['contains'],
        'computerName': ['contains'],
        'uuid': ['contains'],
        'detectionAgentVersion': ['contains'],
        'components': ['eq'],
    }

    def __init__(self):
        super(ThreatQueryFilter, self).__init__()


class TimelineThreatQuery(ThreatQueryFilter):
    QUERY_ARGS = ThreatQueryFilter.QUERY_ARGS.copy()
    QUERY_ARGS['activityTypes'] = ['eq']

    def __init__(self):
        super(ThreatQueryFilter, self).__init__()

    @classmethod
    def get_query_params(cls, query_filter, filter_args):
        if filter_args and 'activityTypes' in filter_args and isinstance(filter_args['activityTypes'], Iterable):
            filter_args['activityTypes'] = ','.join(map(str, filter_args['activityTypes']))
        return super(ThreatQueryFilter, cls).get_query_params(query_filter, filter_args)


def _generate_post_data(targetScope, whiteningOption):
    post_data = dict()
    if whiteningOption is not None:
        post_data['whiteningOption'] = whiteningOption
    if targetScope is not None:
        post_data['targetScope'] = targetScope
    return post_data


class Threats(object):
    """Threats service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **threat_args):
        """
        Get list of ``Threats`` from the console by filters, default filter is empty

        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=GET_THREATS, params=query_params)  # , specific_prefix='web/api/v2.1')
        if res.status_code != 200:
            logger.warning("Failed to get threats, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Threat(**threat) for threat in res.data]
        return res

    def summary(self):
        """
        Get summary of all ``Threats`` by threat type

        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=THREATS_SUMMARY)
        if res.status_code != 200:
            logger.warning("Failed to get threats, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def groups(self, query_filter=None, **threat_args):
        """
        Get ``Threats`` grouped by filter, default filter is empty

        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=THREAT_GROUPS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threats, grouped by filter, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [ThreatGroup(**grp) for grp in res.data]
        return res

    def count_by_filters(self, query_filter=None, **threat_args):
        """
        Count number of ``Threats`` answering a filter

        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=COUNT_BY_FILTERS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat count by filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def free_text_filters(self):
        """
        Returns possible free text filters

        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def disable_engines(self, engines_to_disable):
        """
        Disables detection engines, returns indicator of success or failure

        :type engines_to_disable: List (str)
        :rtype: ManagementResponse
        """
        post_data = {'engines': engines_to_disable}
        res = self.client.post(endpoint=DISABLE_ENGINES, data=post_data)
        if res.status_code != 200:
            logger.warning("Failed to disable engines, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def mitigate(self, action, query_filter=None, **threat_args):
        """
        Mitigate ``Threat`` as resolved by filter with an action, default filter
        is empty.

        Actions could be ``kill``, ``quarantine``, ``remediate``, ``rollback-remediation``
        or ``un-quarantine``

        Returns number of affected ``Threats``
        :type action: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=MITIGATE_THREAT.format(action), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mitigate threat, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def container_network_connect(self, container_id, query_filter=None, **threat_args):
        """
        Connect ``Container`` to network

        Returns success or failure
        :type container_id: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=CONTAINER_UNQ, query_filter=query_params, data={'containerId': container_id})
        if res.status_code != 200:
            logger.warning("Failed to re-connect container, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def container_network_disconnect(self, container_id, query_filter=None, **threat_args):
        """
        Disconnect ``Container`` to network

        Returns success or failure
        :type container_id: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=CONTAINER_NQ, query_filter=query_params, data={'containerId': container_id})
        if res.status_code != 200:
            logger.warning("Failed to disconnect container, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def agents_disconnect(self, query_filter=None, **threat_args):
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=THREATS_AGENTS_DISCONNECT, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mitigate threat, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def agents_connect(self, query_filter=None, **threat_args):
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=THREATS_AGENTS_CONNECT, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mitigate threat, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def add_to_blacklist(self, targetScope, whiteningOption=None, query_filter=None, **threat_args):
        """
        Add ``Threats`` hashes to blacklist by filter

        Scope level must be provided ("account", "site", "tenant" or "group")

        Returns number of affected ``Threats``
        :type whiteningOption: string
        :type targetScope: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = _generate_post_data(targetScope, whiteningOption)
        res = self.client.post(endpoint=ADD_TO_BLACKLIST, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to add to blacklist, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def add_to_exclusions(self, target_scope, exclusion_type, query_filter=None, **threat_args):
        """
        Add ``Threats`` hashes to exclusions by filter

        Scope level must be provided ("account", "site", "tenant" or "group")

        Returns number of affected ``Threats``
        :type exclusion_type: string oneof: path, certificate, browser, file_type, hash
        :type targetScope: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = {'targetScope': target_scope, 'type': exclusion_type}
        res = self.client.post(endpoint=ADD_TO_EXCLUSIONS, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to add to exclusions, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def fetch_files(self, password, query_filter=None, **threat_args):
        """
        :type password: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = {'password': password}
        res = self.client.post(endpoint=FETCH_THREAT, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to fetch threat files, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def filters_auto_complete(self, key, text, query_filter=None, **threat_args):
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=THREATS_FILTERS_AUTOCOMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get autocomplete, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def dv_mark_as_threat(self, status, events, initiated_by=None):
        data = {
            'status': status,
            'events': events,
        }
        if initiated_by:
            data['initiatedBy'] = initiated_by
        res = self.client.post(endpoint=DV_MARK_AS_THREAT, data=data)
        if res.status_code != 200:
            logger.warning('Failed to send DV mark as threat POST request. Response code: {}'.format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def dv_add_to_blacklist(self, target_scope, hashes):
        data = {
            'targetScope': target_scope,
            'hashes': hashes,
        }
        res = self.client.post(endpoint=DV_ADD_TO_BLACKLIST, data=data)
        if res.status_code != 200:
            logger.warning('Failed to send DV add to blacklist POST request. Response code: {}'.format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def export_threats(self, query_filter=None, **threat_args):
        """
        Export threats from the console by filters, default filter is empty
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=EXPORT_THREATS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to export threats, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def threat_analysis(self, threat_id, query_filter=None, **threat_args):
        """
        Get threat analysis information
        Available components: threatInfo, mitigationStatus, agentRealtimeInfo, agentDetectionInfo, containerInfo,
        kubernetesInfo, indicators. Empty means all components.
        :type threat_id
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=THREAT_ANALYSIS.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat analysis, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def threat_appearances(self, threat_id):
        """
        Get appearances details (network history info) of a detected threat
        :type threat_id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=THREAT_APPEARANCES.format(threat_id))
        if res.status_code != 200:
            logger.warning("Failed to get threat appearances details, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_threat_timeline(self, threat_id, query_filter=None, **threat_args):
        """
        Get threat timeline, paginated, with sorting and filtering options. Default sorting: createdAt, desc.
        :type threat_id
        :type query_filter: ThreatTimelineQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = TimelineThreatQuery.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=THREAT_TIMELINE.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat timeline, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_threat_timeline_categories(self):
        """
        Get the available categories of activities in the timeline.
        Maps each category name to the belonging activity types.

        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=THREAT_TIMELINE_CATEGORIES)
        if res.status_code != 200:
            logger.warning("Failed to get threat timeline categories, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_threat_timeline(self, threat_id, query_filter=None, **threat_args):
        """
        Export threat timeline, with sorting and filtering options. Default sorting: createdAt, desc.
        :type threat_id
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=EXPORT_THREAT_TIMELINE.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to export threat timeline, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def update_threat_external_ticket(self, external_ticket_id, query_filter=None, **threat_args):
        """
        Update Threats External Ticket Id
        :param external_ticket_id:
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        data = {
            'externalTicketId': external_ticket_id
        }
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=EXTERNAL_TICKET_ID, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update threat external ticket, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def update_threat_analyst_verdict(self, analyst_verdict, query_filter=None, **threat_args):
        """
        Update threats analyst verdict.
        :param analyst_verdict:
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        data = {
            'analystVerdict': analyst_verdict
        }
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=UPDATE_THREAT_ANALYST_VERDICT, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update threat analyst verdict, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def update_threat_incident(self, incident_status, analyst_verdict=None, query_filter=None, **threat_args):
        """
        Update threats incident.
        :param incident_status:
        :param analyst_verdict: [Optional] A new analyst verdict to set
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        data = {
            'incidentStatus': incident_status
        }
        if analyst_verdict:
            data['analystVerdict'] = analyst_verdict
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=UPDATE_THREAT_INCIDENT, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update threat incident, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def download_mitigation_report(self, report_id):
        res = self.client.get(endpoint=DOWNLOAD_MITIGATION_REPORT.format(report_id))
        if res.status_code != 200:
            logger.warn("Failed to download mitigation report, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return bytearray(res.response.content)

    def get_threat_available_actions(self, query_filter=None, **threat_args):
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=AVAILABLE_ACTIONS, params=query_params)  # , specific_prefix='web/api/v2.1')
        if res.status_code != 200:
            logger.warning("Failed to get threats, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_whitening_options(self, threat=None, threat_id=''):
        id = threat_id if threat_id else threat.id
        res = self.client.get(endpoint=WHITENING_OPTIONS.format(id))
        if res.status_code != 200:
            logger.warning("Failed to get whitening_options, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def download_from_cloud(self, threat_id):
        res = self.client.get(endpoint=DOWNLOAD_THREAT_FROM_CLOUD.format(threat_id))
        if res.status_code != 200:
            logger.warning("Failed to get download_from_cloud details, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
