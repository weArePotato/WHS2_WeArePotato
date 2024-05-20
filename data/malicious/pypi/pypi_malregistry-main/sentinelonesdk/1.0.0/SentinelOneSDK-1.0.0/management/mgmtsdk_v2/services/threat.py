import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.threat import Threat
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Threat')


class ThreatQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'agentId': ['eq'],
        'agentIds': ['eq'],
        'agentIsActive': ['eq'],
        'classifications': ['in'],
        'classificationSource': ['in'],
        'collectionId': ['in'],
        'computerName': ['contains'],
        'contentHash': ['eq', 'in', 'contains'],
        'contentHashes': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte'],
        'cursor': ['eq'],
        'displayName': ['eq', 'like'],
        'engine': ['eq'],
        'engines': ['eq'],
        'fromScan': ['eq'],
        'initiatedBy': ['eq'],
        'groupIds': ['eq'],
        'hidden': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'maliciousGroupId': ['in'],
        'mitigationStatuses': ['eq'],
        'orderBy': ['eq'],
        'osTypes': ['eq'],
        'query': ['eq'],
        'resolved': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'status': ['eq'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte'],
        'uuid': ['contains'],
    }

    def __init__(self):
        super(ThreatQueryFilter, self).__init__()


def _generate_post_data(annotation, annotation_url, targetScope, whiteningOption):
    post_data = dict()
    if annotation is not None:
        post_data['annotation'] = annotation
    if annotation_url is not None:
        post_data['annotationUrl'] = annotation_url
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
        res = self.client.get(endpoint=GET_THREATS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threats, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Threat(**threat) for threat in res.data]
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

    def mark_as_resolved(self, annotation=None, annotation_url=None, query_filter=None, **threat_args):
        """
        Mark ``Threat`` as resolved by filter with annotation message/url 
        (optional), default filter is empty.
        Returns number of affected ``Threats``
        
        :type annotation: string
        :type annotation_url: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = dict()
        if annotation is not None:
            post_data['annotation'] = annotation
        if annotation_url is not None:
            post_data['annotationUrl'] = annotation_url
        res = self.client.post(endpoint=MARK_AS_RESOLVED, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mark as resolved, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def mark_as_unresolved(self, annotation=None, annotation_url=None, query_filter=None, **threat_args):
        """
        Mark ``Threat`` as unresolved by filter with annotation message/url
        (optional), default filter is empty.
        Returns number of affected ``Threats``

        :type annotation: string
        :type annotation_url: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = dict()
        if annotation is not None:
            post_data['annotation'] = annotation
        if annotation_url is not None:
            post_data['annotationUrl'] = annotation_url
        res = self.client.post(endpoint=MARK_AS_UNRESOLVED, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mark as unresolved, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def mark_as_threat(self, targetScope, annotation=None, annotation_url=None, whiteningOption=None,
                       query_filter=None, **threat_args):
        """
        Mark ``Threat`` as resolved by filter with annotation 
        message/url (optional), default filter is empty.
        
        Scope level must be provided ("site", "tenant" or "group")
        
        Returns number of affected ``Threats``
    
        :type annotation: string
        :type annotation_url: string
        :type whiteningOption: string
        :type targetScope: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = _generate_post_data(annotation, annotation_url, targetScope, whiteningOption)
        res = self.client.post(endpoint=MARK_AS_THREAT, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mark as threat, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def mark_as_benign(self, targetScope, annotation=None, annotation_url=None, whiteningOption=None,
                       query_filter=None, **threat_args):
        """
        Mark ``Threat`` as benign by filter with annotation 
        message/url (optional), default filter is empty.
        
        Scope level must be provided ("site", "tenant" or "group")
        
        Returns number of affected ``Threats``
        
        :type annotation: string
        :type annotation_url: string    
        :type whiteningOption: string
        :type targetScope: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = _generate_post_data(annotation, annotation_url, targetScope, whiteningOption)
        res = self.client.post(endpoint=MARK_AS_BENIGN, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to mark as benign, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
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

    def add_to_blacklist(self, targetScope, annotation=None, annotation_url=None, whiteningOption=None,
                         query_filter=None, **threat_args):
        """
        Add ``Threats`` hashes to blacklist by filter with annotation 
        message/url (optional), default filter is empty.
        
        Scope level must be provided ("site", "tenant" or "group")
        
        Returns number of affected ``Threats``
        :type annotation: string
        :type annotation_url: string
        :type whiteningOption: string
        :type targetScope: string
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        post_data = _generate_post_data(annotation, annotation_url, targetScope, whiteningOption)
        res = self.client.post(endpoint=ADD_TO_BLACKLIST, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to add to blacklist, response_code: {}".format(res.json))
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

    def update_threat(self, threat_id, annotation=None, annotation_url=None, query_filter=None, **threat_args):
        """
        Update a threat's annotation or annotation url

        :type threat_id: str
        :type annotation: str
        :type annotation_url: str
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :rtype: ManagementResponse
        """
        query_params = ThreatQueryFilter.get_query_params(query_filter, threat_args)
        data = dict()
        if annotation:
            data['annotation'] = annotation
        if annotation_url:
            data['annotation_url'] = annotation_url
        res = self.client.put(endpoint=UPDATE_THREAT.format(threat_id), data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warn("Failed to update threat, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_whitening_options(self, threat=None, threat_id=''):
        id = threat_id if threat_id else threat.id
        res = self.client.get(endpoint=WHITENING_OPTIONS.format(id))
        if res.status_code != 200:
            logger.warning("Failed to get whitening_options, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res


