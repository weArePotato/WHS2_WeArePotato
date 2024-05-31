import time

from raft import task
from ...base.utils import notice, notice_end, confirm
from ...base.utils import print_table
from ..ec2 import get_tag
from ..base import AwsTask, name_tag


@task(klass=AwsTask)
def transit_routes(ctx, session=None, profile=None, **kwargs):
    """
    lists all transit gateway routes
    """
    notice('getting transit gateway route tables')
    ec2 = session.client('ec2')
    gateways = ec2.describe_transit_gateway_route_tables()
    table_ids = [
        x['TransitGatewayRouteTableId']
        for x in gateways['TransitGatewayRouteTables']
    ]
    notice_end()
    print_table([ 'table id' ], [ [ x ] for x in table_ids ])
    rows = []
    header = [ 'table_id', 'cidr', 'type', 'resource_id', 'account', 'name', ]
    attachments = {}
    for table_id in table_ids:
        notice(f'getting routes for {table_id}')
        routes = ec2.search_transit_gateway_routes(
            TransitGatewayRouteTableId=table_id,
            Filters=[{
                'Name': 'state',
                'Values': [ 'active', ],
            }]
        )
        for route in routes['Routes']:
            attachment = route['TransitGatewayAttachments'][0]
            attachment_id = attachment['TransitGatewayAttachmentId']
            row = [
                table_id,
                route['DestinationCidrBlock'],
                attachment['ResourceType'],
                attachment['ResourceId'],
            ]
            detail = attachments.get(attachment_id)
            if not detail:
                detail = ec2.describe_transit_gateway_attachments(
                    TransitGatewayAttachmentIds=[
                        attachment_id,
                    ],
                )
                detail = detail['TransitGatewayAttachments'][0]
            account = detail['ResourceOwnerId']
            name = get_tag(detail, 'Name')
            row.append(account)
            row.append(name or '')
            rows.append(row)
        notice_end()
    print()
    print_table(header, rows)


@task(klass=AwsTask)
def accept_resource_shares(ctx, session=None, profile=None, **kwargs):
    """
    accepts any pending resource shares
    """
    notice('getting invitations')
    ram = session.client('ram')
    invitations = ram.get_resource_share_invitations()
    invitations = invitations['resourceShareInvitations']
    invitations = [ x for x in invitations if x['status'] == 'PENDING' ]
    notice_end(f'{len(invitations)} pending invitations')
    for x in invitations:
        arn = x['resourceShareInvitationArn']
        account_id = x['senderAccountId']
        notice(f'accepting {account_id} / {arn}')
        ram.accept_resource_share_invitation(resourceShareInvitationArn=arn)
        notice_end()


@task(klass=AwsTask)
def accept_pending_tgw_attachments(ctx, session=None, profile=None, **kwargs):
    """
    accepts any pending resource shares
    """
    notice('getting pending attachments')
    ec2 = session.client('ec2')
    attachments = ec2.describe_transit_gateway_attachments(Filters=[dict(
        Name='state',
        Values=[
            'pending',
            'pendingAcceptance',
        ]
    )])
    attachments = list(attachments['TransitGatewayAttachments'])
    notice_end(f'{len(attachments)} pending')
    for x in attachments:
        n_id = x['TransitGatewayAttachmentId']
        owner = x['ResourceOwnerId']
        resource_type = x['ResourceType']
        if confirm(f'accept {owner} / {n_id}'):
            notice('accepting')
            if resource_type == 'vpc':
                ec2.accept_transit_gateway_vpc_attachment(
                    TransitGatewayAttachmentId=n_id
                )
            elif resource_type == 'peering':
                ec2.accept_transit_gateway_peering_attachment(
                    TransitGatewayAttachmentId=n_id
                )
            notice_end()


@task(klass=AwsTask)
def tgw_attachments(ctx, session=None, **kwargs):
    """
    lists all tgw attachments
    """
    ec2 = session.client('ec2')
    attachments = ec2.describe_transit_gateway_attachments()
    attachments = attachments['TransitGatewayAttachments']
    attachments = [ x for x in attachments if x['State'] != 'deleted' ]
    header = [ 'id', 'name', 'route_table' ]
    rows = []
    for x in attachments:
        rows.append([
            x['TransitGatewayAttachmentId'],
            name_tag(x),
            x.get('Association', {}).get('TransitGatewayRouteTableId') or ''
        ])
    rows.sort(key=lambda lx: (lx[1], lx[0]))
    print()
    print_table(header, rows)


@task(klass=AwsTask)
def associate_tgw_attachment(ctx, attachment_id, route_table_id, session=None, **kwargs):
    """
    moves the transit gateway attachment to the specified route table
    """
    ec2 = session.client('ec2')
    attachments = ec2.describe_transit_gateway_attachments(
        TransitGatewayAttachmentIds=[ attachment_id ],
    )
    attachments = attachments['TransitGatewayAttachments']
    if not attachments:
        notice_end('not found')
        return
    x = attachments[0]
    current_route_table_id = x.get('Association', {}).get('TransitGatewayRouteTableId') or ''
    if current_route_table_id == route_table_id:
        notice_end('already associated')
        return
    if current_route_table_id:
        notice(f'disassociating from {current_route_table_id}')
        ec2.disassociate_transit_gateway_route_table(
            TransitGatewayRouteTableId=current_route_table_id,
            TransitGatewayAttachmentId=attachment_id,
        )
        notice_end()
    notice(f'associating to {route_table_id}')
    time.sleep(30)
    ec2.associate_transit_gateway_route_table(
        TransitGatewayRouteTableId=route_table_id,
        TransitGatewayAttachmentId=attachment_id,
    )
    notice_end()
