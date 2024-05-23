import logging

from management.common.query_filter import FullScopeFilter
from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.entities.policy import Policy
from management.mgmtsdk_v2.exceptions import raise_from_response, BadScopeException

logger = logging.getLogger('Policy')


class Policies(object):
    def __init__(self, client):
        self.client = client

    def get_global(self):
        """
        :return: global policy
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GLOBAL_POLICY)
        if res.status_code != 200:
            logger.warning("Failed to get global policy, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def get(self, scope_filter=None, **scope_args):
        """
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :return: Policy answering the query
        :rtype: ManagementResponse
        """
        query_params = FullScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=GET_POLICY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get policy, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def create(self, policy, scope_filter=None, **scope_args):
        """
        :param policy:
        :type policy:
        :param scope_filter: Scope filter object
        :type scope_filter: FullScopeFilter
        :param scope_args: Key value with query filters
        :type scope_args: **dict
        :return: created Policy
        :rtype: ManagementResponse
        """

        query_params = FullScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.post(endpoint=CREATE_POLICY, data=policy.to_json(), query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create policy, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def update_tenant(self, **kwargs):
        """
        :param kwargs:
        :type kwargs: **dict
        :return: updated tenant policy
        :rtype: ManagementResponse
        """
        policy = self.get_global().data
        for key, val in kwargs.items():
            if hasattr(policy.engines, key):
                policy.engines.__setattr__(key, _convert_engine_state(val))
            elif hasattr(policy.iocAttributes, key):
                policy.iocAttributes.__setattr__(key, val)
            elif hasattr(policy.autoFileUpload, key):
                policy.autoFileUpload.__setattr__(key, val)
            elif hasattr(policy.agentUi, key):
                policy.agentUi.__setattr__(key, val)

            else:
                policy.__setattr__(key, val)
        res = self.client.put(endpoint=UPDATE_TENANT_POLICY, data=policy.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update tenant policy, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Policy(**res.data)
        return res

    def change_dfi_engine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, preExecution=val)

    def change_reputation_engine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, reputation=val)

    def change_data_files(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, dataFiles=val)

    def change_executables_engine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, executables=val)

    def change_exploits_engine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, exploits=val)

    def change_lateral_movement(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, lateralMovement=val)

    def change_application_control(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, applicationControl=val)

    def change_penetration(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, penetration=val)

    def change_dfi_suspicious(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, preExecutionSuspicious=val)

    def change_pup_engine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_engine=True, pup=val)

    def change_ioc_attributes(self, site_id='', group_id='', tenant=None, **kwargs):
        return self._update_policy(site_id, group_id, tenant, is_ioc=True, **kwargs)

    def change_mitigation_mode(self, val, site_id='', group_id='', tenant=None):
        if val == 'detect':
            return self._update_policy(site_id, group_id, tenant,
                                       autoMitigationAction='mitigation.none',
                                       mitigationModeSuspicious='detect',
                                       mitigationMode='detect', networkQuarantineOn=False)
        if val == 'protect':
            return self._update_policy(site_id, group_id, tenant,
                                       autoMitigationAction='mitigation.quarantineThreat',
                                       mitigationMode='protect')
        return self._update_policy(site_id, group_id, tenant, mitigationMode=val)

    def change_mitigation_mode_suspicious(self, val, site_id='', group_id='', tenant=None):
        if val == 'protect':
            return self._update_policy(site_id, group_id, tenant,
                                       autoMitigationAction='mitigation.quarantineThreat',
                                       mitigationModeSuspicious='protect',
                                       mitigationMode='protect')
        return self._update_policy(site_id, group_id, tenant, mitigationModeSuspicious=val)

    def change_network_quarantine(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, networkQuarantineOn=val)

    def change_agent_logging(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, agentLoggingOn=val)

    def change_research(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, researchOn=val)

    def change_agent_ui(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, is_agent_ui=True, agentUiOn=val)

    def change_scan_new_agents(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, scanNewAgents=val)

    def change_anti_tamper(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, antiTamperingOn=val)

    def change_snapshots(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, snapshotsOn=val)

    def change_notification(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, agentNotification=val)

    def change_auto_decommission_days(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, autoDecommissionDays=val)

    def change_on_write(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, monitorOnWrite=val)

    def change_on_execute(self, val, site_id='', group_id='', tenant=None):
        return self._update_policy(site_id, group_id, tenant, monitorOnExecute=val)

    def change_auto_mitigation_action(self, val, site_id='', group_id='', tenant=None):
        if val == 'mitigation.none':
            return self._update_policy(site_id, group_id, tenant,
                                       autoMitigationAction=val,
                                       mitigationModeSuspicious='detect',
                                       mitigationMode='detect', networkQuarantineOn=False)
        return self._update_policy(site_id, group_id, tenant, autoMitigationAction=val)

    def change_file_upload(self, val, site_id='', group_id='', tenant=None, **kwargs):
        return self._update_policy(site_id, group_id, tenant, is_file_upload=val, **kwargs)

    def agent_hot_fix(self, enabled=True, enabledFamilyAssets=["1202907197076406354", "1202907197076406355"],
                      inherit=False, query_filter={'tenant': True}):
        data = {
            'enabled': enabled,
            'enabledFamilyAssets': enabledFamilyAssets,
            'inherit': inherit
        }

        res = self.client.put(endpoint=HOTFIX_POLICY, query_filter=query_filter, data=data)
        if res.status_code != 200:
            logger.warning("Failed to update tenant policy, response_code: {}".format(res.json))
            raise_from_response(res)

        return res

    def get_agent_hot_fix(self, scope_filter=None, **scope_args):
        query_params = FullScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=HOTFIX_POLICY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update tenant policy, response_code: {}".format(res.json))
            raise_from_response(res)

        return res

    def _update_policy(self, site_id='', group_id='', tenant=None,
                       is_engine=False, is_ioc=False, is_file_upload=False, is_agent_ui=False, is_rso=False, **kwargs):
        if tenant:
            if site_id or group_id:
                raise BadScopeException('Please provide only one of: site_id, group_id, or tenant=True')
            return self.update_tenant(**kwargs)
        scope_id = site_id if site_id else group_id
        if not scope_id:
            raise BadScopeException('Please provide one of: site_id, group_id, or tenant=True')
        if site_id:
            current = self.get(siteIds=site_id).data
            policy = _update_params(current, is_engine=is_engine, is_ioc=is_ioc, is_file_upload=is_file_upload,
                                    is_agent_ui=is_agent_ui, is_rso=is_rso, **kwargs)
            return self.create(policy, siteIds=site_id)
        if group_id:
            current = self.get(groupIds=group_id).data
            policy = _update_params(current, is_engine=is_engine, is_ioc=is_ioc, is_file_upload=is_file_upload,
                                    is_agent_ui=is_agent_ui, is_rso=is_rso, **kwargs)
            return self.create(policy, groupIds=group_id)

    def change_remote_scripts(self, site_id='', group_id='', tenant=None, **kwargs):
        return self._update_policy(site_id, group_id, tenant, is_rso=True, **kwargs)


def _update_params(current_policy, is_engine, is_ioc, is_file_upload, is_agent_ui, is_rso, **kwargs):
    if is_engine:
        for key, val in kwargs.items():
            current_policy.engines.__setattr__(key, _convert_engine_state(val))
    elif is_ioc:
        for key, val in kwargs.items():
            current_policy.iocAttributes.__setattr__(key, val)
    elif is_file_upload:
        for key, val in kwargs.items():
            current_policy.autoFileUpload.__setattr__(key, val)
    elif is_agent_ui:
        for key, val in kwargs.items():
            if key == 'agentUiOn':
                current_policy.__setattr__(key, val)
            current_policy.agentUi.__setattr__(key, val)
    elif is_rso:
        for key, val in kwargs.items():
            current_policy.remoteScriptOrchestration.__setattr__(key, val)
    else:
        for key, val in kwargs.items():
            current_policy.__setattr__(key, val)
    return current_policy


def _convert_engine_state(state):
    if state is True or str(state).lower() == 'true':
        return 'on'
    elif state is False or str(state).lower() == 'false':
        return 'off'
    else:
        return state
