import time
from raft import task
from convocations.palo_alto.base import XmlApiTask


@task(klass=XmlApiTask)
def upgrade(ctx, version='10.1.5', api=None, username=None, password=None,
            host=None, peer=None, session=None, **kwargs):
    """
    Updates the ha pair
    """
    from panos.firewall import Firewall
    from .base import XmlApi
    from ..base.utils import notice, notice_end
    from lxml import etree
    api = api or XmlApi(host, username, password, session=session)
    username, password = XmlApi.resolve_creds(username, password, session)
    primary = Firewall(host, username, password)
    secondary = None
    if secondary:
        secondary = Firewall(peer, username, password)
        notice('setting preemptive to no')
        params = dict(
            xpath=(
                '/config/devices/entry[@name="localhost.localdomain"]'
                '/deviceconfig/high-availability/group/election-option'
            ),
            element='<preemptive>no</preemptive>',
        )
        r = api.post('config', 'set', **params)
        print(etree.tostring(r, pretty_print=True).decode('utf-8'))
        primary.commit(sync=True)
        notice_end()
        notice(f'upgrading secondary to version {version}')
        secondary.software.upgrade_to_version(version)
        notice_end()
        notice('waiting 120 seconds for secondary to come back up')
        time.sleep(120)
        notice_end()
        notice('checking version after upgrade')
        secondary.refresh_system_info()
        notice_end(secondary.version)
        input('please press <enter> to continue')
        notice('suspending ha on active peer')
        primary.op('request high-availability state suspend')
        notice_end()

    notice(f'upgrading primary to version {version}')
    primary.software.upgrade_to_version(version)
    notice_end()
    notice('waiting 120 seconds for primary to come back up')
    time.sleep(120)
    notice_end()
    notice('checking version after upgrade')
    primary.refresh_system_info()
    notice_end(primary.version)

    if secondary:
        notice('setting preemptive to yes')
        params = dict(
            xpath=(
                '/config/devices/entry[@name="localhost.localdomain"]'
                '/deviceconfig/high-availability/group/election-option'
            ),
            element='<preemptive>yes</preemptive>',
        )
        r = api.post('config', 'set', **params)
        notice_end()
        notice('committing')
        primary.commit(True)
        notice_end()
        print(etree.tostring(r, pretty_print=True).decode('utf-8'))
        notice('turning on ha on primary')
        primary.op('request high-availability state functional')
        notice_end()
        notice('turning off ha on secondary to force failover')
        secondary.op('request high-availability state suspend')
        notice_end()
        time.sleep(10)
        notice('turning ha back on secondary')
        secondary.op('request high-availability state functional')
        notice_end()
