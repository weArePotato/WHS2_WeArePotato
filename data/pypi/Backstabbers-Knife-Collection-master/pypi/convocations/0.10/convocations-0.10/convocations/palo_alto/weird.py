from lxml import etree
from raft import task
from .base import XmlApiTask, XmlApi
from ..base.utils import notice, notice_end


@task(klass=XmlApiTask)
def remove_hip_profiles(ctx, host=None, config=None,
                        device='localhost.localdomain',
                        vsys='vsys1', **kwargs):
    """
    if we see weird hip profiles in the rulebase, this convocation removes them
    """
    notice(f'connecting to {host}')
    api = kwargs.get('api')
    api = api or XmlApi(host, filename=config)
    doc = api.get('config', 'show')
    notice_end()
    notice('searching rules')
    xpath = (
        f"devices/entry[@name='{device}']/vsys/"
        f"entry[@name='{vsys}']/rulebase/security"
    )
    doc_xpath = f'{xpath}/rules'
    xpath = (
        f"/config/devices/entry[@name='{device}']/"
        f"vsys/entry[@name='{vsys}']/rulebase/security"
    )
    rulebase = doc.xpath(doc_xpath)
    rules = rulebase[0]
    entries = rules.xpath('entry')
    notice_end(f'{len(entries)}')
    notice('looking for hip profiles')
    hip_profiles = rules.xpath('entry/hip-profiles')

    for x in hip_profiles:
        x.getparent().remove(x)
    notice_end(f'{len(hip_profiles)}')
    for x in entries:
        notice(f"updating {x.attrib['name']}")
        entry_xpath = f"{xpath}/rules/entry[@name='{x.attrib['name']}']"
        inner_xml = etree.tostring(x).decode('utf-8')
        response = api.post('config', 'edit', xpath=entry_xpath, element=inner_xml)
        notice_end(etree.tostring(response).decode('utf-8'))
