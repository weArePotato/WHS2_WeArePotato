# helpers for use with aws resource access manager
from raft.tasks import task
from ...base.utils import notice
from ...base.utils import notice_end
from ..base import AwsTask


__all__ = [
    'accept_sharing_invitation',
]


@task(klass=AwsTask)
def accept_sharing_invitation(ctx, name, session=None, **kwargs):
    """
    Accepts the sharing invitation with the provided name

    n.b., the first invitation containing name will be accepted
          the comparison is case-insensitive
    """
    ram = session.client('ram')
    notice('looking for invitations')
    response = ram.get_resource_share_invitations()
    results = response.get('resourceShareInvitations')
    for x in results:
        if x['status'] != 'PENDING':
            continue
        invitation_name = x['resourceShareName'].lower()
        notice('name')
        notice_end(invitation_name)
        if name.lower() in invitation_name:
            notice_end(f'{invitation_name}')
            notice(f'accepting {invitation_name}')
            arn = x['resourceShareInvitationArn']
            ram.accept_resource_share_invitation(
                resourceShareInvitationArn=arn
            )
            notice_end()
            return
    if not results:
        notice_end('no invitations found')
        return
    notice_end()
