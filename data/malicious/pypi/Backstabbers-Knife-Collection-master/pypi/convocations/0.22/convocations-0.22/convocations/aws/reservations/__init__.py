import json
import os
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

from raft import task
from ...base.utils import notice, notice_end, print_table
from ..base import AwsTask, yielder
from ..base import name_tag
from ..ec2 import get_tag


def signature(data, region):
    instance_type = data['InstanceType']
    scope = data['Scope']
    if scope == 'Availability Zone':
        scope = data['AvailabilityZone']
    else:
        scope = region
    product = data['ProductDescription']
    if 'windows' in product.lower():
        product = 'windows'
    else:
        product = 'linux'
    return scope, product, instance_type


def instance_sig(instance):
    availability_zone = instance['Placement']['AvailabilityZone']
    product = instance.get('Platform', 'linux')
    product = product.lower()
    instance_type = instance['InstanceType']
    return availability_zone, product, instance_type


def described_instances(result):
    for r in result['Reservations']:
        for instance in r['Instances']:
            if instance['State']['Name'].lower() == 'running':
                yield instance


@task(klass=AwsTask)
def reservation_report(ctx, pricing=False, purchase=False, session=None, **kwargs):
    """
    produces an excel report of all instances and reservations

    The report will have two tabs:
      raw_data will show all of the instances, and the pricing comparison
         between reserved and on-demand pricing.  We use instance tags
         to determine which instances should be reserved.
         We will also try to do our best to indicate if we see a reservation
         in place that matches the instance so that we know which instances
         tagged reserved have a reservation in place and those that need one
         to purchase.
      the counts sheet will show all of the counts for reservations that we
         should purchase.  i.e., the breakdown by availability-zone and
         instance type of instances that are tagged reserved, but for
         which we do not see an active reservation.

    You can use the `--purchase` flag to initiate purchases of reservations
    in accordance with the counts sheet in the report.
    """
    from pandas import DataFrame
    from pandas import ExcelWriter
    client = session.client('ec2')
    notice('loading reservations')
    reservations = client.describe_reserved_instances()
    notice_end()
    notice('loading instances')
    result = client.describe_instances()
    instances = list(described_instances(result))
    while result.get('NextToken'):
        result = client.describe_instances(NextToken=result['NextToken'])
        instances += list(described_instances(result))
    notice_end(f'{len(instances)}')
    costs = defaultdict(lambda: defaultdict(dict))
    on_demand = defaultdict(lambda: defaultdict(dict))
    if pricing:
        costs, on_demand = reservation_pricing(ctx, session=session, quiet=True)
    sigs = []
    reservation_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
    reserved = []
    for reservation in reservations['ReservedInstances']:
        sig = signature(reservation, session.region_name)
        sigs.append(sig)
        if reservation['State'] in ('active', 'payment-pending'):
            n = reservation['InstanceCount']
            reservation_counts[sig[0]][sig[1]][sig[2]] += n

    region = session.region_name
    mantissa = Decimal('0.001')
    for instance in instances:
        sig = instance_sig(instance)
        n = reservation_counts[sig[0]][sig[1]][sig[2]]
        name = name_tag(instance)
        reservation = get_tag(instance, 'reserved').lower() == 'true'
        rg = costs[sig[0]][sig[1]][sig[2]]
        offering_id, hourly = ' ', Decimal(0)
        if rg and len(rg) == 2:
            offering_id, hourly = rg
        hourly = Decimal(hourly).quantize(mantissa, ROUND_HALF_UP)
        monthly = hourly * Decimal(730)
        on_demand_hourly = on_demand[sig[0]][sig[1]][sig[2]]
        on_demand_monthly = on_demand_hourly * Decimal(730)
        if n > 0 and reservation:
            reserved.append({
                'name': name,
                'status': 'reserved',
                # 'reservation_id': reservation_id,
                'instance_type': sig[2],
                'product': sig[1],
                'availability_zone': sig[0],
                'region': region,
                'reservation_tag': reservation,
                'offering_id': offering_id,
                'on_demand_hourly': float(on_demand_hourly),
                'on_demand_monthly': float(on_demand_monthly),
                'reserved_hourly': float(hourly),
                'reserved_monthly': float(monthly),
                'monthly': float(monthly if reservation else on_demand_monthly),
            })
            reservation_counts[sig[0]][sig[1]][sig[2]] -= 1
            continue
        n = reservation_counts[region][sig[1]][sig[2]]
        if n > 0 and reservation:
            reserved.append({
                'name': name,
                'status': 'reserved',
                # 'reservation_id': reservation_id,
                'instance_type': sig[2],
                'product': sig[1],
                'availability_zone': sig[0],
                'region': region,
                'reservation_tag': reservation,
                'offering_id': offering_id,
                'on_demand_hourly': float(on_demand_hourly),
                'on_demand_monthly': float(on_demand_monthly),
                'reserved_hourly': float(hourly),
                'reserved_monthly': float(monthly),
                'monthly': float(monthly if reservation else on_demand_monthly),
            })
            reservation_counts[region][sig[1]][sig[2]] -= 1
            continue
        reserved.append({
            'name': name,
            'status': 'not reserved',
            # 'reservation_id': reservation_id,
            'instance_type': sig[2],
            'product': sig[1],
            'availability_zone': sig[0],
            'region': region,
            'reservation_tag': reservation,
            'offering_id': offering_id,
            'on_demand_hourly': float(on_demand_hourly),
            'on_demand_monthly': float(on_demand_monthly),
            'reserved_hourly': float(hourly),
            'reserved_monthly': float(monthly),
            'monthly': float(monthly if reservation else on_demand_monthly),
        })
    for sig in sigs:
        n = reservation_counts[sig[0]][sig[1]][sig[2]]
        for x in range(n):
            reserved.append({
                'name': 'reservation',
                'status': 'unused',
                'instance_type': sig[2],
                'product': sig[1],
                'availability_zone': sig[0],
                'region': region,
                'reservation_tag': None,
                'offering_id': None,
                'on_demand_hourly': None,
                'on_demand_monthly': None,
                'reserved_hourly': None,
                'reserved_monthly': None,
                'monthly': None,
            })

    os.makedirs('./reports', exist_ok=True)
    profile = kwargs.get('prefix') or session.alias or kwargs.get('profile') or session.profile_name
    profile = profile.lower().replace(' ', '_').replace('-', '_')
    df = DataFrame(reserved)
    filename = f'./reports/{profile}_reservation_report.xlsx'
    writer = ExcelWriter(filename)  # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, sheet_name='raw_data')
    df_counts = df[df['reservation_tag'] == True]  # pylint: disable=singleton-comparison
    df_counts = df_counts[df_counts['status'] == 'not reserved']
    header = [ 'availability_zone', 'instance_type', 'product', 'offering_id', ]
    df_counts = df_counts.groupby(header)
    df_counts = df_counts.size().reset_index()
    df_counts['n'] = df_counts[0]
    df_counts = df_counts[header + [ 'n' ]]
    df_counts.to_excel(writer, sheet_name='counts')
    writer.save()
    if not purchase:
        return
    to_purchase = df_counts.to_dict('records')
    for x in to_purchase:
        instance_type = x['instance_type']
        offering_id = x['offering_id']
        n = x['n']
        notice(f'purchasing {offering_id} / {instance_type} / {n}')
        response = client.purchase_reserved_instances_offering(
            ReservedInstancesOfferingId=offering_id,
            InstanceCount=n,
        )
        notice_end(response['ReservedInstancesId'])


