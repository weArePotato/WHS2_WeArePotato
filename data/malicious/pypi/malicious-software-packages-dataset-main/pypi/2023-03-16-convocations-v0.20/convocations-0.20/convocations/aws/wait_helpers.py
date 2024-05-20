from botocore.exceptions import WaiterError
from ..base.utils import notice
from ..base.utils import notice_end


def wait(waiter, message, **kwargs):
    config = kwargs.pop('WaiterConfig', None)
    config = config or {}
    config.setdefault('Delay', 15)
    config.setdefault('MaxAttempts', 2)
    for n in range(1, 41):
        notice(f'waiting for {message} {n}/40')
        try:
            waiter.wait(WaiterConfig=config, **kwargs)
        except WaiterError:
            notice_end('not yet')
        else:
            notice_end()
            break
