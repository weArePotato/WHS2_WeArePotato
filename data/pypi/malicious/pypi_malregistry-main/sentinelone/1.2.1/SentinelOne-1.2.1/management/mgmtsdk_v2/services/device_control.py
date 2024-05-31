import logging

from management.common.query_filter import QueryFilter, FullScopeFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.device_control import Rule, DeviceEvent
from management.mgmtsdk_v2.exceptions import raise_from_response, SentinelBaseException

logger = logging.getLogger('DeviceControl')


class ReorderFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'interface': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(ReorderFilter, self).__init__()


class DeviceControlQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'action': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte'],
        'cursor': ['eq'],
        'deviceClass': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'interface': ['eq'],
        'interfaces': ['eq'],
        'limit': ['eq'],
        'query': ['eq'],
        'osType': ['eq'],
        'productId': ['eq'],
        'ruleName': ['eq'],
        'scopes': ['eq'],
        'serviceClass': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'status': ['eq'],
        'tenant': ['eq'],
        'uId': ['eq'],
        'vendorId': ['eq'],
    }

    def __init__(self):
        super(DeviceControlQueryFilter, self).__init__()


class EventQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'deviceClasses': ['eq'],
        'eventIds': ['eq'],
        'eventTime': ['gt', 'gte', 'lt', 'lte', 'between'],
        'eventTypes': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'interfaces': ['eq'],
        'limit': ['eq'],
        'productIds': ['eq'],
        'query': ['eq'],
        'serviceClasses': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipOnly': ['eq'],
        'sortOrder': ['eq'],
        'sortBy': ['eq'],
        'tenant': ['eq'],
        'uIds': ['eq'],
        'vendorIds': ['eq'],
    }

    def __init__(self):
        super(EventQueryFilter, self).__init__()


class DeviceControl(object):

    def __init__(self, client):
        self.client = client

    def create_rule(self, rule, query_filter=None, **rule_args):
        query_params = FullScopeFilter.get_query_params(query_filter, rule_args)
        res = self.client.post(endpoint=DEVICE_CONTROL, query_filter=query_params, data=rule.to_json())
        if res.status_code != 200:
            logger.warning("Failed to create rule, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Rule(**res.data)
        return res

    def get_rules(self, query_filter=None, **rule_args):
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        ret = []
        res = self.client.get(endpoint=DEVICE_CONTROL, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get rules, response_code: {}".format(res.status_code))
            raise_from_response(res)
        rules = res.data
        for rule in rules:
            ret.append(Rule(**rule))
        res.data = ret
        return res

    def delete_rules(self, query_filter=None, **rule_args):  # delete
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        res = self.client.delete(endpoint=DEVICE_CONTROL, data={}, payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning("Failed to delete rules, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def get_interfaces(self):
        res = self.client.get(endpoint=DEVICE_CONTROL_INTERFACES)
        if res.status_code != 200:
            logger.warning("Failed to get interfaces, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def reorder_rules(self, reordered_ids_list, scope_filter=None, **scope_args):
        query_params = ReorderFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=DEVICE_CONTROL_REORDER, data=reordered_ids_list, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to reorder rules, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update_rule(self, rule_id, tenant=False, accountIds=None, siteIds=None, groupIds=None, **kwargs):
        if siteIds:
            rule = self.get_rules(ids=rule_id, siteIds=siteIds).data[0].to_json()
        elif accountIds:
            rule = self.get_rules(ids=rule_id, accountIds=accountIds).data[0].to_json()
        elif groupIds:
            rule = self.get_rules(ids=rule_id, groupIds=groupIds).data[0].to_json()
        elif tenant is True:
            rule = self.get_rules(ids=rule_id, tenant=True).data[0].to_json()
        else:
            raise SentinelBaseException('Scope info not provided')
        rule.update(kwargs)
        res = self.client.put(endpoint=DEVICE_CONTROL_UPDATE_RULE.format(rule_id), data=rule)
        if res.status_code != 200:
            logger.warning("Failed to update rule, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Rule(**res.data)
        return res

    def count_by_filters(self, query_filter=None, **rule_args):
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        res = self.client.get(endpoint=DEVICE_CONTROL_PRIVATE_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to count agents, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_settings(self, scope_filter=None, **scope_args):
        query_params = FullScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=DEVICE_CONTROL_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get settings, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def update_settings(self, filter=None, **kwargs):
        res = self.client.put(endpoint=DEVICE_CONTROL_SETTINGS, query_filter=filter, data=kwargs)
        if res.status_code != 200:
            logger.warning("Failed to update settings, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def copy_rules(self, data, query_filter=None, **rule_args):
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        res = self.client.post(endpoint=DEVICE_CONTROL_COPY_RULES, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed to copy rule, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def move_rules(self, data, query_filter=None, **rule_args):
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        res = self.client.post(endpoint=DEVICE_CONTROL_MOVE_RULES, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed to move rules, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def change_rules_status(self, status, query_filter=None, **rule_args):
        query_params = DeviceControlQueryFilter.get_query_params(query_filter, rule_args)
        res = self.client.put(endpoint=DEVICE_CONTROL_STATUS, query_filter=query_params, data={'status': status})
        if res.status_code != 200:
            logger.warning("Failed to change rules status, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def get_events(self, query_filter=None, **event_args):
        query_params = EventQueryFilter.get_query_params(query_filter, event_args)
        ret = []
        res = self.client.get(endpoint=DEVICE_CONTROL_EVENTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get rules, response_code: {}".format(res.status_code))
            raise_from_response(res)
        events = res.data
        for event in events:
            ret.append(DeviceEvent(**event))
        res.data = ret
        return res
