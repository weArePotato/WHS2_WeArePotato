import os.path
from uuid import uuid4

from raft import task
from .base import XmlApiTask, XmlApi
from ..base.utils import notice, notice_end


@task(klass=XmlApiTask)
def install_pfx(ctx, pfx, pfx_password=None,
                host=None, username=None, password=None,
                profile=None, **kwargs):
    """
    installs a cert to the firewall
    """
    from lxml import etree
    from OpenSSL.crypto import load_pkcs12
    api = XmlApi(host, username, password, profile=profile, **kwargs)
    session = kwargs['session']
    notice(f'loading {pfx}')
    if pfx.startswith('s3://'):
        pfx = pfx[5:]
        bucket, key = pfx.split('/', 1)
        s3 = session.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        p12_data = response['Body'].read()
        notice_end()
    else:
        if os.path.exists(pfx):
            notice_end()
        else:
            notice_end(False)
            return
        with open(pfx, 'rb') as f:
            p12_data = f.read()

    p12 = load_pkcs12(p12_data, pfx_password)
    if not pfx_password:
        pfx_password = uuid4().hex.encode('utf-8')[:30]
        p12_data = p12.export(pfx_password)
    name = p12.get_certificate().get_subject()
    name = name.get_components()[0][-1].decode('utf-8')
    notice(f'importing to {host}')
    response = api.import_pfx(name, p12_data, pfx_password)
    success = response.attrib['status'] == 'success'
    notice_end(success)
    if not success:
        print(etree.tostring(response, pretty_print=True).decode())
    else:
        notice('committing')
        response = api.commit('updated ssl certificate')
        if response.tag == 'msg':
            line = response.xpath('.//line')
            if line:
                line = line[0]
                notice_end(line.text.lower())
            else:
                notice_end(False)
                print(etree.tostring(response, pretty_print=True).decode())
        else:
            notice_end(False)
            print(etree.tostring(response, pretty_print=True).decode())
