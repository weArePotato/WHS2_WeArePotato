import logging

from management.common.query_filter import BaseScopeFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2_1.entities.app_management import get_risk_data_class


class AppManagement(object):
    """ Application management service """
    def __init__(self, client):
        self.client = client

    def init_scan(self, scope_filter=None, **scope_args):
        """
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :return: affected number
        :rtype: ManagementResponse
        """
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.post(endpoint=APP_SCAN, query_filter=query_params)
        if res.status_code != 200:
            logging.info(f"Failed to init app management scan, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_scan_status(self, scope_filter=None, **scope_args):
        """
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :return: risks scan status dict
        :rtype: ManagementResponse
        """
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=APP_SCAN_STATUS, params=query_params)
        if res.status_code != 200:
            logging.info(f"Failed to get app management scan status, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_risks(self, **params):
        res = self.client.get(endpoint=RISKS_GET, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get risks, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_risks_expanded(self, risk_id: str, scope_filter=None, **scope_args):
        """
        :param risk_id: risk id to expand
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :return: risks scan status dict
        :rtype: ManagementResponse
        """
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        query_params.update({'id': risk_id})
        res = self.client.get(endpoint=RISKS_EXPANDED, params=query_params)
        if res.status_code != 200:
            logging.info(f"Failed to get risks expanded for {risk_id}, response_code: {res.json}")
            raise_from_response(res)
        if res.data:
            res.data = [get_risk_data_class(**data) for data in res.data]
        return res

    def get_risks_filter_count(self, **params):
        res = self.client.get(endpoint=RISKS_FILTERS_COUNT, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get risks filters count, response_code: {res.json}")
            raise_from_response(res)
        return res

    def export_risks(self, **params):
        res = self.client.get(endpoint=RISKS_EXPORT, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to export risks, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_inventory(self, **params):
        res = self.client.get(endpoint=INVENTORY_GET, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get inventory, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_inventory_filter_count(self, **params):
        res = self.client.get(endpoint=INVENTORY_FILTERS_COUNT, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get inventory filters count, response_code: {res.json}")
            raise_from_response(res)
        return res

    def export_inventory(self, **params):
        res = self.client.get(endpoint=INVENTORY_EXPORT, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to export inventory, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_inventory_versions_count(self, app_name, app_vendor, scope_filter=None, **scope_args):
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        query_params.update({'applicationName': app_name, 'applicationVendor': app_vendor})
        res = self.client.get(endpoint=INVENTORY_VERSIONS_COUNT, params=query_params)
        if res.status_code != 200:
            logging.info(f"Failed to get inventory versions count, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_inventory_endpoints(self, app_name, app_vendor, **params):
        params.update({'applicationName': app_name, 'applicationVendor': app_vendor})
        res = self.client.get(endpoint=INVENTORY_ENDPOINTS, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get inventory endpoints, response_code: {res.json}")
            raise_from_response(res)
        return res
