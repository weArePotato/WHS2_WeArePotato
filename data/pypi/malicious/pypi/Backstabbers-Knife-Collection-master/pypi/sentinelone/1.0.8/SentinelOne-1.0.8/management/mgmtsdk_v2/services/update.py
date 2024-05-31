import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import DEPLOY_PACKAGE, \
    LATEST_PACKAGES_BY_OS, DELETE_PACKAGES, LATEST_PACKAGES, \
    UPLOAD_AGENT_PACKAGE, DOWNLOAD_PACKAGE, \
    DOWNLOAD_AGENT_PACKAGE, UPDATE_PACKAGE, UPLOAD_PACKAGE

from management.mgmtsdk_v2.entities.update import Package
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Update')


class UpdateQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'cursor': ['eq'],
        'fileExtension': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'osType': ['in'],
        'query': ['eq'],
        'sha1': ['eq'],
        'siteId': ['in'],
        'accountIds': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'status': ['eq'],
        'version': ['eq'],

    }

    def __init__(self):
        super(UpdateQueryFilter, self).__init__()


class UpdateByOsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'siteIds': ['eq'],
        'accountIds': ['eq'],
        'packageType': ['eq'],
    }

    def __init__(self):
        super(UpdateByOsQueryFilter, self).__init__()


class Updates(object):
    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **update_args):
        """
        :param query_filter: Query filter object
        :type query_filter: UpdateQueryFilter
        :param udpate_args: Key value with query filters
        :type udpate_args: **dict
        :return: Packages answering the query
        :rtype: ManagementResponse
        """
        query_params = UpdateQueryFilter.get_query_params(query_filter, update_args)
        res = self.client.get(endpoint=LATEST_PACKAGES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get packages, response_code: {}".format(res.status_code))
            return
        res.data = [Package(**pkg) for pkg in res.data]
        return res

    def upload_package(self, files):
        """
        :type files: dict of Multipart-Encoded Files
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=UPLOAD_PACKAGE, files=files)
        if res.status_code != 200:
            logger.warning("Failed to upload package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def deploy(self):
        """
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=DEPLOY_PACKAGE)
        if res.status_code != 200:
            logger.warning("Failed to deploy package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_by_os(self, query_filter=None, **update_args):
        """
        :param siteIds: list of site Ids
        :type: list
        :return: Packages grouped by os-type
        :rtype: ManagementResponse
        """
        query_params = UpdateByOsQueryFilter.get_query_params(query_filter, update_args)
        res = self.client.get(endpoint=LATEST_PACKAGES_BY_OS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get latest packages, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def delete(self, ids):
        """
        :param ids: package ids to delete
        :type ids: list
        :return: number of delete packages
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_PACKAGES, data={"ids": ids})
        if res.status_code != 200:
            logger.warning("Failed to delete packages, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data["affected"])
        return res

    def upload_agent_package(self, version, status, files, data=None):
        """
        :type version: string
        :type status: string
        :type files: dict of Multipart-Encoded Files
        :type data: dict of optional flags
        """
        if not data:
            data = dict()
        data['version'] = version
        data['status'] = status
        res = self.client.post(endpoint=UPLOAD_AGENT_PACKAGE, payload=data, files=files)
        if res.status_code != 200:
            logger.warning("Failed to upload package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def download_package(self, siteId, packageId, return_raw_response=False):
        """
        :param siteId: site id
        :type siteId: string
        :param packageId: package id
        :type packageId: string
        :param: package id
        :return: requested package
        :rtype: bytearray
        """
        res = self.client.get(endpoint=DOWNLOAD_PACKAGE.format(siteId, packageId), use_raw=True)
        if res.status_code != 200:
            logger.warning("Failed to download package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        if return_raw_response:
            return res
        return bytearray(res.content)

    def download_agent_package(self, packageId):
        """
        :param packageId: package id
        :type packageId: string
        :param: package id
        :return: requested package
        :rtype: bytearray
        """
        res = self.client.get(endpoint=DOWNLOAD_AGENT_PACKAGE.format(packageId), use_raw=True)
        if res.status_code != 200:
            logger.warning("Failed to download package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return bytearray(res.content)

    def update(self, packageId, data):
        """
        :param packageId: id of package to update
        :type packageId: string
        :param data: package details to update
        :type data: dict
        :return: updated Package
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=UPDATE_PACKAGE.format(packageId), data=data)
        if res.status_code != 200:
            logger.warning("Failed to update package, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Package(**res.data)
        return res
