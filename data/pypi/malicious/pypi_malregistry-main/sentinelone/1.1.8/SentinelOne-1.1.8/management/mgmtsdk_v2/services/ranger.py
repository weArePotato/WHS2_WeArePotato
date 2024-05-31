import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.ranger import Gateway
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Ranger')


class RangerFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'tenant': ['eq'],
        'osType': ['eq', 'in'],
        'osName': ['eq'],
        'osVersion': ['eq', 'contains'],
        'localIp': ['eq', 'contains'],
        'externalIp': ['eq', 'contains'],
        'ids': ['eq'],
        'snapshotIds': ['eq'],
        'deviceType': ['eq', 'in'],
        'macAddress': ['eq', 'contains'],
        'gatewayMacAddress': ['eq', 'contains'],
        'firstSeen':  ['gt', 'gte', 'lt', 'lte', 'between'],
        'lastSeen':  ['gt', 'gte', 'lt', 'lte', 'between'],
        'agentIds': ['eq'],
        'managedState': ['eq'],
        'managedStates': ['eq'],
        'manufacturer': ['eq', 'contains'],
        'discoveryMethods': ['eq'],
        'hostnames': ['eq', 'contains'],
        'subnetAddress': ['contains'],
        'tcpPorts': ['contains'],
        'udpPorts': ['contains'],
        'query': ['eq'],
        'limit': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'countOnly': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'period': ['eq'],
    }

    def __init__(self):
        super(RangerFilter, self).__init__()


class RangerGatewayFilter(QueryFilter):

    QUERY_ARGS = {
        'externalIp': ['eq', 'contains'],
        'limit': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'countOnly': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'macAddress': ['eq', 'contains'],
        'ip': ['eq', 'contains'],
        'ids': ['eq'],
        'allowScan': ['eq'],
        'agentPercentage': ['gt', 'gte', 'lt', 'lte', 'between'],
        'numberOfAgents': ['gt', 'gte', 'lt', 'lte', 'between'],
        'numberOfRangers': ['gt', 'gte', 'lt', 'lte', 'between'],
        'totalAgents': ['gt', 'gte', 'lt', 'lte', 'between'],
        'createdAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'manufacturer': ['eq', 'contains'],
        'allowedScanners': ['contains'],
        'query': ['eq'],
        'tcpPorts': ['contains'],
        'udpPorts': ['contains'],
        'accountIds': ['eq'],
        'snmpScan': ['eq'],
        'mdnsScan': ['eq'],
        'rdnsScan': ['eq'],
        'smbScan': ['eq'],
        'icmpScan': ['eq'],
        'new': ['eq'],
        'archived': ['eq'],
        'scanOnlyLocalSubnets': ['eq'],
    }

    def __init__(self):
        super(RangerGatewayFilter, self).__init__()


class Ranger(object):
    """Ranger service"""

    def __init__(self, client):
        self.client = client

    def get_device_inventory_table_view(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_DEVICE_INVENTORY_TABLE_VIEW, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get inventory table view, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_ranger_filters_count(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get ranger filters-count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_gateway_filters_count(self, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=GATEWAY_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get gateway filters-count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_device_inventory(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_EXPORT_DEVICE_INVENTORY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to export ranger data to csv, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_ranger_free_text_filters(self):
        res = self.client.get(endpoint=RANGER_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get ranger free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_gateway_free_text_filters(self):
        res = self.client.get(endpoint=GATEWAY_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get gateway free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def ranger_filters_auto_complete(self, key, text, query_filter=None, **agent_args):
        query_params = RangerFilter.get_query_params(query_filter, agent_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=RANGER_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get ranger autocomplete filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def gateway_filters_auto_complete(self, key, text, query_filter=None, **agent_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, agent_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=GATEWAY_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get gateway autocomplete filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_raw_json(self, inventory_id):
        res = self.client.get(endpoint=RANGER_GET_ROW_JSON.format(inventory_id))
        if res.status_code != 200:
            logger.warning("Failed to get ranger raw data, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_raw_data(self, inventory_id):
        res = self.client.get(endpoint=RANGER_RAW_DATA_EXPORT.format(inventory_id))
        if res.status_code != 200:
            logger.warning("Failed to export ranger raw data, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_snapshot_status(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_GET_SNAPSHOT_STATUS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get snapshot status, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_latest_snapshot(self):
        res = self.client.get(endpoint=RANGER_GET_LATEST_SNAPSHOT)
        if res.status_code != 200:
            logger.warning("Failed to get latest snapshot, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_gateways(self, gateway_filter=None, **gateway_args):
        query_params = RangerGatewayFilter.get_query_params(gateway_filter, gateway_args)
        ret = list()
        res = self.client.get(endpoint=RANGER_GET_GATEWAYS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get gateways, response_code: {}".format(res.status_code))
            raise_from_response(res)
        gateways = res.data
        for gateway in gateways:
            ret.append(Gateway(**gateway))
        res.data = ret
        return res

    def update_gateway(self, account_id, gateway_id, **kwargs):
        gateway = self.get_gateways(accountIds=account_id, ids=gateway_id).data[0]
        for key, val in kwargs.items():
            gateway.__setattr__(key, val)
        res = self.client.put(endpoint=RANGER_UPDATE_GATEWAY.format(gateway_id), data=gateway.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update gateway, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Gateway(**res.data)
        return res

    def update_gateways(self, allowscan, archived, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.post(endpoint=RANGER_UPDATE_GATEWAYS, data={'allowScan': allowscan, 'archived': archived},
                               payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning("Failed to update gateways, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def get_ranger_settings(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_GET_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get ranger settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def update_ranger_settings(self, account_ids, **kwargs):
        res = self.client.put(endpoint=RANGER_UPDATE_SETTINGS, query_filter={'accountIds': account_ids}, data=kwargs)
        if res.status_code != 200:
            logger.warning("Failed to update ranger settings, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_ranger_network_dashboard(self, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_NETWORK_DASHBOARD, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get ranger network dashboard, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_subnet_scan_data(self, account_id, **params):
        params['accountIds'] = [account_id]
        res = self.client.get(endpoint=RANGER_SUBNET_SCAN_DATA, params=params)
        if res.status_code != 200:
            logger.warning("Failed to get ranger subnet scan data, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
