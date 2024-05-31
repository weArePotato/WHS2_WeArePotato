from raft import task
from .base import XmlApiTask, XmlApi
from ..base.utils import notice, notice_end

try:
    from lxml import etree
except ImportError:
    pass


@task(klass=XmlApiTask)
def save_config(ctx, host=None, bucket=None, username=None, password=None,
                api=None, session=None, **kwargs):
    """
    saves off the running config from the specified hosts.
    if bucket is specified, the config is saved as the bootstrap
    config in the specified bucket
    """
    notice('getting config')
    api = api or XmlApi(host, username, password, session=session)
    doc = api.get('config', 'show')
    config = etree.tostring(doc, pretty_print=True)
    notice_end()
    if not bucket:
        print(config.decode('utf-8'))
    else:
        key = f'{host}/config.xml'
        notice(f'upload to s3://{bucket}/{key}')
        s3 = session.client('s3')
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=etree.tostring(doc, pretty_print=True))
        notice_end()


@task(klass=XmlApiTask)
def export_config(ctx, host=None, bucket=None, session=None, username=None,
                  password=None, api=None, **kwargs):
    """
    exports the running config from the specified hosts.
    if bucket is specified, the config is saved as the bootstrap
    config in the specified bucket
    """
    notice('exporting config')
    api = api or XmlApi(host, username, password, session.profile_name)
    doc = api.get('export', category='configuration', )
    config = etree.tostring(doc, pretty_print=True)
    notice_end()
    if not bucket:
        print(config.decode('utf-8'))
    else:
        key = f'{host}/config.xml'
        notice(f'upload to s3://{bucket}/{key}')
        s3 = session.client('s3')
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=etree.tostring(doc, pretty_print=True))
        notice_end()
