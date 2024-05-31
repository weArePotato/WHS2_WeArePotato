import logging

from management.common.query_filter import HighScopeFilter, QueryFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.settings import Syslog, NotificationRecipient, SmsSmtp, Sso
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Site')


class NotificationRecipientsQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'email': ['eq'],
        'name': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
        'sms': ['eq'],
    }

    def __init__(self):
        super(NotificationRecipientsQueryFilter, self).__init__()


class Settings(object):

    def __init__(self, client):
        self.client = client

    def set_syslog(self, syslog, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=SYSLOG, data=syslog.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set syslog settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Syslog(**res.data)
        return res

    def get_syslog(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=SYSLOG, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set syslog settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Syslog(**res.data)
        return res

    def test_syslog(self, syslog, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.post(endpoint=TEST_SYSLOG_SETTINGS, data=syslog.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to test syslog, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_system_config(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=GET_SYSTEM_CONFIG, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get system config, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_notification_settings(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=NOTIFICATION_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get notification settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def set_notification_settings(self, data, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=NOTIFICATION_SETTINGS, data=data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set notification settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_notification_recipients_settings(self, recip_filter=None, **recip_args):
        query_params = NotificationRecipientsQueryFilter.get_query_params(recip_filter, recip_args)
        ret = list()
        res = self.client.get(endpoint=RECIPIENTS_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get notification recipients settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        if 'recipients' in list(res.data):
            recipients = res.data['recipients']
            for recip in recipients:
                ret.append(NotificationRecipient(**recip))
            res.data = ret
        return res

    def set_notification_recipients_settings(self, notification_recipient, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=RECIPIENTS_SETTINGS,
                              data=notification_recipient.to_json(),
                              query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set recipients, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = NotificationRecipient(**res.data)
        return res

    def delete_notification_recipient(self, recip_id):
        res = self.client.delete(endpoint=DELETE_NOTIFICATION_RECIPIENT.format(recip_id))
        if res.status_code != 200:
            logger.warning("Failed to delete notification recipient, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def get_sms_settings(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=SMS_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get sms settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SmsSmtp(**res.data)
        return res

    def set_sms_settings(self, sms, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=SMS_SETTINGS, data=sms.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set sms settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SmsSmtp(**res.data)
        return res

    def get_smtp_settings(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=SMTP_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get smtp settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SmsSmtp(**res.data)
        return res

    def set_smtp_settings(self, smtp, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=SMTP_SETTINGS, data=smtp.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set smtp settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = SmsSmtp(**res.data)
        return res

    def test_smtp_settings(self, smtp, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.post(endpoint=TEST_SMTP_SETTINGS, data=smtp.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to test smtp, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_sso_settings(self, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=SSO_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get sso settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Sso(**res.data)
        return res

    def set_sso_settings(self, sso, scope_filter=None, **scope_args):
        query_params = HighScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.put(endpoint=SSO_SETTINGS, data=sso.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set sso settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = Sso(**res.data)
        return res
