import warnings

from raft import Task
from raft.context import Context
from ..aws.base import make_session


try:
    from urllib3.exceptions import InsecureRequestWarning
    import requests
    import yaml
    from murmuration import kms_wrapped
    from lxml import etree
except ImportError:
    pass


class XmlApiTask(Task):
    def __call__(self, *args, **kwargs):
        ctx = args[0]
        host = kwargs.get('host')
        profile = kwargs.get('profile')
        bucket = kwargs.get('bucket')
        session = kwargs.get('session')
        if isinstance(ctx, Context):
            if profile is None:
                try:
                    profile = ctx.aws.profile
                except AttributeError:
                    pass
            if host is None:
                try:
                    host = ctx.palo_alto.host
                    kwargs['host'] = host
                except AttributeError:
                    pass
            if bucket is None:
                try:
                    bucket = ctx.palo_alto.bucket
                    kwargs['bucket'] = bucket
                except AttributeError:
                    pass
            kwargs['username'] = ctx.palo_alto.username
            kwargs['password'] = ctx.palo_alto.password
        if host and 'username' in kwargs and 'password' in kwargs:
            api = XmlApi(**kwargs)
            kwargs['api'] = api
        session = make_session(profile, session)
        kwargs['session'] = session
        super().__call__(*args, **kwargs)


class XmlApi:
    def __init__(self, host, username=None, password=None, profile=None, **kwargs):
        self.session = requests.Session()
        self.session.verify = False
        self.host = host
        self.base_url = f'https://{self.host}/api/'
        self.generate(host, username, password, profile, **kwargs)

    def generate(self, host, username=None, password=None, profile=None, **kwargs):
        """
        generates an api key using the rest api with the palo alto
        """
        filename = kwargs.get('filename')
        if filename:
            with open(filename, 'r') as f:
                conf = yaml.load(f, Loader=yaml.SafeLoader)
            api_conf = conf.get('api') or {}
            username = username or api_conf.get('username')
            password = password or api_conf.get('password')
            profile = profile or conf.get('profile')
        if password:
            try:
                password = kms_wrapped.decrypt(password, profile=profile)
            except:
                pass
        doc = self.post('keygen', None, user=username, password=password)
        api_key = doc.text
        self.session.headers = {
            'X-PAN-KEY': api_key,
        }

    def raw(self, method, params=None, data=None, files=None):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', category=InsecureRequestWarning)
            response = self.session.request(
                method, self.base_url,
                params=params, data=data, files=files)
            return response

    def get(self, type_, action=None, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = type_
        if action:
            params['action'] = action
        response = self.raw('get', params)
        return self.handle_response(response)

    @classmethod
    def handle_response(cls, response):
        doc = etree.fromstring(response.content)
        if doc.tag == 'response':
            stuff = doc.xpath('/response/result')
            if stuff:
                stuff = stuff[0]
            for x in stuff:
                return x
        print('returning doc as is')
        return doc

    def post(self, type_, action, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = type_
        if action:
            params['action'] = action
        response = self.raw('post', data=params)
        return self.handle_response(response)

    def import_cert(self, name, category, filename, **kwargs):
        params = {}
        params.update(kwargs)
        params['type'] = 'import'
        params['category'] = category
        params['certificate-name'] = name
        params['format'] = 'pem'
        files = {}
        with open(filename, 'r') as f:
            files['file'] = f.read()
        response = self.raw('post', data=params, files=files or None)
        return self.handle_response(response)
