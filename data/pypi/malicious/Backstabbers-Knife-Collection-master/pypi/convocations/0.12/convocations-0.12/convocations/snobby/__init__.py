import os
from raft.tasks import Task, task


class SnobbyTask(Task):
    def __init__(self, *args, **kwargs):
        self.playbook = kwargs.pop('playbook')
        self.inventory = 'hosts'
        self.limit = kwargs.pop('limit', None)
        self.extra = {}
        for key, value in kwargs.items():
            if key not in (
                    'body',
                    'name',
                    'aliases',
                    'positional',
                    'optional',
                    'default',
                    'auto_shortflags',
                    'help',
                    'pre',
                    'post',
                    'autoprint',
                    'iterable',
                    'incrementable',
            ):
                self.extra[key] = value
        for key in self.extra:
            kwargs.pop(key)
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        ctx = args[0]
        extra = []
        limit = kwargs.pop('limit', None) or self.limit
        tags = kwargs.pop('tags', None) or ''
        verbose = kwargs.pop('verbose', False)
        if tags:
            tags = f'--tags {tags}'
        for key, value in self.extra.items():
            extra.append(f'-e {key}={value}')
        for key, value in kwargs.items():
            extra.append(f'-e {key}={value}')
        if verbose:
            extra.append('-vvvv')
        extra = ' '.join(extra)
        if limit:
            limit = f'--limit {limit}'
        command = (
            'ansible-playbook '
            f' -i {self.inventory}'
            f" {limit or ''}"
            f' {self.playbook}'
            f' {extra}'
            f' {tags}'
        )
        if os.path.isfile('./ansible.cfg') and 'ANSIBLE_CONFIG' not in os.environ:
            os.environ['ANSIBLE_CONFIG'] = './ansible.cfg'
        ctx.run(command, pty=True)
