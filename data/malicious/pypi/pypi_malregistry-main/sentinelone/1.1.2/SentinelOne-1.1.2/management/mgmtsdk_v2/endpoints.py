"""
This module contains all the endpoints the Management object uses to communicate
with the SentinelOne management
"""

# THREATS #
GET_THREATS = 'threats'
THREAT_GROUPS = 'private/threat-groups'
MARK_AS_RESOLVED = 'threats/mark-as-resolved'
MARK_AS_UNRESOLVED = 'threats/mark-as-unresolved'
MARK_AS_BENIGN = 'threats/mark-as-benign'
MARK_AS_THREAT = 'threats/mark-as-threat'
MITIGATE_THREAT = 'threats/mitigate/{}'
ADD_TO_BLACKLIST = 'threats/add-to-blacklist'
DISABLE_ENGINES = 'threats/engines/disable'
FETCH_THREAT = 'threats/fetch-file'
EXPORT_THREATS = 'threats/analyze/report'
UPDATE_THREAT = 'threats/{}'
WHITENING_OPTIONS = 'threats/{}/whitening-options'

# SITES #
GET_SITES = 'sites'
GET_SITE_BY_ID = 'sites/{}'
CREATE_SITE = 'sites'
REGENERATE_SITE_KEY = 'sites/{}/regenerate-key'
REVERT_SITE_POLICY = 'sites/{}/revert-policy'
UPDATE_SITE = 'sites/{}'
DELETE_SITE = 'sites/{}'
CREATE_WITH_ADMIN = 'site-with-admin'
UPDATE_SITE_POLICY = 'sites/{}/policy'
GET_SITE_POLICY = 'sites/{}/policy'
REACTIVATE_SITE = 'sites/{}/reactivate'
EXPIRE_SITE = 'sites/{}/expire-now'
DUPLICATE_SITE = 'sites/duplicate-site'
SITES_BULK_UPDATE = 'sites/update-bulk'

# REPORTS #
GET_REPORTS = 'reports'
GET_REPORTS_TASKS = 'report-tasks'
GET_INSIGHT_TYPES = 'reports/insights/types'
GET_RSS_FEED = 'sentinelonerss'
DELETE_REPORTS = 'reports/delete-reports'
DELETE_REPORT_TASKS = 'reports/delete-tasks'
CREATE_REPORT_TASK = 'report-tasks'
UPDATE_REPORT_TASK = 'report-tasks/{}'

# GROUPS #
GET_GROUPS = 'groups'
GET_GROUP_BY_ID = 'groups/{}'
GET_DEFAULT_GROUP = 'private/groups-default'
COUNT_GROUPS = 'private/group-count'
UPDATE_RANKS = 'groups/ranks'
CREATE_GROUP = 'groups'
REVERT_GROUP_POLICY = 'groups/{}/revert-policy'
UPDATE_GROUP_POLICY = 'groups/{}/policy'
GET_GROUP_POLICY = 'groups/{}/policy'
MOVE_AGENTS = 'groups/{}/move-agents'
DELETE_GROUP = 'groups/{}'
UPDATE_GROUP = 'groups/{}'
REGENERATE_GROUP_KEY = 'groups/{}/regenerate-key'

# AGENTS #
GET_AGENTS = 'agents'
COUNT_AGENTS = 'agents/count'
GET_APPLICATIONS = 'agents/applications'
GET_PROCESSES = 'agents/processes'
GET_PASSPHRASES = 'agents/passphrases'
EXPORT_LOGS = 'agents/{}/uploads/{}'

# UPDATES #
UPLOAD_PACKAGE = 'upload/software'
DEPLOY_PACKAGE = 'upload/software/deploy'
LATEST_PACKAGES_BY_OS = 'update/agent/latest-packages'
DELETE_PACKAGES = 'update/agent/packages'
LATEST_PACKAGES = 'update/agent/packages'
UPLOAD_AGENT_PACKAGE = 'upload/agent/software'
DOWNLOAD_PACKAGE = 'update/agent/download/{}/{}'
DOWNLOAD_AGENT_PACKAGE = 'update/agent/download/{}'
UPDATE_PACKAGE = 'update/agent/packages/{}'

