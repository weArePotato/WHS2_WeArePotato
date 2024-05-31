from management.mgmtsdk_v2.services import Agents, Exclusions, ExclusionsCatalog, ConfigOverrides, \
    Policies, Groups, InsightTypes, Reports, ReportTasks, RssFeeds, \
    Sites, System, Users, Threats, Activities, Filters, Hashes, Updates, \
    AgentActions, Forensics, DeepVisibility, Commands, Settings, DeviceControl, Accounts, FirewallControl, \
    Applications, DeepVisibilityV2, Locations, Navigation, Ranger, Rbac, ApiDoc, Tasks, TasksConfiguration, api
from .client import Client
from .services.glads_asset_inventory import GlobalAssetsInventory


class Management(object):
    """
    Management object provides all capabilities the SDK has to offer.
    The management object fields are the services which provides the APIs
    to communicate with the SentinelOne management console

    So for example, to perform threat related operations one should use the Management's
    object threat field, endpoint operations via Management's agents, etc
    """

    def __init__(self, hostname, username=None, password=None, api_token=None, client_settings=None, auth_manager=None):
        """
        :param hostname: Management's hostname
        :type hostname: string
        :param username: Management username
        :type username: string
        :param password: Management password
        :type password: string
        :param api_token: Management Api Token
        :type api_token: string
        :param client_settings: all parameters  to requests lib such as: verify / proxy / timeout / etc.
        :type client_settings: dict
        """
        if not client_settings:
            client_settings = {}

        self.client = Client(hostname=hostname, username=username, password=password,
                             api_token=api_token, client_settings=client_settings, auth_manager=auth_manager)
        self.hostname = hostname
        self.accounts = Accounts(self.client)
        self.activities = Activities(self.client)
        self.agent_actions = AgentActions(self.client)
        self.agents = Agents(self.client)
        self.api =  api.run()
        self.apidoc = ApiDoc(self.client)
        self.applications = Applications(self.client)
        self.commands = Commands(self.client)
        self.config_override = ConfigOverrides(self.client)
        self.deep_visibility = DeepVisibility(self.client)
        self.deep_visibility_v2 = DeepVisibilityV2(self.client)
        self.device_control = DeviceControl(self.client)
        self.exclusions = Exclusions(self.client)
        self.exclusions_catalog = ExclusionsCatalog(self.client)
        self.filters = Filters(self.client)
        self.firewall_control = FirewallControl(self.client)
        self.forensics = Forensics(self.client)
        self.groups = Groups(self.client)
        self.hashes = Hashes(self.client)
        self.insight_types = InsightTypes(self.client)
        self.locations = Locations(self.client)
        self.navigation = Navigation(self.client)
        self.policies = Policies(self.client)
        self.ranger = Ranger(self.client)
        self.rbac = Rbac(self.client)
        self.report_tasks = ReportTasks(self.client)
        self.reports = Reports(self.client)
        self.rss = RssFeeds(self.client)
        self.settings = Settings(self.client)
        self.sites = Sites(self.client)
        self.system = System(self.client)
        self.tasks = Tasks(self.client)
        self.tasks_configuration = TasksConfiguration(self.client)
        self.threats = Threats(self.client)
        self.updates = Updates(self.client)
        self.users = Users(self.client)
        self.global_assets_inventory = GlobalAssetsInventory(self.client)
    def __repr__(self):
        return '<management.mgmtsdk_v2.mgmt.Management: {}>'.format(self.hostname)
