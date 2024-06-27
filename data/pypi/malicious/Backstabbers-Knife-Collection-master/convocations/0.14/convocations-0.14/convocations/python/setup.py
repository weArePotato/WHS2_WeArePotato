import os
import sys
from raft import task

from convocations.base.utils import get_context_value


@task
def global_python(ctx, pythons=None):
    """
    finds a global python interpreter in order of preference

    example config:

    ```yaml
    py:
      pythons:
        - /path/to/python3.8
        - /path/to/python2.7
    ```
    :param ctx:
    :param pythons:
    :return:
    """
    possible = pythons or get_context_value(ctx, 'py.pythons') or [
        'python3.10',
        'python3.9',
        'python3.8',
        'python3.7',
        'python3.6',
    ]
    if sys.platform != 'win32':
        for x in possible:
            result = ctx.run(f'which {x}', warn=True)
            if result.ok:
                return result.stdout.strip()
    else:
        for x in possible:
            st = x.replace('.', '')
            st = os.path.join('/', st, 'python.exe')
            if os.path.exists(st):
                return st
        result = ctx.run('(Get-Command python).source', warn=True)
        if result.ok:
            return result.stdout.strip()
    return None


@task
def setup(ctx, name=None):
    """
    creates the virtual environment and installs prerequisites
    example config:

    ```yaml
    py:
      venv_name: .venv
      windows_venv_name: .wenv
    ```
    """
    from ..aws.codebuild.detect import is_codebuild
    if is_codebuild():
        from ..aws.codebuild import setup as cb_setup
        cb_setup(ctx)
        return

    default_name = '.'
    if sys.platform in ('linux', 'darwin'):
        default_name = get_context_value(ctx, 'py.venv_name', '.')
    elif sys.platform == 'win32':
        default_name = get_context_value(ctx, 'py.windows_venv_name', '.wenv')
    name = name or default_name
    expected_python = os.path.join(name, 'bin', 'python')
    if not os.path.exists(expected_python):
        python = global_python(ctx)
        ctx.run(f'{python} -m venv {name}')
    if os.path.exists(expected_python):
        python = expected_python
        pip = f'{python} -m pip install'
        result = ctx.run(f'{pip} -U wheel', pty=True)
        if result.exited:
            return
        result = ctx.run(f'{pip} -U raft', pty=True)
        if result.exited:
            return
        result = ctx.run(f'{pip} -r requirements.txt', pty=True)
        if result.exited:
            return
        if os.path.exists('setup.py'):
            result = ctx.run(f'{pip} -e .', pty=True)
            if result.exited:
                return
    else:
        print('no suitable python version found')
