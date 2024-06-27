from raft.tasks import task
from convocations.base.utils import print_table, notice, notice_end
from .base import CheckpointTask


@task(klass=CheckpointTask)
def services(ctx, exp='', protocol='tcp', host=None, client=None, **kwargs):
    """
    filters available services by expression
    """
    from cpapi.api_response import APIResponse
    payload = dict(limit=500)
    command = f'show-services-{protocol}'
    exp = exp.lower()
    response: APIResponse = client.api_call(command, payload=payload)
    print(f'{response.data}')
    total = response.data['total']
    rg = response.data['objects']
    if total > 500:
        payload['offset'] = 0
        while total > 0:
            total -= 500
            payload['offset'] += 500
            response = client.api_call(command, payload)
            rg += response.data['objects']
    rg = filter(lambda lx: exp in lx['name'].lower(), rg)
    header = [ 'name', 'type', 'port' ]
    rows = [ [ x.get('name'), x.get('type'), x.get('port') ] for x in rg ]
    print_table(header, rows)
    return rg


@task(klass=CheckpointTask)
def service(ctx, name, groups=True, protocol='tcp',
            host=None, client=None, prefix='', quiet=False, **kwargs):
    """
    shows the available service named `name`
    """
    from cpapi.api_response import APIResponse
    command = f'show-service-{protocol}'
    payload = dict(name=name)
    if not quiet:
        notice(f'{prefix}loading service')
    response: APIResponse = client.api_call(command, payload=payload)
    data = response.data
    if not quiet:
        notice_end(data['name'])
        notice(f'{prefix}port')
        notice_end(data['port'])
        notice(f'{prefix}protocol')
        notice_end(data.get('protocol'))
        if groups:
            groups = data.get('groups') or []
            for group in groups:
                notice(f'{prefix}group')
                notice_end(group['name'])
    return data


@task(klass=CheckpointTask)
def service_group(ctx, name, host=None, client=None, **kwargs):
    """
    shows the available service group named `name`
    """
    from cpapi.api_response import APIResponse
    command = 'show-service-group'
    payload = dict(name=name)
    notice('loading service group')
    response: APIResponse = client.api_call(command, payload=payload)
    group_data = response.data
    notice_end(group_data['name'])
    rows = []
    members = group_data['members']
    print()
    header = [ 'name', 'port', 'protocol', 'type' ]
    for x in members:
        service_data = service(ctx, name=x['name'], client=client, quiet=True)
        rows.append([
            x['name'],
            service_data['port'],
            service_data['protocol'],
            service_data['type'].replace('service-', '') ])
        x.update(service_data)
    print_table(header, rows)
    return group_data
