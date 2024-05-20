import logging

from management.common.query_filter import QueryFilter, FullScopeFilter
from management.mgmtsdk_v2.endpoints import GET_REPORTS_TASKS, \
    DELETE_REPORT_TASKS, CREATE_REPORT_TASK, UPDATE_REPORT_TASK
from management.mgmtsdk_v2.entities.report_task import ReportTask

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('ReportTask')


class ReportTaskQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gt', 'gte', 'lt', 'lte'],
        'cursor': ['eq'],
        'frequency': ['eq'],
        'fromDate': ['eq'],
        'groupIds': ['eq'],
        'id': ['eq'],
        'ids': ['eq'],
        'interval': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'query': ['eq'],
        'scheduleType': ['eq'],
        'scope': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'taskId': ['eq'],
        'toDate': ['eq'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte'],
    }

    def __init__(self):
        super(ReportTaskQueryFilter, self).__init__()


class ReportTasks(object):

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **task_args):
        """
        :optional: list of query filters
        :return: List of ReportTask objects
        """
        ret = []
        query_params = ReportTaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=GET_REPORTS_TASKS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get report tasks, response_code: {}".format(res.status_code))
            raise_from_response(res)
        report_tasks = res.data
        for report_task in report_tasks:
            ret.append(ReportTask(**report_task))
        res.data = ret
        return res

    def delete(self, query_filter=None, **task_args):
        """
        :optional: list of query filters
        :return: ReportTasks deleted
        """
        query_params = ReportTaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.post(endpoint=DELETE_REPORT_TASKS, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to delete report tasks, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data["affected"])
        return res

    def create(self, report_task, query_filter=None, **task_args):
        query_params = FullScopeFilter.get_query_params(query_filter, task_args)
        res = self.client.post(endpoint=CREATE_REPORT_TASK, query_filter=query_params, data=report_task.to_json())
        if res.status_code != 200:
            logger.warning("Failed to create report task, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update(self, taskId, **data):
        res = self.client.put(endpoint=UPDATE_REPORT_TASK.format(taskId), data=data)
        if res.status_code != 200:
            logger.warning("Failed to update report task, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = ReportTask(**res.data)
        return res
