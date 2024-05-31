import logging

from management.mgmtsdk_v2.endpoints import RBAC_GET_USER_ROLE, RBAC_GET_ROLES, RBAC_GET_USER_PERMISSIONS
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Rbac')


class Rbac(object):
    """Rbac service"""

    def __init__(self, client):
        self.client = client

    def get_rbac_roles(self, **kwargs):
        res = self.client.get(endpoint=RBAC_GET_ROLES, params=kwargs)
        if res.status_code != 200:
            logging.warning("Failed to Get rbac roles, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_rbac_role(self, **kwargs):
        res = self.client.get(endpoint=RBAC_GET_USER_ROLE.format(kwargs['id']), params=kwargs)
        if res.status_code != 200:
            logging.warning("Failed to Get rbac role, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_rbac_fe_role(self, **kwargs):
        res = self.client.get(endpoint=RBAC_GET_USER_PERMISSIONS, params=kwargs)
        if res.status_code != 200:
            logging.warning("Failed to Get rbac FE role, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
