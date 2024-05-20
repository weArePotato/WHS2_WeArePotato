import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.user import User
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('User')


class UserQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'allowRemoteShell': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'dateJoined': ['eq'],
        'email': ['eq'],
        'emailReadOnly': ['eq'],
        'emailVerified': ['eq'],
        'firstLogin': ['eq'],
        'fullName': ['eq'],
        'fullNameReadOnly': ['eq'],
        'groupIds': ['eq'],
        'groupsReadOnly': ['eq'],
        'ids': ['eq'],
        'lastLogin': ['eq'],
        'limit': ['eq'],
        'primaryTwoFaMethod': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'source': ['eq'],
        'twoFaEnabled': ['eq'],
        'username': ['eq'],
    }

    def __init__(self):
        super(UserQueryFilter, self).__init__()


class Users(object):
    """Users service"""

    def __init__(self, client):
        self.client = client

    def login_by_token(self, token):
        """
        :param token:
        :type token: string
        :return: token
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=LOGIN_BY_TOKEN, params={'token': token})
        if res.status_code != 200:
            logger.warning("Failed to login by token, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(token)
        res.data = token
        return res

    def login_by_api_token(self, api_token):
        """
        :param api_token:
        :type api_token: string
        :return: token
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=LOGIN_BY_API_TOKEN, data={'apiToken': api_token})
        if res.status_code != 200:
            logger.warning("Failed to login by api token, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(res.data['token'])  # TODO: Validate ret from console
        res.data = res.data['token']
        return res

    def auth_by_recovery_code(self, code):
        """
        :param code: recovery code
        :type code: string
        :return: login data
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=LOGIN_BY_RECOVERY_CODE, data={'code': code})
        if res.status_code != 200:
            logger.warning("Failed to auth by recovery code, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(res.data['token'])  # TODO: Validate ret from console
        return res

    def auth_with_app(self, code):
        """
        :param code: code
        :type code: string
        :return: login data
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=AUTH_WITH_APP, data={'code': code})
        if res.status_code != 200:
            logger.warning("Failed to auth with app, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(res.data['token'])
        return res

    def sign_in_with_eula(self):
        """
        :return: token
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=SIGN_IN_WITH_EULA)
        if res.status_code != 200:
            logger.warning("Failed to sign in with eula, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['token']
        return res

    def disable_2fa(self, user_id, two_fa_code=None, current_password=None):
        """
        :param user_id: id of user to disable 2fa for
        :type user_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {'id': user_id}
        if two_fa_code:
            data['twoFaCode'] = two_fa_code
        if current_password:
            data['currentPassword'] = current_password

        res = self.client.post(endpoint=DISABLE_TWO_FA, data=data)
        if res.status_code != 200:
            logger.warning("Failed to disable 2fa, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def enable_2fa(self, user_id, two_fa_code=None, current_password=None):
        """
        :param user_id: id of user to enable 2fa for
        :type user_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {'id': user_id}
        if two_fa_code:
            data['twoFaCode'] = two_fa_code
        if current_password:
            data['currentPassword'] = current_password

        res = self.client.post(endpoint=ENABLE_TWO_FA, data=data)
        if res.status_code != 200:
            logger.warning("Failed to enable 2fa, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def generate_recovery_codes(self):
        """
        :return: recovery codes
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=GENERATE_RECOVERY_CODES)
        if res.status_code != 200:
            logger.warning("Failed to generate recovery code, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['codes']
        return res

    def check_tenant_admin(self):
        """
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=CHECK_TENANT_ADMIN)
        if res.status_code != 200:
            logger.warning("Failed to check tenant admin, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def verify_code(self, user_id, verificationCode):
        """
        :param user_id:
        :type user_id: string
        :param verificationCode:
        :type verificationCode: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {'id': user_id, 'verificationCode': verificationCode}
        res = self.client.post(endpoint=VERIFY_CODE, data=data)
        if res.status_code != 200:
            logger.warning("Failed to verify code, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def generate_api_token(self):
        """
        :return: generated api token
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=GENERATE_API_TOKEN)
        if res.status_code != 200:
            logger.warning("Failed to generate api token, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['token']
        return res

    def check_viewer(self):
        """
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=CHECK_VIEWER_AUTH)
        if res.status_code != 200:
            logger.warning("Failed to check viewer, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def revoke_api_token(self, user_id):
        """
        :param user_id:
        :type user_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.post(endpoint=REVOKE_API_TOKEN, data={'id': user_id})
        if res.status_code != 200:
            logger.warning("Failed to revoke api token, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def change_password(self, user_id, current_password, new_password, confirm_new_password):
        """
        :param user_id:
        :type user_id: string
        :param current_password:
        :type current_password: string
        :param new_password:
        :type new_password: string
        :param confirm_new_password:
        :type confirm_new_password: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {
            'id': user_id,
            'currentPassword': current_password,
            'newPassword': new_password,
            'confirmNewPassword': confirm_new_password,
        }
        res = self.client.post(endpoint=CHANGE_PASSWORD, data=data)
        if res.status_code != 200:
            logger.warning("Failed to change password, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def delete_users(self, query_filter=None, **user_args):
        """
        :param query_filter: Query filter object
        :type query_filter: UserQueryFilter
        :param user_args: Key value with query filters
        :type user_args: **dict
        :return: success status
        :rtype: ManagementResponse
        """
        query_params = UserQueryFilter.get_query_params(query_filter, user_args)
        res = self.client.post(endpoint=DELETE_USERS, data={}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to delete user, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def request_2fa_app(self, current_password=None):
        """
        :return: 2FA app
        :rtype: ManagementResponse
        """
        payload = None
        if current_password:
            payload = {'currentPassword': current_password}
        res = self.client.post(endpoint=REQUEST_TWO_FA_APP, payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to request 2fa app, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def enable_2fa_app(self, code, id=None):
        """
        :param code:
        :type code: string
        :param id:
        :type id: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {'code': code}
        if id:
            data['id'] = id
        res = self.client.post(endpoint=ENABLE_TWO_FA_APP, data=data)
        if res.status_code != 200:
            logger.warning("Failed to enable 2fa app, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def login(self, username, password, rememberMe=None):
        """
        :param username:
        :type username: string
        :param password:
        :type password: string
        :param rememberMe:
        :type rememberMe: Boolean
        :return: login details
        :rtype: ManagementResponse
        """
        post_data = {'username': username, 'password': password}
        if rememberMe:
            post_data['rememberMe'] = rememberMe
        res = self.client.post(endpoint=LOGIN, payload=post_data)
        if res.status_code != 200:
            logger.warning("Failed to login, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(res.data['token'])
        res.data = res.data['token']
        return res

    def logout(self):
        res = self.client.post(endpoint=LOGOUT)
        if res.status_code != 200:
            logger.warning("Failed to logout, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_auth(token='')

    def get(self, query_filter=None, **user_args):
        """
        :param query_filter: Query filter object
        :type query_filter: UserQueryFilter
        :param user_args: Key value with query filters
        :type user_args: **dict
        :return: Users answering the query
        :rtype: ManagementResponse
        """
        query_params = UserQueryFilter.get_query_params(query_filter, user_args)
        ret = []
        res = self.client.get(endpoint='users', params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get users, response_code: {}".format(res.json))
            raise_from_response(res)
        users = res.data
        for user in users:
            ret.append(User(**user))
        res.data = ret
        return res

    def create(self, user):
        """
        :param user:
        :type user: User
        :return: created user
        :rtype: ManagementResponse
        """
        data = user.to_json()
        res = self.client.post(endpoint=CREATE_USER, data=data)
        if res.status_code != 200:
            logger.warning("Failed to create user, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = User(**res.data)
        return res

    def user_by_token(self, token):
        """
        :param token:
        :type token: string
        :return: user by it's token
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=USER_BY_TOKEN, params={'token': token})
        if res.status_code != 200:
            logger.warning("Failed to get user by token, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = User(**res.data)
        return res

    def auth_by_sso(self, scope_id):
        """
        :param scope_id:
        :type scope_id: string
        :return: response json
        """
        res = self.client.post(endpoint=AUTH_BY_SSO.format(scope_id))
        if res.status_code != 200:
            logger.warning("Failed to auth by sso, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def api_token_details(self, user_id):
        """
        :param user_id:
        :type user_id: string
        :return: api token details
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=API_TOKEN_DETAILS_FOR_USERS.format(user_id))
        if res.status_code != 200:
            logger.warning("Failed to get api token details, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def delete(self, user_id):
        """
        :param user_id:
        :type user_id: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_USER.format(user_id))
        if res.status_code != 200:
            logger.warning("Failed to delete user, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_user(self, user_id):
        """
        :param user_id:
        :param user_id: string
        :return: User answering the query
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_USER.format(user_id))
        if res.status_code != 200:
            logger.warning("Failed to get user by id, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = User(**res.data)
        return res

    def update(self, user_id, **kwargs):
        """
        :param user_id:
        :type user_id: string
        :return: updated user
        :rtype: ManagementResponse
        """
        user = self.get_user(user_id).data
        for key, val in kwargs.items():
            user.__setattr__(key, val)
        res = self.client.put(endpoint=UPDATE_USER.format(user_id), data=user.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update user, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = User(**res.data)
        return res

    def _update_auth(self, token):
        self.client.update_auth(token)

    def generate_iframe_token(self, account_id, role, agent_uuids=None, user_name=None):
        """
        :param account_id: the account id for the account user
        :param role: viewer/admin
        :param agent_uuids: agent_uuids to filter user by
        :param userName: userName the userName of the generated user

        :return: iframe token for created user
        """
        data = {'accountId': account_id, 'role': role}
        if agent_uuids:
            data['agentUuids'] = agent_uuids
        if user_name:
            data['userName'] = user_name
        res = self.client.post(endpoint=GENERATE_IFRAME_TOKEN, data=data)

        if res.status_code != 200:
            logger.warning("Failed to create iframe user, response_code: {}".format(res.json))
            raise_from_response(res)

        return res

    def login_by_iframe_user(self, iframe_token):
        res = self.client.post(endpoint=LOGIN_BY_IFRAME_USER, data={'iframeToken': iframe_token})
        if res.status_code != 200:
            logger.warning("Failed to login with iframe user, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_iframe_token(iframe_token, res.data['token'])
        return res

    def revoke_iframe_token(self, iframe_token):
        res = self.client.post(endpoint=REVOKE_IFRAME_TOKEN, data={'iframeToken': iframe_token})
        if res.status_code != 200:
            logger.warning("Failed to revoke iframe token, response_code: {}".format(res.json))
            raise_from_response(res)
        self.client.update_iframe_token(None, None)
        return res

    def get_iframe_token_details(self, iframe_token):
        res = self.client.post(endpoint=IFRAME_TOKEN_DETAILS, data={'iframeToken': iframe_token})
        if res.status_code != 200:
            logger.warning("Failed to revoke iframe token, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def send_verification_email(self, query_filter=None, **user_args):
        """
        :param query_filter: Query filter object
        :type query_filter: UserQueryFilter
        :param user_args: Key value with query filters
        :type user_args: **dict
        :return: success status
        :rtype: ManagementResponse
        """
        query_params = UserQueryFilter.get_query_params(query_filter, user_args)
        res = self.client.post(endpoint=SEND_VERIFICATION_EMAIL, data={}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to send verification email, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def validate_verification_token(self, token):
        """
        :param token:
        :type token: string
        :return: success status
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=VALIDATE_VERIFICATION_TOKEN, params={'token': token})
        if res.status_code != 200:
            logger.warning("Failed to validate verification token, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def verify_email(self, token, password):
        """
        :param token:
        :type token: string
        :param password:
        :type password: string
        :return: success status
        :rtype: ManagementResponse
        """
        data = {
            'token': token,
            'password': password,
        }
        res = self.client.post(endpoint=VERIFY_EMAIL, data=data)
        if res.status_code != 200:
            logger.warning("Failed to verify email, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_my_user(self):
        res = self.client.get(endpoint=MY_USER)
        if res.status_code != 200:
            logger.warning("Failed to get user by id, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = User(**res.data)

        return res

    def two_fa_reset(self, user_ids, query_filter=None, **filter_args):
        """
            Reset 2FA configuration for the user
        """
        body = {'ids': user_ids}
        query_params = UserQueryFilter.get_query_params(query_filter, filter_args)
        res = self.client.post(endpoint=RESET_2FA, data=body, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed save filter, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def update_2fa_email(self, user_id, email):
        """
        :param user_id:
        :type user_id: string
        :type email: string
        :return: updated user
        :rtype: ManagementResponse
        """
        data = {'email': email}
        res = self.client.put(endpoint=RECOVER_EMAIL.format(user_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to update 2fa email, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def verify_code_recovery_email(self, user_id, code):
        """
        :param user_id:
        :type user_id: string
        :type code: string
        :return: updated user
        :rtype: ManagementResponse
        """
        data = {'code': code}
        res = self.client.post(endpoint=VERIFY_RECOVER_EMAIL.format(user_id), data=data)
        if res.status_code != 200:
            logger.warning("Failed to verify code recovery email, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def send_code(self):
        res = self.client.post(endpoint=SEND_CODE)
        if res.status_code != 200:
            logger.warning("Failed to send code, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def verify_code_2fa(self, code):
        """
        :param user_id:
        :type code: string
        :return: updated user
        :rtype: ManagementResponse
        """
        data = {'code': code}
        res = self.client.post(endpoint=VERIFY_CODE_2FA, data=data)
        if res.status_code != 200:
            logger.warning("Failed to verify code, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def resend_recovery_email_code(self, user_id):
        res = self.client.post(endpoint=RESEND_RECOVERY_EMAIL.format(user_id))
        if res.status_code != 200:
            logger.warning("Failed to resend recovery email code, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
