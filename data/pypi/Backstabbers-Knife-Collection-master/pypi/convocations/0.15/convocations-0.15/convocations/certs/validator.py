from typing import List, Optional
from cryptography import x509
from cryptography.x509.name import NameAttribute, ObjectIdentifier
from cryptography.hazmat.backends import default_backend
from cryptography.x509.extensions import ExtensionNotFound
from raft import task
from ..base.utils import notice, notice_end
from ..base.utils import print_table


def read_chain(filename: str) -> List[bytes]:
    with open(filename, 'r') as f:
        data = f.read()
    data = data.split('-----END CERTIFICATE-----')
    data = [ x.strip() for x in data ]
    return [ f'{x}\n-----END CERTIFICATE-----\n'.encode('ascii') for x in filter(None, data) ]


def common_name(x: x509.name.Name) -> Optional[str]:
    oid: ObjectIdentifier = ObjectIdentifier('2.5.4.3')
    attributes: List[NameAttribute] = x.get_attributes_for_oid(oid)
    if not attributes:
        return None
    return attributes[0].value


def yield_bytes(st):
    for x in range(0, len(st), 2):
        yield st[x:x + 2]


def get_extension(x, key: str) -> x509.extensions.Extension:
    oid: ObjectIdentifier = ObjectIdentifier(key)
    e: x509.extensions.Extension = x.extensions.get_extension_for_oid(oid)
    return e


def subject_fingerprint(x) -> Optional[str]:
    e = get_extension(x, '2.5.29.14')
    key_id: x509.extensions.SubjectKeyIdentifier = e.value
    return ':'.join(yield_bytes(key_id.digest.hex()))


def issuer_fingerprint(x) -> Optional[str]:
    try:
        e = get_extension(x, '2.5.29.35')
        key_id: x509.extensions.AuthorityKeyIdentifier = e.value
        return ':'.join(yield_bytes(key_id.key_identifier.hex()))
    except ExtensionNotFound:
        return ''


@task
def validate_chain(ctx, filename):
    """
    validates a bundled crt file
    """
    backend = default_backend()
    certs = read_chain(filename)
    values, values2 = [], []
    for cert in certs:
        cert = x509.load_pem_x509_certificate(cert, backend)
        subject = common_name(cert.subject)
        issuer = common_name(cert.issuer)
        subject_key = subject_fingerprint(cert)
        issuer_key = issuer_fingerprint(cert)
        expiration = cert.not_valid_after.strftime('%Y-%m-%d')
        values.append([ subject, issuer, expiration ])
        values2.append([ subject_key, issuer_key ])
    notice('validating issuer chain')
    valid = True
    for x in range(1, len(values2)):
        if values2[x][0] != values2[x - 1][-1]:
            valid = False
    if valid:
        notice_end()
    else:
        notice_end('invalid')
    print()
    print_table([ 'subject', 'issuer', 'expiration', ], values)
    print()
    print_table([ 'subject fingerprint', 'issuer fingerprint', ], values2)