# POLICIES #
GET_POLICY = 'private/policy'
CREATE_POLICY = 'private/policy'
GLOBAL_POLICY = 'tenant/policy'
UPDATE_TENANT_POLICY = 'tenant/policy'
HOTFIX_POLICY = 'atlas-agents-control/hotfix-policy/policy'

# EXCLUSIONS #
RESTRICTIONS = 'restrictions'
RESTRICTIONS_VALIDATION = 'restrictions/validate'
EXCLUSIONS = 'exclusions'
EXCLUSIONS_VALIDATION = 'exclusions/validate'
EXCLUSIONS_CATALOG = 'private/exclusions/applications-catalog'
EXPORT_EXCLUSIONS = 'export/exclusions'
EXPORT_RESTRICTIONS = 'export/restrictions'

# SYSTEM #
SYSTEM_COMMON_PREFIX = 'system'
SYSTEM_CONFIG = '{}/configuration'.format(SYSTEM_COMMON_PREFIX)
SYSTEM_INFO = '{}/info'.format(SYSTEM_COMMON_PREFIX)
SYSTEM_STATUS = '{}/status'.format(SYSTEM_COMMON_PREFIX)
ENABLED_FEATURES = 'private/{}/enabled-features'.format(SYSTEM_COMMON_PREFIX)
SYSTEM_EULA_CONFIG = 'private/system/eula-config'

# CONFIG_OVERRIDE #
CONFIG_OVERRIDE = 'config-override'
DELETE_CONFIG_OVERRIDE = 'config-override/{}'
UPDATE_CONFIG_OVERRIDE = 'config-override/{}'

# ACTIVITIES #
EXPORT = 'export/activities'
ACTIVITIES = 'activities'
ACTIVITY_TYPES = 'activities/types'

# AGENT ACTIONS #
AGENT_ACTIONS_COMMON_PREFIX = 'agents/actions'
RESET_LOCAL_CONFIG = '{}/reset-local-config'.format(AGENT_ACTIONS_COMMON_PREFIX)
APPROVE_UNINSTALL = '{}/approve-uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
REJECT_UNINSTALL = '{}/reject-uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
RESTART = '{}/restart-machine'.format(AGENT_ACTIONS_COMMON_PREFIX)
UPDATE_SOFTWARE = '{}/update-software'.format(AGENT_ACTIONS_COMMON_PREFIX)
INITIATE_SCAN = '{}/initiate-scan'.format(AGENT_ACTIONS_COMMON_PREFIX)
DECOMMISSION = '{}/decommission'.format(AGENT_ACTIONS_COMMON_PREFIX)
MOVE_AGENTS_TO_SITE = '{}/move-to-site'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_LOGS = '{}/fetch-logs'.format(AGENT_ACTIONS_COMMON_PREFIX)
ABORT_SCAN = '{}/abort-scan'.format(AGENT_ACTIONS_COMMON_PREFIX)
DISCONNECT_FROM_NETWORK = '{}/disconnect'.format(AGENT_ACTIONS_COMMON_PREFIX)
SET_PERSISTENT_CONFIG_OVERRIDES = '{}/set-config'.format(AGENT_ACTIONS_COMMON_PREFIX)
BROADCAST_MESSAGE = '{}/broadcast'.format(AGENT_ACTIONS_COMMON_PREFIX)
UNINSTALL = '{}/uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
SHUTDOWN = '{}/shutdown'.format(AGENT_ACTIONS_COMMON_PREFIX)
CONNECT_TO_NETWORK = '{}/connect'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_FILES = 'agents/{}/actions/fetch-files'
MOVE_TO_CONSOLE = 'agents/actions/move-to-console'
START_REMOTE_SHELL = '{}/start-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
CLEAR_REMOTE_SHELL = '{}/clear-remote-shell-session'.format(AGENT_ACTIONS_COMMON_PREFIX)
CAN_START_REMOTE_SHELL = '{}/can-start-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
TERMINATE_REMOTE_SHELL = '{}/terminate-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_INSTALLED_APPS = '{}/fetch-installed-apps'.format(AGENT_ACTIONS_COMMON_PREFIX)
RANDOMIZE_UUID = '{}/randomize-uuid'.format(AGENT_ACTIONS_COMMON_PREFIX)
FIREWALL_LOGGING = '{}/firewall-logging'.format(AGENT_ACTIONS_COMMON_PREFIX)
SET_EXTERNAL_ID = '{}/set-external-id'.format(AGENT_ACTIONS_COMMON_PREFIX)
MARK_AS_UP_TO_DATE = '{}/mark-up-to-date'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_APPLICATIONS = '{}/fetch-installed-apps'.format(AGENT_ACTIONS_COMMON_PREFIX)
DISABLE_RANGER = '{}/ranger-disable'.format(AGENT_ACTIONS_COMMON_PREFIX)
ENABLE_RANGER = '{}/ranger-enable'.format(AGENT_ACTIONS_COMMON_PREFIX)

