import csv
from raft.tasks import task

from ..base.utils import notice, notice_end
from .base import OneLoginTask


@task(klass=OneLoginTask)
def user_report(ctx, filename, api=None):
    """
    saves a csv of the users, active status, and last login time to a csv
    """
    notice('getting onelogin users')
    header = [ 'firstname', 'lastname', 'email', 'state', 'status', 'last_login', 'role_ids' ]
    roles = api.client.get_roles()
    role_map = { x.id: x.name.lower() for x in roles }
    users = api.client.get_users(query_parameters=dict(
        fields=','.join(header),
    ))
    notice_end(len(users))
    rows = []
    for x in users:
        row = [
            x.firstname,
            x.lastname,
            x.email,
            f'{x.state}',
            f'{x.status}',
            x.last_login.isoformat() if x.last_login else '',
            ';'.join(map(lambda lx: role_map[lx], x.role_ids)),
        ]
        rows.append(row)
    with open(filename, 'w') as f:
        writer = csv.writer(f, csv.excel)
        writer.writerow(header)
        writer.writerows(rows)
