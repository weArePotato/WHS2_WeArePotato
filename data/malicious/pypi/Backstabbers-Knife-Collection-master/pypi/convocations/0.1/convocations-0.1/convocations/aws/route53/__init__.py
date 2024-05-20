from raft.tasks import task

from ...base.utils import notice, notice_end, print_table
from ..base import AwsTask
from ..base import yielder


@task(klass=AwsTask)
def nameservers(ctx, zone_name, session=None, **kwargs):
    """
    lists all of the name servers for a particular zone name
    """
    route53 = session.client('route53')
    g = yielder(route53, 'list_hosted_zones')
    header = [ 'zone', 'id', 'nameserver' ]
    rows = []
    for x in g:
        if zone_name.lower() in x['Name']:
            notice(x['Name'])
            hosted_zone = route53.get_hosted_zone(Id=x['Id'])
            if 'DelegationSet' in hosted_zone:
                ns = hosted_zone['DelegationSet']['NameServers']
                for nameserver in ns:
                    rows.append([ x['Name'], x['Id'], nameserver ])
            else:
                rows.append([ x['Name'], x['Id'], '' ])
            notice_end()
    print_table(header, rows)
