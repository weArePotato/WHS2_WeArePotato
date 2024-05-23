import os.path
from raft import task
from ..aws.base import AwsTask
from ..base.utils import get_context_value, notice, notice_end


@task
def test(ctx, f=None, quiet=False, **kwargs):
    """
    runs pytest against the specified directory with a default `-vvv` option

    ```yaml
    py:
      test_dir: tests
    ```
    :param f: the path to the test directory or to a pytest file
    :param quiet: if specified, changes pytest to regular output mode
    :param ctx:
    :param kwargs:
    """
    f = f or get_context_value(ctx, 'py.test_dir')
    if not f:
        for x in 'test', 'tests':
            if os.path.exists(x):
                f = x
    notice(f'looking for {f}')
    if not os.path.exists(f):
        notice_end(False)
        return
    notice_end()

    verbose = '' if quiet else '-vvv'
    ctx.run(
        'source bin/activate'
        f' && coverage run -m pytest {f} {verbose}'
        ' && coverage report --show-missing',
        pty=True
    )


@task(klass=AwsTask)
def test_with_aws(ctx, f=None, quiet=False, **kwargs):
    """
    runs pytest against the specified directory with a default `-vvv` option
    runs sso_login first in case you are running tests that require
    a waddle config

    ```yaml
    aws:
      profile: default
    py:
      test_dir: tests
    ```
    :param f: the path to the test directory or to a pytest file
    :param quiet: if specified, changes pytest to regular output mode
    :param ctx:
    :param kwargs:
    """
    return test(ctx, f, quiet, **kwargs)