# USERS #
LOGIN_BY_TOKEN = 'users/login/by-token'
LOGIN_BY_API_TOKEN = 'users/login/by-api-token'
LOGIN_BY_RECOVERY_CODE = 'users/auth/recovery-code'
AUTH_WITH_APP = 'users/auth/app'
SIGN_IN_WITH_EULA = 'users/auth/eula'
DISABLE_TWO_FA = 'users/2fa/disable'
ENABLE_TWO_FA = 'users/2fa/enable'
GENERATE_RECOVERY_CODES = 'users/generate-recovery-codes'
CHECK_TENANT_ADMIN = 'users/tenant-admin-auth-check'
VERIFY_CODE = 'users/user-code-verification'
GENERATE_API_TOKEN = 'users/generate-api-token'
CHECK_VIEWER_AUTH = 'users/viewer-auth-check'
REVOKE_API_TOKEN = 'users/revoke-api-token'
CHANGE_PASSWORD = 'users/change-password'
DELETE_USERS = 'users/delete-users'
REQUEST_TWO_FA_APP = 'users/request-app'
ENABLE_TWO_FA_APP = 'users/enable-app'
LOGIN = 'users/login'
UPDATE_USER = 'users/{}'
GET_USER = 'users/{}'
DELETE_USER = 'users/{}'
API_TOKEN_DETAILS_FOR_USERS = 'users/{}/api-token-details'
AUTH_BY_SSO = 'users/login/sso-saml2/{}'
USER_BY_TOKEN = 'user'
LOGOUT = 'users/logout'
CREATE_USER = 'users'
RESET_2FA = 'users/reset-2fa'
RECOVER_EMAIL = 'users/{}/recovery-email'
VERIFY_RECOVER_EMAIL = 'users/{}/verify-code-recovery-email'
SEND_CODE = 'users/2fa-recover/send-code'
VERIFY_CODE_2FA = 'users/2fa-recover/verify-code'
RESEND_RECOVERY_EMAIL = 'users/{}/resend-recovery-email-code'

GENERATE_IFRAME_TOKEN = 'users/generate-iframe-token'
LOGIN_BY_IFRAME_USER = 'private/users/login/by-iframe-token'
REVOKE_IFRAME_TOKEN = 'private/users/revoke-iframe-token'
IFRAME_TOKEN_DETAILS = 'private/users/iframe-token-details'
MY_USER = 'private/my-user'

SEND_VERIFICATION_EMAIL = 'users/onboarding/send-verification-email'
VALIDATE_VERIFICATION_TOKEN = 'users/onboarding/validate-token'
VERIFY_EMAIL = 'users/onboarding/verify'

# FILTERS #
GET_DV_FILTER = 'filters/dv'
SAVE_DV_FILTER = 'filters/dv'
UPDATE_DV_FILTER = 'filters/dv/{}'
DELETE_DV_FILTER = 'filters/dv/{}'
FILTERS_WITH_METADATA = 'private/filters/enriched'
GET_FILTERS = 'filters'
SAVE_FILTER = 'filters'
DELETE_FILTER = 'filters/{}'
UPDATE_FILTER = 'filters/{}'

# HASH #
HASH_CLASSIFICATION = 'hashes/{}/classification'
HASH_REPUTATION = 'hashes/{}/reputation'

