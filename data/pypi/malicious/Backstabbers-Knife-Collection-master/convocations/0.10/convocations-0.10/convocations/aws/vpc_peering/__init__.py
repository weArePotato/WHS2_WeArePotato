from raft.tasks import task
from ...base.utils import notice, notice_end
from ..base import AwsTask


__all__ = [
    'peer_vpc',
]


@task(klass=AwsTask)
def peer_vpc(ctx, vpc_id, peer_vpc_id, peer_owner_id, peer_region, session=None):
    """
    creates peering request from one vpc to another
    """
    notice(f'initiating peering from {vpc_id} to {peer_vpc_id}')
    ec2 = session.client('ec2')
    response = ec2.create_vpc_peering_connection(
        PeerVpcId=peer_vpc_id,
        PeerOwnerId=peer_owner_id,
        VpcId=vpc_id,
        PeerRegion=peer_region,
    )
    notice_end()
    print(response)
