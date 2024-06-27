from tempfile import NamedTemporaryFile
from uuid import uuid4

from raft import task
from .base import XmlApiTask


@task(klass=XmlApiTask)
def install_cert(ctx, name, cert, key, **kwargs):
    """
    installs a cert to the firewall
    """
    from lxml import etree
    from OpenSSL.crypto import dump_privatekey
    from OpenSSL.crypto import load_privatekey
    from OpenSSL.crypto import FILETYPE_PEM
    api = kwargs['api']
    passphrase = uuid4().hex
    with open(key, 'rb') as f:
        x509_key = load_privatekey(FILETYPE_PEM, f.read())
    with NamedTemporaryFile('wb', buffering=1) as f:
        st = dump_privatekey(
            FILETYPE_PEM,
            x509_key,
            passphrase=passphrase.encode())
        f.write(st)
        f.flush()

        response = api.import_cert(name, 'certificate', cert)
        print(etree.tostring(response, pretty_print=True).decode())

        response = api.import_cert(
            name, 'private-key', f.name, passphrase=passphrase)
        print(etree.tostring(response, pretty_print=True).decode())
