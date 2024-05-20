import logging

from management.mgmtsdk_v2.entities.policy import Policy

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.account import Account
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Account')


class AccountQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountId': ['eq'],
        'accountType': ['eq'],
        'activeLicenses': ['eq'],
        'adminOnly': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['gte', 'lte', 'gt', 'lt', 'between'],
        'cursor': ['eq'],
        'expiration': ['eq'],
        'features': ['eq'],
        'ids': ['eq'],
        'isDefault': ['eq'],
        'limit': ['eq'],
        'name': ['eq'],
        'query': ['eq'],
        'accountIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'state': ['eq'],
        'states': ['eq'],
        'suite': ['eq'],
        'totalLicenses': ['eq'],
        'updatedAt': ['gte', 'lte', 'gt', 'lt', 'between'],
    }

    def __init__(self):
        super(AccountQueryFilter, self).__init__()


class Accounts(object):
    """Accounts service"""

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **account_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AccountQueryFilter
        :param account_args: Key value with query filters
        :type account_args: **dict
        :return: Accounts answering the query
        :rtype: ManagementResponse
        """
        query_params = AccountQueryFilter.get_query_params(query_filter, account_args)
        ret = []
        res = self.client.get(endpoint=GET_ACCOUNTS_PRIVATE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get accounts, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for account in res.data:
            ret.append(Account(**account))
        res.data = ret
        return res

    def create(self, account):
        """
        :param account: Account object to create
        :type account: Account
        :return: created account
        :rtype: ManagementResponse
        """
        data = account.to_json()
        res = self.client.post(endpoint=ACCOUNTS, data=data)
        if res.status_code != 200:
            logger.warning("Failed to create account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Account(**res.data)
        return res

    def create_with_admin(self, account, user):
        """
        :param account: account to create
        :type account: Account
        :param user: user to created as admin for account
        :type user: User
        :return: created account, contained user
        :rtype Account
        """
        data = account.to_json()
        data['user'] = user.to_json()
        res = self.client.post(endpoint=ACCOUNT_WITH_ADMIN, data=data)
        if res.status_code != 200:
            logger.warning("Failed to create account with admin, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Account(**res.data)
        return res

    def get_account(self, query_filter=None, **account_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AccountQueryFilter
        :param account_args: Key value with query filters
        :type account_args: **dict
        :return: Accounts answering the query
        :rtype: ManagementResponse
        """
        query_params = AccountQueryFilter.get_query_params(query_filter, account_args)
        ret = []
        res = self.client.get(endpoint=ACCOUNTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get accounts, response_code: {}".format(res.status_code))
            raise_from_response(res)
        for account in res.data:
            ret.append(Account(**account))
        res.data = ret
        return res

    def revert_policy(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=ACCOUNT_REVERT_POLICY.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to revert account policy response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_by_id(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return: Account with provided id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=ACCOUNT_SPECIFIC.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to get account by id, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Account(**res.data)
        return res

    def update(self, account_id, **kwargs):
        """
        :param account_id:
        :type account_id: string
        :param kwargs:
        :type kwargs: **dict
        :return: updated account
        :rtype Account
        """
        account = self.get_by_id(account_id).data
        account_id = account.id
        for key, val in kwargs.items():
            account.__setattr__(key, val)
        if 'licenses' not in kwargs:  # returned licenses not equals to what we need to send, so we removing returned if we not sending licenses dict
            account.licenses = None
        if 'skus' not in kwargs:  # returned skus may be affected by licenses, so we removing returned if we not sending skus dict
            account.skus = None

        data = account.to_json()
        data['id'] = account_id
        res = self.client.put(endpoint=ACCOUNT_SPECIFIC.format(account_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to update account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Account(**res.data)
        return res

    def delete(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return: Account with provided id
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=ACCOUNT_SPECIFIC.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to delete account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def reactivate(self, account_id, unlimited=None, expiration=None):
        """
        :param unlimited:
        :param expiration:
        :param account_id:
        :type account_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = dict()
        if unlimited:
            data['unlimited'] = unlimited
        if expiration:
            data['expiration'] = expiration
        res = self.client.put(endpoint=ACCOUNT_REACTIVATE.format(account_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to reactivate account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def expire(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return: Account with provided id
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=ACCOUNT_EXPIRE_NOW.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to expire account, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Account(**res.data)
        return res

    def update_policy(self, account_id, **kwargs):
        """
        :param account_id:
        :type account_id: string
        :param kwargs: policy fields to update for account
        :type kwargs: **dict
        :return: updated account's policy
        :rtype: ManagementResponse
        """
        policy = self.get_policy(account_id).data
        policy_dict = policy.to_json()
        policy_dict.update(kwargs)
        res = self.client.put(endpoint=UPDATE_ACCOUNT_POLICY.format(account_id), data=policy_dict)
        if res.status_code != 200:
            logger.warning("Failed to update account policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get_policy(self, account_id):
        """
        :param account_id:
        :type account_id:
        :return: policy of account by given account_id
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_ACCOUNT_POLICY.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to get account policy, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def generate_uninstall_password(self, account_id, expiration):
        """
        :param account_id:
        :type account_id: string
        :return expiration, version, last_revoked:
        :rtype ManagementResponse:
        """
        logging.info(f'generating uninstall-password for account:{account_id} with expiration:{expiration}')

        data = {'expiration': expiration}
        res = self.client.post(endpoint=GENERATE_UNINSTALL_PASSWORD.format(account_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to generate_uninstall_password, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get_uninstall_password_details(self, account_id, expiration):
        """
        :param account_id, expiration:
        :type account_id: string
        :type expiration: string yyyy-mm-dd
        :return expiration, version:
        :rtype ManagementResponse:
        """
        logging.info(f'get uninstall-password-details for account:{account_id} with expiration:{expiration}')

        data = {'expiration': expiration}
        res = self.client.get(endpoint=GET_UNINSTALL_PASSWORD_DETAILS.format(account_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to get uninstall_password_details, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get_uninstall_password(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return password:
        :rtype ManagementResponse:
        """
        logging.info(f'get uninstall-password for account:{account_id}')

        res = self.client.get(endpoint=GET_UNINSTALL_PASSWORD.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to get uninstall_password, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def revoke_uninstall_password(self, account_id):
        """
        :param account_id:
        :type account_id: string
        :return expiration, version, last_revoked:
        :rtype ManagementResponse:
        """
        logging.info(f'revoking uninstall-password for account:{account_id}')

        res = self.client.post(endpoint=REVOKE_UNINSTALL_PASSWORD.format(account_id))
        if res.status_code != 200:
            logger.warning("Failed to revoke_uninstall_password, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res
