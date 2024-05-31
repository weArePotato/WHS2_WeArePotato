import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.config_override import ConfigOverride

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('ConfigOverride')


class ConfigOverrideQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'agentIds': ['eq'],
        'agentVersions': ['eq'],
        'cursor': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'description': ['like'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'name': ['like'],
        'osTypes': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'tenant': ['eq'],
        'versionOption': ['eq']
    }

    def __init__(self):
        super(ConfigOverrideQueryFilter, self).__init__()


class ConfigOverrides(object):
    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **conf_over_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ConfigOverrideQueryFilter
        :param conf_over_args: Key value with query filters
        :type conf_over_args: **dict
        :return: config overrides answer the query
        :rtype: ManagementResponse
        """
        query_params = ConfigOverrideQueryFilter.get_query_params(query_filter, conf_over_args)
        ret = list()
        res = self.client.get(endpoint=CONFIG_OVERRIDE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get config_overrides, response_code: {}".format(res.json))
            raise_from_response(res)
        conf_overs = res.data
        for conf_over in conf_overs:
            ret.append(ConfigOverride(**conf_over))
        res.data = ret
        return res

    def create(self, config_override):
        """
        :param config_override: config to override policy
        :type config_override: ConfigOverride
        :return: created ConfigOverride
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=CONFIG_OVERRIDE, data=config_override.to_json())
        if res.status_code != 200:
            logger.warning("Failed to create config_override, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = ConfigOverride(**res.data)
        return res

    def delete(self, conf_over_id):
        """
        :param conf_over_id:
        :type conf_over_id: string
        :return: response json
        """
        res = self.client.delete(endpoint=DELETE_CONFIG_OVERRIDE.format(conf_over_id))
        if res.status_code != 200:
            logger.warning("Failed to delete config_override, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def update(self, config_override):
        """
        :param config_override: configOverride to update
        :type config_override: ConfigOverride
        :return: updated ConfigOverride
        :rtype: ManagementRespons
        """
        res = self.client.put(endpoint=UPDATE_CONFIG_OVERRIDE.format(config_override.id),
                              data=config_override.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update config_override, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = ConfigOverride(**res.data)
        return res
