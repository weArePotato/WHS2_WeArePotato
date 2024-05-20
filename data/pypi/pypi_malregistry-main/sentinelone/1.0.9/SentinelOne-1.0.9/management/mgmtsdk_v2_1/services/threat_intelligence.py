import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import THREAT_INTELLIGENCE
from management.mgmtsdk_v2_1.entities.threat_intelligence import Ioc

logger = logging.getLogger('TI')


class IocQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'name': ['contains'],
        'uuids': ['eq'],
        'batchId': ['eq'],
        'externalId': ['eq'],
        'source': ['eq'],
        'type': ['eq'],
        'value': ['eq'],
        'method': ['eq'],
        'category': ['in'],
        'patternType': ['eq'],
        'pattern': ['eq'],
        'creationTime': ['gte', 'lte', 'gt', 'lt', 'between'],
        'createdAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'creator': ['contains'],
        'reference': ['eq'],
        'description': ['contains'],
        'accountIds': ['eq'],
        'tenant': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'updatedAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'limit': ['eq'],
        'skipCount': ['eq'],
        'skip': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq']
    }

    def __init__(self):
        super(IocQueryFilter, self).__init__()


class Threat_Intel(object):
    def __init__(self, client):
        self.client = client

    def create_or_update_ioc(self, iocs, query_filter=None, **ioc_args):
        query_params = IocQueryFilter.get_query_params(query_filter, ioc_args)
        if not query_params:
            query_params = {'tenant': 'true'}
        if type(iocs) == list:
            data = [current_ioc.to_json() for current_ioc in iocs]
        else:
            data = [iocs.to_json()]
            logger.info(f'Creating/updating the following IOC: {data}')
        res = self.client.post(endpoint=THREAT_INTELLIGENCE, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create/update IOC, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)

        return [Ioc(randomize_empty=False, **ioc) for ioc in res.data]

    def get_ioc(self, query_filter=None, **ioc_args):
        query_params = IocQueryFilter.get_query_params(query_filter, ioc_args)
        if not query_params:
            query_params = {'tenant': 'true'}
        res = self.client.get(endpoint=THREAT_INTELLIGENCE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get IOC, response_code: {}".format(res.status_code))
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)

        res.data = [Ioc(randomize_empty=False, **ioc) for ioc in res.data]
        return res

    def delete_ioc(self, query_filter=None, **ioc_args):
        query_params = IocQueryFilter.get_query_params(query_filter, ioc_args)

        res = self.client.delete(endpoint=THREAT_INTELLIGENCE, payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning(f"Failed to delete IOC, response_code: {res.status_code}")
            logger.warning(f"Error: {res.errors}")
            raise_from_response(res)

        return res.data['affected']
