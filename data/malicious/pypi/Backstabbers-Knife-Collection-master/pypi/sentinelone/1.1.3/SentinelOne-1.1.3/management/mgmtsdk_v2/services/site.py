import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.policy import Policy
from management.mgmtsdk_v2.entities.site import Site
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Site')


class SiteQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountId': ['eq'],
        'accountIds': ['eq'],
        'activeLicenses': ['eq'],
        'adminOnly': ['eq'],
        'availableMoveSites': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['eq'],
        'cursor': ['eq'],
        'expiration': ['eq'],
        'externalId': ['eq'],
        'features': ['eq'],
        'healthStatus': ['eq'],
        'isDefault': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'query': ['eq'],
        'registrationToken': ['eq'],
        'siteIds': ['eq'],
        'siteType': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'states': ['eq'],
        'suite': ['eq'],
        'totalLicenses': ['eq'],
        'updatedAt': ['eq'],
    }

    def __init__(self):
        super(SiteQueryFilter, self).__init__()


class Sites(object):
    """Sites service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **site_args):
        """
        :param query_filter: Query filter object
        :type query_filter: SiteQueryFilter
        :param site_args: Key value with query filters
        :type site_args: **dict
        :return: Sites answering the query
        :rtype: ManagementResponse
        """
        query_params = SiteQueryFilter.get_query_params(query_filter, site_args)
        ret = []
        res = self.client.get(endpoint=GET_SITES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get sites, response_code: {}".format(res.status_code))
            raise_from_response(res)
        sites = res.data['sites']
        for site in sites:
            ret.append(Site(**site))
        res.data = ret
        return res

    def get_by_id(self, site_id):
        """
        :param site_id:
        :type site_id: string
        :return: Site with provided id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_SITE_BY_ID.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to get site by id, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def create(self, site):
        """
        :param site: Site object to create
        :type site: Site
        :return: created site
        :rtype: ManagementResponse
        """
        data = site.to_json()
        res = self.client.post(endpoint=CREATE_SITE, data=data)
        if res.status_code != 200:
            logger.warning("Failed to create site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def regenerate_key(self, site_id):
        """
        :param site_id:
        :type site_id: string
        :return: new registration token
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=REGENERATE_SITE_KEY.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to regenerate key for site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['registrationToken']
        return res

    def revert_policy(self, site_id):
        """
        :param site_id:
        :type site_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=REVERT_SITE_POLICY.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to revert policy site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update(self, site_id, **kwargs):
        """
        :param site_id:
        :type site_id: string
        :param kwargs:
        :type kwargs: **dict
        :return: updated site
        :rtype Site
        """
        site = self.get_by_id(site_id).data
        for key, val in kwargs.items():
            site.__setattr__(key, val)
            if 'licenses' not in kwargs:  # returned licenses not equals to what we need to send, so we removing returned if we not sending licenses dict
                site.licenses = None
        res = self.client.put(endpoint=UPDATE_SITE.format(site_id), data=site.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def create_with_admin(self, site, user):
        """
        :param site: site to create
        :type site: Site
        :param user: user to created as admin for site
        :type user: User
        :return: created site, contained user
        :rtype Site
        """
        data = site.to_json()
        data['user'] = user.to_json()
        res = self.client.post(endpoint=CREATE_WITH_ADMIN, data=data)
        if res.status_code != 200:
            logger.warning("Failed to create site with admin, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def update_policy(self, site_id, **kwargs):
        """
        :param site_id:
        :type site_id: string
        :param kwargs: policy fields to update for site
        :type kwargs: **dict
        :return: updated site's policy
        :rtype: ManagementResponse
        """
        policy = self.get_policy(site_id).data
        policy_dict = policy.to_json()
        policy_dict.update(kwargs)
        res = self.client.put(endpoint=UPDATE_SITE_POLICY.format(site_id), data=policy_dict)
        if res.status_code != 200:
            logger.warning("Failed to update site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get_policy(self, site_id):
        """
        :param site_id:
        :type site_id:
        :return: policy of site by given site_id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_SITE_POLICY.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to get site policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def delete(self, site_id):
        """
        :param site_id:
        :type site_id: string
        :return: Site with provided id
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_SITE.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to delete site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def reactivate(self, site_id, unlimited=None, expiration=None):
        """
        :param unlimited:
        :param expiration:
        :param site_id:
        :type site_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = dict()
        if unlimited:
            data['unlimited'] = unlimited
        if expiration:
            data['expiration'] = expiration
        res = self.client.put(endpoint=REACTIVATE_SITE.format(site_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to reactivate site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def expire(self, site_id):
        """
        :param site_id:
        :type site_id: string
        :return: Site with provided id
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=EXPIRE_SITE.format(site_id))
        if res.status_code != 200:
            logger.warning("Failed to expire site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def duplicate(self, **kwargs):
        res = self.client.post(endpoint=DUPLICATE_SITE, data=kwargs)
        if res.status_code != 200:
            logger.warning("Failed to duplicate site, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Site(**res.data)
        return res

    def update_bulk(self, site_ids, query_filter=None, description=None, unlimited_expiration=None, site_type=None,
                    inherits=None, expiration=None, licenses=None):
        """
        :param description:
        :param unlimited_expiration:
        :param site_type:
        :param inherits:
        :param expiration:
        :param licenses:
        :param site_ids:
        :type site_ids: list
        :return: affected
        :rtype: ManagementResponse
        """
        data = dict()
        if description:
            data['description'] = description
        if site_type:
            data['siteType'] = site_type
        if unlimited_expiration:
            data['unlimitedExpiration'] = unlimited_expiration
        if inherits:
            data['inherits'] = inherits
        if expiration:
            data['expiration'] = expiration
        if licenses:
            data['licenses'] = licenses

        query_params = SiteQueryFilter.get_query_params(query_filter, {'siteIds': site_ids})
        res = self.client.put(endpoint=SITES_BULK_UPDATE, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update bulk sites: {}".format(res.status_code))
        return res.data

