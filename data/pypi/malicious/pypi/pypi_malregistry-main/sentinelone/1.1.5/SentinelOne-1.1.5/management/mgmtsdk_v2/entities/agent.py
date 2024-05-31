
class Agent(object):

    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.activeDirectory = ActiveDirectory(**kwargs.get('activeDirectory'))
        self.activeThreats = kwargs.get('activeThreats', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.appsVulnerabilityStatus = kwargs.get('appsVulnerabilityStatus', None)
        self.computerName = kwargs.get('computerName', None)
        self.consoleMigrationStatus = kwargs.get('consoleMigrationStatus', None)
        self.consoleMigrationStatuses = kwargs.get('consoleMigrationStatuses', None)
        self.coreCount = kwargs.get('coreCount', None)
        self.cpuCount = kwargs.get('cpuCount', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.cpuId = kwargs.get('cpuId', None)
        self.domain = kwargs.get('domain', None)
        self.encryptedApplications = kwargs.get('encryptedApplications', None)
        self.externalId = kwargs.get('externalId', None)
        self.externalIp = kwargs.get('externalIp', None)
        self.groupIp = kwargs.get('groupIp', None)
        self.groupId = kwargs.get('groupId', None)
        self.id = kwargs.get('id', None)
        self.groupName = kwargs.get('groupName', None)
        self.infected = kwargs.get('infected', None)
        self.inRemoteShellSession = kwargs.get('inRemoteShellSession', None)
        self.installerType = kwargs.get('installerType', None)
        self.isActive = kwargs.get('isActive', None)
        self.isDecommissioned = kwargs.get('isDecommissioned', None)
        self.decommissionedAt = kwargs.get('decommissionedAt', None)
        self.isPendingUninstall = kwargs.get('isPendingUninstall', None)
        self.isUninstalled = kwargs.get('isUninstalled', None)
        self.isUpToDate = kwargs.get('isUpToDate', None)
        self.lastActiveDate = kwargs.get('lastActiveDate', None)
        self.lastLoggedInUserName = kwargs.get('lastLoggedInUserName', None)
        self.licenseKey = kwargs.get('licenseKey', None)
        self.locations = kwargs.get('locations', None)
        self.locationType = kwargs.get('locationType', None)
        self.machineType = kwargs.get('machineType', None)
        self.migrationStatus = kwargs.get('migrationStatus', None)
        self.mitigationMode = kwargs.get('mitigationMode', None)
        self.mitigationModeSuspicious = kwargs.get('mitigationModeSuspicious', None)
        self.modelName = kwargs.get('modelName', None)
        network_interfaces = kwargs.get('networkInterfaces', None)
        self.networkInterfaces = [NetworkInterface(**ni) for ni in network_interfaces]
        self.networkStatus = kwargs.get('networkStatus', None)
        self.osArch = kwargs.get('osArch', None)
        self.osName = kwargs.get('osName', None)
        self.osRevision = kwargs.get('osRevision', None)
        self.osStartTime = kwargs.get('osStartTime', None)
        self.osType = kwargs.get('osType', None)
        self.osUsername = kwargs.get('osUsername', None)
        self.registeredAt = kwargs.get('registeredAt', None)
        self.scanAbortedAt = kwargs.get('scanAbortedAt', None)
        self.scanFinishedAt = kwargs.get('scanFinishedAt', None)
        self.scanStartedAt = kwargs.get('scanStartedAt', None)
        self.scanStatus = kwargs.get('scanStatus', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.totalMemory = kwargs.get('totalMemory', None)
        self.userActionsNeeded = kwargs.get('userActionsNeeded', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.uuid = kwargs.get('uuid', None)
        self.cloudProviders = CloudProvider.get_providers_from_data(**kwargs.get('cloudProviders', {}))


class ActiveDirectory(object):

    def __init__(self, **kwargs):
        self.computerDistinguishedName = kwargs.get('computerDistinguishedName', None)
        self.computerMemberOf = kwargs.get('computerMemberOf', None)
        self.lastUserDistinguishedName = kwargs.get('lastUserDistinguishedName', None)
        self.lastUserMemberOf = kwargs.get('lastUserMemberOf', None)


class NetworkInterface(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        inet = kwargs.get('inet', None)
        self.inet = [i for i in inet]
        inet6 = kwargs.get('inet6', None)
        self.inet6 = [i for i in inet6]
        self.name = kwargs.get('name', None)
        self.physical = kwargs.get('physical', None)


class AgentCountSummary(object):

    def __init__(self, **kwargs):
        self.decommissioned = kwargs.get('decommissioned', None)
        self.infected = kwargs.get('infected', None)
        self.online = kwargs.get('online', None)
        self.outOfDate = kwargs.get('outOfDate', None)
        self.total = kwargs.get('total', None)
        self.upToDate = kwargs.get('upToDate', None)


class Application(object):

    def __init__(self, **kwargs):
        self.installedDate = kwargs.get('installedDate', None)
        self.name = kwargs.get('name', None)
        self.publisher = kwargs.get('publisher', None)
        self.size = kwargs.get('size', None)
        self.version = kwargs.get('version', None)

class Process(object):

    def __init__(self, **kwargs):
        self.cpuUsage = kwargs.get('cpuUsage', None)
        self.executablePath = kwargs.get('executablePath', None)
        self.memoryUsage = kwargs.get('memoryUsage', None)
        self.pid = kwargs.get('pid', None)
        self.processName = kwargs.get('processName', None)
        self.startTime = kwargs.get('startTime', None)


class CloudProvider(object):
    def __init__(self, **kwargs):
        self.cloud_provider = kwargs.get('cloud_provider')
        self.azr_vm_size = kwargs.get('azr_vm_size')
        self.azr_location = kwargs.get('azr_location')
        self.azr_subscription_id = kwargs.get('azr_subscription_id')
        self.azr_vm_id = kwargs.get('azr_vm_id')
        self.azr_image = kwargs.get('azr_image')
        self.azr_tags = kwargs.get('azr_tags')
        self.aws_instance_type = kwargs.get('aws_instance_type')
        self.aws_region = kwargs.get('aws_region')
        self.aws_ami_id = kwargs.get('aws_ami_id')
        self.aws_account_id = kwargs.get('aws_account_id')
        self.aws_instance_id = kwargs.get('aws_instance_id')
        self.aws_security_groups = kwargs.get('aws_security_groups')
        self.aws_role = kwargs.get('aws_role')
        self.aws_subnet_ids = kwargs.get('aws_subnet_ids')
        self.aws_vpc_id = kwargs.get('aws_vpc_id')
        self.aws_tags = kwargs.get('aws_tags')
        self.gcp_instance_type = kwargs.get('gcp_instance_type')
        self.gcp_zone = kwargs.get('gcp_zone')
        self.gcp_image = kwargs.get('gcp_image')
        self.gcp_project_id = kwargs.get('gcp_project_id')
        self.gcp_instance_id = kwargs.get('gcp_instance_id')
        self.gcp_network = kwargs.get('gcp_network')
        self.gcp_service_account_email = kwargs.get('gcp_service_account_email')
        self.gcp_tags = kwargs.get('gcp_tags')
        self.k8s_version = kwargs.get('k8s_version')
        self.k8s_type = kwargs.get('k8s_type')
        self.k8s_cluster_name = kwargs.get('k8s_cluster_name')
        self.k8s_node_name = kwargs.get('k8s_node_name')
        self.k8s_node_labels = kwargs.get('k8s_node_labels')
        self.k8s_pod_name = kwargs.get('k8s_pod_name')
        self.k8s_namespace = kwargs.get('k8s_namespace')

    @classmethod
    def get_providers_from_data(cls, data=None):
        providers = []
        if not data:
            return providers
        for provider_name, values in data.items():
            provider = cls(cloudProvider=provider_name, **values)
            providers.append(provider)
        return providers