@task(klass=AwsTask)
def on_demand_pricing(ctx, instances, session=None, **kwargs):
    """
    gets on-demand pricing for our instances
    """
    pricing = session.client('pricing', region_name='us-east-1')
    region = session.region_name
    costs = defaultdict(lambda: defaultdict(dict))
    for instance in instances:
        sig = instance_sig(instance)
        costs[sig[0]][sig[1]][sig[2]] = Decimal(0)
    prices = []
    for zone, v1 in costs.items():
        v1_values = list(v1.items())
        for product, v2 in v1_values:
            v2_values = list(v2.items())
            for instance_type, values in v2_values:
                filters = [
                    dict(Type='TERM_MATCH', Field='tenancy', Value='shared'),
                    dict(Type='TERM_MATCH', Field='operatingSystem', Value=product),
                    dict(Type='TERM_MATCH', Field='instanceType', Value=instance_type),
                    dict(Type='TERM_MATCH', Field='usagetype', Value=f'USE2-BoxUsage:{instance_type}'),
                    dict(Type='TERM_MATCH', Field='licenseModel', Value='No License required'),
                    dict(Type='TERM_MATCH', Field='preInstalledSw', Value='NA')
                ]
                if region not in ('us-east-1', 'us-west-2'):
                    filters.append(dict(Type='TERM_MATCH', Field='regionCode', Value=region))
                result = pricing.get_products(
                    ServiceCode='AmazonEC2',
                    Filters=filters, FormatVersion='aws_v1')
                if not result['PriceList']:
                    continue
                p = result['PriceList'][0]
                p = json.loads(p)
                for t1 in p['terms']['OnDemand'].values():
                    for t2 in t1['priceDimensions'].values():
                        hourly = t2['pricePerUnit']['USD']
                        hourly = Decimal(hourly).quantize(Decimal('0.0001'), ROUND_HALF_UP)
                        v2[instance_type] = hourly
                        prices.append({
                            'az': zone,
                            'product': product,
                            'type': instance_type,
                            'hourly': hourly,
                            'monthly': hourly * Decimal(365 * 2),
                            'yearly': hourly * Decimal(365 * 24),
                        })
    # header = [ 'az', 'product', 'type', 'hourly', 'monthly', 'yearly' ]
    # rows = []
    # for x in prices:
    #     row = [ x[key] for key in header ]
    #     rows.append(row)
    # print_table(header, rows)
    return costs


