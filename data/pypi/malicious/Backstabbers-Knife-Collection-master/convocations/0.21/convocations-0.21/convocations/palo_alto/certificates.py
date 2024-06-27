import os.path
from uuid import uuid4

from raft import task
from .base import XmlApiTask, XmlApi
from ..base.utils import notice, notice_end


def load_from_s3(session, url):
    notice(f'loading {url}')
    url = url[5:]
    bucket, key = url.split('/', 1)
    s3 = session.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()
    notice_end()
    return content


def load_file(filename):
    notice(f'loading {filename}')
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            content = f.read()
            notice_end()
            return content
    else:
        notice_end(False)
        return None


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
    if pfx.startswith('s3://'):
        p12_data = load_from_s3(session, pfx)
    else:
        p12_data = load_file(pfx)
        if not p12_data:
            return

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


@task(klass=XmlApiTask)
def install_pem(ctx, cert, key=None, passphrase=None,
                host=None, username=None, password=None,
                profile=None, **kwargs):
    """
    installs a cert / keypair to the firewall

    cert or keypair may be specified as an s3 url
    """
    from lxml import etree
    from OpenSSL.crypto import load_certificate
    from OpenSSL.crypto import load_privatekey
    from OpenSSL.crypto import dump_privatekey
    from OpenSSL.crypto import FILETYPE_PEM
    api = XmlApi(host, username, password, profile=profile, **kwargs)
    session = kwargs['session']
    notice(f'loading {cert}')
    if cert.startswith('s3://'):
        cert_content = load_from_s3(session, cert)
    else:
        cert_content = load_file(cert)
        if not cert_content:
            return

    key_content = None
    if key:
        if key.startswith('s3://'):
            key_content = load_from_s3(session, key)
        else:
            key_content = load_file(key)
            if not key_content:
                return
        pem_key = load_privatekey(FILETYPE_PEM, key_content, passphrase=passphrase)
        if not passphrase:
            passphrase = uuid4().hex.encode('utf-8')[:30]
            key_content = dump_privatekey(
                FILETYPE_PEM,
                pem_key,
                passphrase=passphrase)

    pem = load_certificate(FILETYPE_PEM, cert_content)
    name = pem.get_subject()
    name = name.get_components()[0][-1].decode('utf-8')
    notice(f'importing to {host}')
    response = api.import_pem(
        name,
        cert_content,
        key_content,
        passphrase=passphrase)
    success = False
    try:
        success = response.attrib['status'] == 'success'
        notice_end(success)
    except KeyError:
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
