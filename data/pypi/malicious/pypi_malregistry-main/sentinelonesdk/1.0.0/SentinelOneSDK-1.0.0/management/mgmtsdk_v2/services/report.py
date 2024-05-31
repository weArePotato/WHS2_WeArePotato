import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import GET_REPORTS, DELETE_REPORTS
from management.mgmtsdk_v2.entities.report import Report

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Threat')


class ReportQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gte', 'lte'],
        'cursor': ['eq'],
        'frequency': ['eq'],
        'fromDate': ['eq'],
        'groupId': ['eq'],
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
    }

    def __init__(self):
        super(ReportQueryFilter, self).__init__()


class Reports(object):

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **report_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ReportQueryFilter
        :param report_args: Key value with query filters
        :type report_args: **dict
        :return: Reports answering the query
        :rtype: ManagementResponse
        """
        ret = []
        query_params = ReportQueryFilter.get_query_params(query_filter, report_args)
        res = self.client.get(endpoint=GET_REPORTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get reports, response_code: {}".format(res.status_code))
            raise_from_response(res)
        reports = res.data
        for report in reports:
            ret.append(Report(**report))
        res.data = ret
        return res

    def delete(self, query_filter=None, **report_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ReportQueryFilter
        :param report_args: Key value with query filters
        :type report_args: **dict
        :return: Number of reports deleted
        :rtype: ManagementResponse
        """
        query_params = ReportQueryFilter.get_query_params(query_filter, report_args)
        res = self.client.post(endpoint=DELETE_REPORTS, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to delete reports, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data["affected"])
        return res
