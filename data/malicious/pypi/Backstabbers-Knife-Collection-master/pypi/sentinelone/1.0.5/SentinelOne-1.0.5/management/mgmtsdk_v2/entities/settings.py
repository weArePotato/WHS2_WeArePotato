import six


class BaseSettings(object):
    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class Syslog(BaseSettings):

    def __init__(self, **kwargs):
        self.clientCertContent = kwargs.get('clientCertContent', None)
        self.clientCertName = kwargs.get('clientCertName', None)
        self.clientKeyName = kwargs.get('clientKeyName', None)
        self.clientKeyContent = kwargs.get('clientKeyContent', None)
        self.enabled = kwargs.get('enabled', None)
        self.format = kwargs.get('format', None)
        self.host = kwargs.get('host', None)
        self.port = kwargs.get('port', None)
        self.serverCertContent = kwargs.get('serverCertContent', None)
        self.serverCertName = kwargs.get('serverCertName', None)
        self.ssl = kwargs.get('ssl', None)
        self.token = kwargs.get('token', None)


class SmsSmtp(BaseSettings):

    def __init__(self, **kwargs):
        self.enabled = kwargs.get('enabled', None)
        self.encryption = kwargs.get('encryption', None)
        self.host = kwargs.get('host', None)
        self.inherits = kwargs.get('inherits', None)
        self.noReplyEmail = kwargs.get('noReplyEmail', None)
        self.password = kwargs.get('password', None)
        self.port = kwargs.get('port', None)
        self.username = kwargs.get('username', None)


class Sso(BaseSettings):

    def __init__(self, **kwargs):
        self.autoProvisioning = kwargs.get('autoProvisioning', None)
        self.defaultUserRole = kwargs.get('defaultUserRole', None)
        self.enabled = kwargs.get('enabled', None)
        self.idpCertName = kwargs.get('idpCertName', None)
        self.idpEntityId = kwargs.get('idpEntityId', None)
        self.idpSsoUrl = kwargs.get('idpSsoUrl', None)
        self.spAcsUrl = kwargs.get('spAcsUrl', None)
        self.spEntityId = kwargs.get('spEntityId', None)

class Ad(BaseSettings):

    def __init__(self, **kwargs):
        self.enabled = kwargs.get('enabled', None)
        self.host = kwargs.get('host', None)
        self.port = kwargs.get('port', None)
        self.rootDn = kwargs.get('rootDn', None)
        self.ssl = kwargs.get('ssl', None)
        self.username = kwargs.get('username', None)

class NotificationRecipient(BaseSettings):

    def __init__(self, **kwargs):
        self.email = kwargs.get('email', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.sms = kwargs.get('sms', None)