@task(klass=AwsTask)
def reservation_pricing(ctx, quiet=False, session=None, **kwargs):
    """
    compares up-front and reserved pricing costs
    """
    ec2 = session.client('ec2')
    costs = defaultdict(lambda: defaultdict(dict))
    on_demand_costs = None
    notice('instances')
    instances = list(yielder(ec2, 'describe_instances'))
    notice_end()
    for instance in instances:
        sig = instance_sig(instance)
        costs[sig[0]][sig[1]][sig[2]] = Decimal(0)
    i = 0
    offerings = []
    for zone, v1 in costs.items():
        v1_values = list(v1.items())
        for product, v2 in v1_values:
            v2_values = list(v2.items())
            for instance_type, values in v2_values:
                i += 1
                if not quiet:
                    notice(f'reservation info page {i}')
                d = 'Windows' if product == 'windows' else 'Linux/UNIX'
                result = ec2.describe_reserved_instances_offerings(
                    OfferingClass='standard',
                    InstanceTenancy='default',
                    InstanceType=instance_type,
                    MinDuration=365 * 24 * 60 * 60,
                    MaxDuration=365 * 24 * 60 * 60,
                    OfferingType='No Upfront',
                    ProductDescription=d,
                )
                for x in result['ReservedInstancesOfferings']:
                    if x['Scope'].lower() != 'region':
                        continue
                    amount = Decimal(x['RecurringCharges'][0]['Amount'])
                    amount = amount.quantize(Decimal('0.001'), ROUND_HALF_UP)
                    yearly = amount * Decimal(24 * 365)
                    monthly = Decimal(yearly) / Decimal(12)
                    hourly = Decimal(yearly) / Decimal(365 * 24)
                    st_id = x['ReservedInstancesOfferingId']
                    v2[instance_type] = (st_id, hourly)
                    offerings.append({
                        'az': zone,
                        'product': product,
                        'type': instance_type,
                        'hourly': hourly,
                        'monthly': monthly,
                        'yearly': yearly,
                    })
                if not quiet:
                    notice_end()
    if not quiet:
        header = [ 'az', 'product', 'type', 'hourly', 'monthly', 'yearly' ]
        rows = []
        for x in offerings:
            row = [ x[key] for key in header ]
            rows.append(row)
        print_table(header, rows)
    on_demand_costs = on_demand_pricing(ctx, instances, session=session)
    return costs, on_demand_costs
