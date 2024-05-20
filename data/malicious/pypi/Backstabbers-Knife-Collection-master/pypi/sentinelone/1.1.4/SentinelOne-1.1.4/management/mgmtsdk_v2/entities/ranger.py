import six


class Gateway(object):

    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.allowScan = kwargs.get('allowScan', None)
        self.allowedScanners = kwargs.get('allowedScanners', None)
        self.archived = kwargs.get('archived', None)
        self.connectedRangers = kwargs.get('connectedRangers', None)
        self.externalIp = kwargs.get('externalIp', None)
        self.id = kwargs.get('id', None)
        self.ip = kwargs.get('ip', None)
        self.inheritSettings = kwargs.get('inheritSettings', None)
        self.macAddress = kwargs.get('macAddress', None)
        self.new = kwargs.get('new', None)
        self.networkName = kwargs.get('networkName', None)
        self.numberOfAgents = kwargs.get('numberOfAgents', None)
        self.numberOfRangers = kwargs.get('numberOfRangers', None)
        self.scanOnlyLocalSubnets = kwargs.get('scanOnlyLocalSubnets', None)
        self.siteId = kwargs.get('siteId', None)
        self.tcpPorts = kwargs.get('tcpPorts', None)
        self.udpPorts = kwargs.get('udpPorts', None)


    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['id', 'accountName', ]:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