# FORENSICS #
GET_THREAT_FORENSIC_DETAILS = 'threats/{}/forensics/details'
GET_APPLICATION_FORENSIC_DETAILS = 'applications/{}/forensics/details'
GET_THREAT_FORENSICS = 'threats/{}/forensics'
GET_APPLICATION_FORENSICS = 'applications/{}/forensics'
GET_THREAT_CONNECTIONS = 'threats/{}/forensics/connections'
GET_APPLICATION_CONNECTIONS = 'applications/{}/forensics/connections'
EXPORT_THREAT = 'threats/{}/forensics/export/{}'
EXPORT_APPLICATION = 'applications/{}/forensics/export/{}'
GET_THREAT_SEEN_ON_NETWORK = 'threats/{}/forensics/seenOnNetwork'

# DEEP VISIBILITY #
GET_EVENT_SEEN_ON_NETWORK = 'ioc/events/process/seen-on-network'
GET_PROCESS_BY_UNIQUE_KEY = 'ioc/process-unique-key'
GET_EVENTS = 'ioc/events'
GET_AGENTS_BREAKDOWN = 'ioc/agents'
GET_PROCESS_BY_AGENT = 'ioc/events/process/{}'
GET_AGENT_SEEN_ON_NETWORK = 'ioc/agents/{}/seen-on-network'
GET_EVENTS_BY_PROCESS = 'ioc/events/{}'
GET_AGENTS_DRILLDOWN = 'ioc/agents/{}'
GET_EVENTS_FILTERED = 'ioc/{}'

# DEEP VISIBILITY_V=2 #
DV_V2_CANCEL_RUNNING_QUERY = 'dv/cancel-query'
DV_V2_GET_EVENT_TYPES = 'dv/count-by-type'
DV_V2_GET_DISTINCT_FIELDS_DATA = 'private/dv/distinct-fields-data'
DV_V2_GET_ALL_EVENTS = 'dv/events'
DV_V2_GET_ALL_PROCESSES = 'dv/process-state'
DV_V2_GET_EVENTS_BY_TYPE = 'dv/events/{}'
DV_V2_CREATE_QUERY = 'dv/init-query'
DV_V2_GET_RECENT_QUERIES = 'dv/queries'
DV_V2_GET_QUERY_STATUS = 'dv/query-status'
DV_V2_GET_PROCESS_STATE = "dv/process-state"
DV_V2_GET_AGENTS = 'private/dv/agents'
DV_V2_GET_SINGLE_EVENT = 'private/dv/event'
DV_V2_GET_PROCESSES = 'private/dv/processes'
DV_V2_GET_TREE = 'private/dv/tree'
DV_V2_GET_ALL_EVENTS_IN_PROCESS_TREE = 'private/dv/tree/events'
DV_V2_CREATE_PROCESS_TREE_QUERY = 'private/dv/tree/init-tree-query'
DV_V2_GET_PROCESS_TREE_EVENTS_BY_TYPE = 'private/dv/tree/{}'
DV_V2_FETCH_FILE = 'dv/fetch-file'
DV_V2_CREATE_POWER_QUERY = 'dv/events/pq'
DV_V2_PING_POWER_QUERY = 'dv/events/pq-ping'


# COMMANDS #
GET_COMMANDS = 'private/commands'

# SETTINGS #
SYSLOG = 'settings/syslog'
GET_SYSTEM_CONFIG = 'private/settings/system-configuration'
AD_SETTINGS = 'settings/active-directory'
NOTIFICATION_SETTINGS = 'settings/notifications'
RECIPIENTS_SETTINGS = 'settings/recipients'
DELETE_NOTIFICATION_RECIPIENT = 'settings/recipients/{}'
SMS_SETTINGS = 'settings/sms'
SMTP_SETTINGS = 'settings/smtp'
SSO_SETTINGS = 'settings/sso'
TEST_SMTP_SETTINGS = 'settings/smtp/test'
TEST_SYSLOG_SETTINGS = 'settings/syslog/test'

