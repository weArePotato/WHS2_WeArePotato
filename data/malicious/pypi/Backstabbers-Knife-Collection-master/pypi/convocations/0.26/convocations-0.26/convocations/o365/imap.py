from imaplib import IMAP4_SSL as Imap
from raft import task


@task
def test_imap(ctx, user, filename='conf/dev.yml'):
    """
    tests imap connectivity via oauth to office 365
    """
    from requests_oauthlib import OAuth2Session
    from oauthlib.oauth2 import BackendApplicationClient
    from waddle import load_config
    conf = load_config(filename)
    client_id = conf.imap.client_id
    client_secret = conf.imap.client_secret
    scope = ' '.join(conf.imap.scopes)
    token_url = conf.imap.token_url
    client = BackendApplicationClient(
        client_id=client_id,
        scope=scope,
    )
    session = OAuth2Session(client=client)
    session.fetch_token(
        token_url,
        scope=scope,
        client_secret=client_secret)
    access_token = session.access_token
    auth = f'user={user}\1auth=Bearer {access_token}\1\1'.encode('utf-8')
    mbox = Imap('outlook.office365.com', 993)
    mbox.debug = 4
    mbox.authenticate('XOAUTH2', lambda lx: auth)
    mbox.select('Inbox', True)
    mbox.close()
