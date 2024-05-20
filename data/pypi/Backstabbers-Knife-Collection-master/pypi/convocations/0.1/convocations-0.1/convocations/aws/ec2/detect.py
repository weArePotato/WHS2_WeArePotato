import os


def detect_ec2(ctx):
    """
    detects whether the current convocation is running in ec2
    by checking the /sys/hypervisor/uuid file
    """
    if os.path.exists('/sys/hypervisor/uuid'):
        result = ctx.run('head -c 3 /sys/hypervisor/uuid')
        return result.stdout.startswith('ec2')
    return False