# DEVICE CONTROL #
DEVICE_CONTROL = 'device-control'
DEVICE_CONTROL_INTERFACES = 'private/device-control/interfaces'
DEVICE_CONTROL_REORDER = 'device-control/reorder'
DEVICE_CONTROL_PRIVATE_FILTERS_COUNT = 'private/device-control/filters-count'
DEVICE_CONTROL_UPDATE_RULE = 'device-control/{}'
DEVICE_CONTROL_SETTINGS = 'device-control/configuration'
DEVICE_CONTROL_COPY_RULES = 'device-control/copy-rules'
DEVICE_CONTROL_MOVE_RULES = 'device-control/move-rules'
DEVICE_CONTROL_STATUS = 'device-control/enable'
DEVICE_CONTROL_EVENTS = 'device-control/events'

# ACCOUNTS #
GET_ACCOUNTS_PRIVATE = 'private/accounts'
ACCOUNTS = 'accounts'
ACCOUNT_WITH_ADMIN = 'private/account-with-admin'
ACCOUNT_REVERT_POLICY = 'accounts/{}/revert-policy'
ACCOUNT_REACTIVATE = 'accounts/{}/reactivate'
ACCOUNT_EXPIRE_NOW = 'accounts/{}/expire-now'
ACCOUNT_SPECIFIC = 'accounts/{}'
UPDATE_ACCOUNT_POLICY = 'accounts/{}/policy'
GET_ACCOUNT_POLICY = 'accounts/{}/policy'
GENERATE_UNINSTALL_PASSWORD = 'accounts/{}/uninstall-password/generate'
GET_UNINSTALL_PASSWORD = 'accounts/{}/uninstall-password/view'
GET_UNINSTALL_PASSWORD_DETAILS = 'accounts/{}/uninstall-password/metadata'
REVOKE_UNINSTALL_PASSWORD = 'accounts/{}/uninstall-password/revoke'

# FIREWALL CONTROL #
FIREWALL_CONTROL = 'firewall-control'
FIREWALL_CONTROL_REORDER = 'firewall-control/reorder'
FIREWALL_CONTROL_PRIVATE_FILTERS_COUNT = 'private/firewall-control/filters-count'
FIREWALL_CONTROL_UPDATE_RULE = 'firewall-control/{}'
FIREWALL_CONTROL_SETTINGS = 'firewall-control/configuration'
FIREWALL_CONTROL_COPY_RULES = 'firewall-control/copy-rules'
FIREWALL_CONTROL_MOVE_RULES = 'firewall-control/move-rules'
FIREWALL_CONTROL_STATUS = 'firewall-control/enable'
FIREWALL_CONTROL_FREE_TEXT_FILTERS = 'private/firewall-control/free-text-filters'
FIREWALL_CONTROL_FILTER_AUTO_COMPLETE = 'private/firewall-control/filters-autocomplete'
FIREWALL_CONTROL_ADD_TAGS = 'firewall-control/add-tags'
FIREWALL_CONTROL_REMOVE_TAGS = 'firewall-control/remove-tags'

# APPS #
GET_INSTALLED_APPS = 'installed-applications'
GET_CVES = 'installed-applications/cves'
GET_CVES_ENRICHED = 'private/installed-applications/{}/cves'
GET_FREE_TEXT_FILTERS = 'private/installed-applications/free-text-filters'
GET_FILTERS_AUTO_COMPLETE = 'private/installed-applications/filters-autocomplete'
GET_FILTERS_COUNT = 'private/installed-applications/filters-count'
GET_RISK_LEVELS_COUNT = 'private/installed-applications/risk-levels-count'
GROUPED_APP_INVENTORY = 'application-inventory'
APP_INVENTORY_COUNTS = 'application-inventory-counts'

# LOCATIONS #
LOCATIONS = 'locations'
UPDATE_LOCATION = 'locations/{}'
COPY_LOCATIONS = 'locations/copy'
LOCATIONS_FREE_TEXT_FILTERS = 'private/locations/free-text-filters'
LOCATIONS_FILTER_AUTO_COMPLETE = 'private/locations/filters-autocomplete'
LOCATIONS_FILTER_COUNT = 'private/locations/filters-count'

