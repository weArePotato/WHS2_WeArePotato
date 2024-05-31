import os
import sys
from raft import task


@task
def global_python(ctx, pythons=None):
    """
    finds a global python interpreter in order of preference
    :param ctx:
    :param pythons:
    :return:
    """
    possible = pythons or [
        'python3.10',
        'python3.9',
        'python3.8',
        'python3.7',
        'python3.6',
    ]
    for x in possible:
        result = ctx.run(f'which {x}', warn=True)
        if result.ok:
            return result.stdout.strip()
    for x in possible:
        st = x.replace('.', '')
        st = os.path.join('/', st, 'python.exe')
        if os.path.exists(st):
            return st
    return None


@task
def setup(ctx, name=None):
    """
    creates the virtual environment and installs prerequisites
    """
    from ..aws.codebuild.detect import is_codebuild
    if is_codebuild():
        from ..aws.codebuild import setup as cb_setup
        cb_setup(ctx)
        return

    default_name = '.'
    if sys.platform in ('linux', 'darwin'):
        default_name = ctx.venv_name if 'venv_name' in ctx else '.'
    elif sys.platform == 'win32':
        default_name = ctx.windows_venv_name if 'windows_venv_name' in ctx else '.wenv'
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
        result = ctx.run(f'{pip} -U pip setuptools raft', pty=True)
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
