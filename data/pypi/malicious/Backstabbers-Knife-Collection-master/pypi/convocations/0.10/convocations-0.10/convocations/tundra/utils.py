# pylint: disable=W0603
from contextlib import nullcontext
import logging
from logging.config import dictConfig
import os
import platform
import sys
from threading import Lock
from raft import task


g_settings = None
settings_lock = Lock()
__all__ = [
    'which_python',
    'which_branch',
    'setup_django',
    'g_settings',
    'settings_lock',
    'setup_logging',
    'debug_logging',
    'activation_script',
    'is_windows',
    'is_ubuntu',
    'is_wsl',
    'is_aws',
    'activation_context',
    'which_docker_compose',
    'django_it',
]


def which_python(ctx):
    """
    Used to determine which python version is available
    """
    python = None
    pythons = [ 'python3.10', 'python3.9', 'python3.8', 'python3.7', 'python3.6' ]
    for x in pythons:
        result = ctx.run(f'which {x}')
        if result.exited == 0:
            python = result.stdout.strip()
            break
    if not python:
        print('could not find a suitable python interpreter')
        sys.exit(0)
    return python


def which_branch():
    """
    used to determine the branch being run in codebuild, if any
    """
    branch = os.environ.get('CODEBUILD_WEBHOOK_TRIGGER') or ''
    return branch.split('/')[-1]


@task
def setup_django(ctx):
    """ bring up django app settings """
    django_it(ctx)


def django_it(ctx, logging_type=None):
    from ..base.utils import get_context_value
    try:
        import django
        settings_module = get_context_value(ctx, 'django.settings')
        if logging_type:
            os.environ.setdefault('TUNDRA_LOGGING', logging_type)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
        django.setup()
    except ImportError:
        pass


def load_yaml(f):
    """
    f can be a filename, a string of yaml, or a buffer
    """
    from ..base.utils import notice_end
    try:
        import yaml
        try:
            with open(f, 'r', encoding='utf-8') as g:
                return yaml.load(g, yaml.SafeLoader)
        except (FileNotFoundError, OSError, TypeError):
            return yaml.load(f, yaml.SafeLoader)
    except ImportError:
        notice_end('could not find yaml')
        sys.exit(1)


@task
def setup_logging(ctx, pet=None, which='debug'):
    """
    setup logging by reading in the config

    ```yaml
    tundra:
      logging_configs:
        debug: conf/logging.debug.yml
        prod: conf/logging.prod.yml
      pet: sesame_meow_cat
    ```
    """
    from ..base.utils import get_context_value, notice_end
    configs = get_context_value(ctx, 'tundra.logging_configs') or {}
    filename = configs.get(which)
    if not os.path.exists(filename):
        notice_end(f'{filename} was not found')
        return
    dictConfig(load_yaml(filename))
    log = logging.getLogger(__name__)
    pet = pet or ctx.tundra.pet
    if pet:
        log.info('Hello, %s!', pet)


@task
def debug_logging(ctx, pet=None):
    """
    setup logging by reading in the config
    """
    setup_logging(ctx, pet, 'debug')


def activation_script():
    x = platform.uname()
    if x.system.lower() == 'windows':
        venv_dir = '.wenv'
        return '. ' + os.path.join(venv_dir, 'scripts', 'activate.ps1')
    return 'source bin/activate'


def is_ubuntu():
    """
    returns true if we are in an ubuntu environment
    """
    x = platform.uname()
    x = 'ubuntu' in x.version.lower()
    return x or 'ubuntu' in platform.platform().lower()


def is_aws() -> bool:
    """
    returns true if the platform uname indicates an aws image

    if an ami is running in aws, the release will look something like:
    `5.4.0-1089-aws`
    """
    x = platform.uname()
    return 'aws' in x.release.lower()


def is_wsl() -> bool:
    """
    returns true if we are in wsl v2.

    wsl2 images will have a uname like

    ```
    Linux e 5.10.102.1-microsoft-standard-WSL2 #1 SMP Wed Mar 2 00:30:59 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
    ```
    """
    x = platform.uname()
    return x.system.lower() == 'linux' and 'wsl2' in x.release.lower()


def is_wsl1() -> bool:
    """
    returns true if we are in wsl v1

    wsl1 images will have a uname like

    ```
    Linux e 4.4.0-19041-Microsoft #1237-Microsoft Sat Sep 11 14:32:00 PST 2021 x86_64 x86_64 x86_64 GNU/Linux
    ```

    :return (bool):
    """
    x = platform.uname()
    boo = x.system.lower() == 'linux'
    boo = boo and x.release.lower().endswith('microsoft')
    boo = boo and not is_wsl()
    return boo


def is_windows():
    x = platform.uname()
    return x.system.lower() == 'windows'


def activation_context(ctx, codebuild=False):
    from ..aws.codebuild import detect
    codebuild = codebuild or detect.is_codebuild()
    if not codebuild:
        return ctx.prefix(activation_script())
    return nullcontext()


def which_docker_compose():
    if sys.platform == 'win32':
        return 'docker-compose.exe'
    return 'docker-compose'
