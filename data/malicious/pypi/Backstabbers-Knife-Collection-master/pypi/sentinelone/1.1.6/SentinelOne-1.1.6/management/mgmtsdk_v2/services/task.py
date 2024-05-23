import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.task import Task
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Task')


class TaskQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'agentId': ['eq'],
        'ids': ['eq'],
        'status': ['eq'],
        'type': ['eq'],
        'text': ['eq'],
        'key': ['eq'],
        'query': ['eq'],
        'limit': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'description': ['contains'],
        'computerName': ['contains'],
        'uuid': ['contains'],
        'detailedStatus': ['contains'],
        'parentTaskId': ['in'],
        'initiatedBy': ['contains'],
        'createdAt': ['gt', 'lt', 'lte', 'gte'],
        'updatedAt': ['gt', 'lt', 'lte', 'gte'],
        'tenant': ['eq']
    }

    def __init__(self):
        super(TaskQueryFilter, self).__init__()


class Tasks(object):
    """Tasks service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **task_args):
        """
        Get list of ``Tasks`` from the console by filters, default filter is empty

        :type query_filter: TaskQueryFilter
        :type task_args: dict
        :rtype: ManagementResponse
        """
        query_params = TaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=TASKS_GET_TASKS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get tasks, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Task(**task) for task in res.data]
        return res

    def cancel(self, query_filter=None, **task_args):
        """
        Cancel tasks that haven not been sent to the endpoint.

        :type query_filter: TaskQueryFilter
        :type task_args: dict
        :rtype: ManagementResponse
        """
        query_params = TaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.post(endpoint=TASKS_CANCEL_TASK, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to cancel task, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_task_filters_count(self, query_filter=None, **task_args):
        query_params = TaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=TASKS_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get task filters-count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_task_free_text_filters(self):
        res = self.client.get(endpoint=TASKS_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get task free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def task_filters_auto_complete(self, key, text, query_filter=None, **task_args):
        query_params = TaskQueryFilter.get_query_params(query_filter, task_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=TASKS_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get task autocomplete filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def download_output_file(self, agent_id, task):
        data = {
            'agentId': agent_id,
            'siteId': task.siteId,
            'signature': task.signature,
            'signatureType': 'SHA256'
        }
        res = self.client.get(endpoint=TASKS_DOWNLOAD_OUTPUT_FILE, params=data)
        if res.status_code != 200:
            logger.warning(f"Failed to download output file (task id={task.id}) {res.status_code}")
            raise_from_response(res)
        return res
