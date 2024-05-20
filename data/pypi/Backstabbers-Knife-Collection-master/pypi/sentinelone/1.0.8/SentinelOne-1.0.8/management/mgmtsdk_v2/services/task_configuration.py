import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.task_configuration import TaskConfiguration
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('TaskConfiguration')


class TaskConfigurationQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'sortBy': ['eq'],
        'limit': ['eq'],
        'taskType': ['eq'],
        'skipCount': ['eq'],
        'sortOrder': ['eq'],
        'countOnly': ['eq'],
	'query': ['eq'],
    }

    def __init__(self):
        super(TaskConfigurationQueryFilter, self).__init__()


class TasksConfiguration(object):
    """Tasks Configuration service"""

    def __init__(self, client):
        self.client = client

    def get_task_configuration(self, query_filter=None, **task_args):
        """
        Return scope's task configuration

          :type query_filter: TaskConfigurationQueryFilter
          :type task_args: dict
          :rtype: ManagementResponse
        """
        query_params = TaskConfigurationQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=TASKS_TASK_CONFIGURATION, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get task configuration, response_code: {}".format(res.status_code))
            raise_from_response(res)
        # res.data = [TaskConfiguration(**task_config) for task_config in res.data]
        res.data = TaskConfiguration(**res.data)
        return res

    def update_task_configuration(self, data_config, query_filter=None, **task_args):
        """
        Update task configuration
          :type data_config: dict
          :type query_filter: TaskConfigurationQueryFilter
          :type task_args: dict
          :rtype: ManagementResponse
          """
        query_params = TaskConfigurationQueryFilter.get_query_params(query_filter, task_args)

        fields_to_ignore = ["taskType", "maintenanceConfigUpdatedAt", "maintenanceConfigUpdatedBy",
                            "concurrencyConfigUpdatedBy", "concurrencyConfigUpdatedAt", "parentMaxConcurrent"]
        cur_config = self.get_task_configuration(**task_args).data
        new_config = {}

        for key in cur_config.__dict__:
            if key not in fields_to_ignore:
                new_config[key] = cur_config.__dict__[key]

        for key, val in data_config.items():
            new_config[key] = val

        res = self.client.put(endpoint=TASKS_TASK_CONFIGURATION, data=new_config, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update task configuration, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = TaskConfiguration(**res.data)
        return res

    def has_explicit_subscope(self, query_filter=None, **task_args):
        """
        Return True if any scope under current scope have not inherit current scope task configuration

          :type query_filter: TaskConfigurationQueryFilter
          :type task_args: dict
          :rtype: ManagementResponse
        """
        query_params = TaskConfigurationQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=TASKS_GET_TASK_CONFIGURATION_HAS_EXPLICIT_SUBSCOPE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get task has explicit sub-scope, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_explicit_subscopes(self, query_filter=None, **task_args):
        """
        Return True if any scope under current scope have not inherit current scope task configuration

          :type query_filter: TaskConfigurationQueryFilter
          :type task_args: dict
          :rtype: ManagementResponse
        """
        query_params = TaskConfigurationQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=TASKS_GET_TASK_CONFIGURATION_EXPLICIT_SUBSCOPES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get task explicit sub-scopes, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
