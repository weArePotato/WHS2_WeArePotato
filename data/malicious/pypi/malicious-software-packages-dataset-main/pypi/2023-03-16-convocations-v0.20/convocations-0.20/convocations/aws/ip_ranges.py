import requests
from raft import task
from convocations.base.utils import print_table
from convocations.base.utils import notice, notice_end


@task
def ip_ranges(ctx, region='us-east-2', service='amazon'):
    """
    filters aws public ip ranges by region and service
    """
    notice('getting ip ranges')
    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    response = requests.get(url, timeout=10)
    data = response.json()
    prefixes = data['prefixes']
    notice_end(f'{len(prefixes)}')
    notice('filtering for region / service')
    i = 0
    rows = []
    for x in prefixes:
        if x['region'] == region and x['service'].lower() == service.lower():
            rows.append([ x['ip_prefix'] ])
            i += 1
    notice_end(f'{i}')
    print_table([ 'cidr' ], rows)
