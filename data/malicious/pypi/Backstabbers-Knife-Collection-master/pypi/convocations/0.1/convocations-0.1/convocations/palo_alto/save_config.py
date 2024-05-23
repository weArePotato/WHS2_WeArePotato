from raft import task
from .base import XmlApiTask, XmlApi


try:
    from lxml import etree
except ImportError:
    pass


@task(klass=XmlApiTask)
def save_config(ctx, host=None, bucket=None, config=None, **kwargs):
    """
    saves off the running config from the specified hosts.
    if bucket is specified, the config is saved as the bootstrap
    config in the specified bucket
    """
    api = kwargs.get('api')
    api = api or XmlApi(host, filename=config)
    doc = api.get('config', 'show')
    if not bucket:
        print(etree.tostring(doc, pretty_print=True).decode('utf-8'))
    else:
        from ..aws.base import make_session
        session = kwargs.get('session')
        session = make_session(kwargs.get('profile'), session)
        s3 = session.client('s3')
        s3.put_object(
            Bucket=bucket,
            Key='config/bootstrap.xml',
            Body=etree.tostring(doc, pretty_print=True))


@task(klass=XmlApiTask)
def export_config(ctx, host=None, bucket=None, config=None, **kwargs):
    """
    exports the running config from the specified hosts.
    if bucket is specified, the config is saved as the bootstrap
    config in the specified bucket
    """
    api = XmlApi(host, filename=config)
    doc = api.get('export', category='configuration', )
    if not bucket:
        print(etree.tostring(doc, pretty_print=True).decode('utf-8'))
    else:
        from ..aws.base import make_session
        session = kwargs.get('session')
        session = make_session(kwargs.get('profile'), session)
        s3 = session.client('s3')
        s3.put_object(
            Bucket=bucket,
            Key='config/bootstrap.xml',
            Body=etree.tostring(doc, pretty_print=True))