# NAVIGATION #
NAVIGATION_GET_TOP_LEVEL_ENDPOINTS = 'private/navigation/top-level/totals'
NAVIGATION_GET_ACCOUNTS = 'private/navigation/accounts'
NAVIGATION_GET_GROUPS = 'private/navigation/groups'
NAVIGATION_SEARCH_FOR_SCOPE_OBJECTS = 'private/navigation/search'
NAVIGATION_GET_TOTAL_ENDPOINTS = 'private/navigation/totals'
NAVIGATION_GET_SITES = 'private/navigation/sites'
NAVIGATION_GET_SINGLE_ACCOUNT = 'private/navigation/accounts/{}'
NAVIGATION_GET_SINGLE_GROUP = 'private/navigation/groups/{}'
NAVIGATION_GET_SINGLE_SITE = 'private/navigation/sites/{}'

# RANGER #
RANGER_DEVICE_INVENTORY_TABLE_VIEW = 'ranger/table-view'
RANGER_FILTERS_COUNT = 'private/ranger/filters-count'
RANGER_EXPORT_DEVICE_INVENTORY = 'ranger/report/csv'
RANGER_FREE_TEXT_FILTERS = 'private/ranger/free-text-filters'
RANGER_FILTERS_AUTO_COMPLETE = 'private/ranger/filters-autocomplete'
RANGER_GET_ROW_JSON = 'ranger/{}/json'
RANGER_RAW_DATA_EXPORT = 'ranger/{}/json/export'
RANGER_GET_SNAPSHOT_STATUS = 'private/ranger/snapshot-status'
RANGER_GET_LATEST_SNAPSHOT = 'private/ranger/latest-snapshot'
RANGER_GET_GATEWAYS = 'ranger/gateways'
RANGER_UPDATE_GATEWAY = 'ranger/gateways/{}'
RANGER_UPDATE_GATEWAYS = 'ranger/gateways/update'
RANGER_NETWORK_DASHBOARD = 'private/ranger/gateways/dashboard'
RANGER_GET_SETTINGS = 'ranger/settings'
RANGER_UPDATE_SETTINGS = 'ranger/settings'
RANGER_SUBNET_SCAN_DATA = 'private/ranger/scan-data'
GATEWAY_FILTERS_COUNT = 'private/ranger/gateways/filters-count'
GATEWAY_FREE_TEXT_FILTERS = 'private/ranger/gateways/free-text-filters'
GATEWAY_FILTERS_AUTO_COMPLETE = 'private/ranger/gateways/filters-autocomplete'

# RBAC #
RBAC_GET_ROLES = 'rbac/roles'
RBAC_GET_USER_ROLE = 'rbac/role/{}'
RBAC_GET_USER_PERMISSIONS = 'private/rbac/user-permissions'

# APIDOC #
APIDOC_GET = 'apidoc'
APIDOC_GET_SWAGGER = 'apidoc/swagger.json'

# TASKS #
TASKS_GET_TASKS = 'private/tasks'
TASKS_CANCEL_TASK = 'private/tasks/cancel-task'
TASKS_FILTERS_COUNT = 'private/tasks/filters-count'
TASKS_FREE_TEXT_FILTERS = 'private/tasks/free-text-filters'
TASKS_FILTERS_AUTO_COMPLETE = 'private/tasks/filters-autocomplete'
TASKS_DOWNLOAD_OUTPUT_FILE = 'remote-scripts/fetch-file'
TASKS_TASK_CONFIGURATION = 'tasks-configuration'
TASKS_GET_TASK_CONFIGURATION_HAS_EXPLICIT_SUBSCOPE = 'tasks-configuration/has-explicit-subscope'
TASKS_GET_TASK_CONFIGURATION_EXPLICIT_SUBSCOPES = 'tasks-configuration/explicit-subscopes'

# STAR (WATCHLIST) #
STAR_GET_FILTERS_COUNT = "private/cloud-detection/rules/filters-count"
WATCHLIST_RULES = 'cloud-detection/rules'
WATCHLIST_RULES_ENABLE = f'{WATCHLIST_RULES}/enable'
WATCHLIST_RULES_DISABLE = f'{WATCHLIST_RULES}/disable'
STAR_AVAILABLE_ACTIONS = f'private/cloud-detection/alerts/available-actions'
