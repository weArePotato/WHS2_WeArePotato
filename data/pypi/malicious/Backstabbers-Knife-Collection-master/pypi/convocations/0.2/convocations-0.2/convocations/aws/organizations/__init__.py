import os
from collections import defaultdict
import json

from raft import task

from ...base.utils import notice
from ...base.utils import notice_end
from ...base.utils import print_table
from ..base import AwsTask
from ..base import yielder


def list_org_accounts(session):
    notice('getting accounts')
    organization = session.client('organizations')
    # paginator = organization.get_paginator('list_accounts')
    # accounts = []
    # for x in paginator.paginate():
    #     accounts += x['Accounts']
    config = dict(PaginationConfig=dict(MaxItems=100))
    accounts = list(yielder(organization, 'list_accounts', **config))
    notice_end(f'{len(accounts)}')
    return accounts


@task(klass=AwsTask)
def org_accounts(ctx, session=None, **kwargs):
    """
    lists all accounts in the organization in a nice tabular format
    """
    accounts = list_org_accounts(session)
    print()
    accounts.sort(key=lambda lx: lx['Name'].lower())
    # header = [ 'name', 'id', 'email' ]
    header = [ 'name', 'id', ]
    rows = []
    for x in accounts:
        rows.append([
            x['Name'],
            x['Id'],
            # x['Email'],
        ])
    print_table(header, rows)


@task(klass=AwsTask)
def sso_groups(ctx, name=None, session=None, **kwargs):
    """
    lists all groups in the aws sso in a nice tabular format
    """
    notice('getting instances')
    client = session.client('sso-admin')
    response = client.list_instances(MaxResults=10)
    notice_end()
    instances = response['Instances']
    if not instances:
        return
    header = [ 'arn', 'identity_store_id', ]
    rows = []
    for x in instances:
        rows.append([
            x['InstanceArn'],
            x['IdentityStoreId'],
        ])
    print('===================')
    print_table(header, rows)
    print('===================')
    identity_store_id = instances[0]['IdentityStoreId']
    identity_store = session.client('identitystore')
    kwargs = dict(IdentityStoreId=identity_store_id)
    groups = list(yielder(identity_store, 'list_groups', **kwargs))
    header = [ 'group_id', 'name', 'external_id' ]
    rows = []
    if name:
        name = name.lower()
    for x in groups:
        display_name = x['DisplayName'].lower()
        if name and name not in display_name:
            continue
        rg = [
            x['GroupId'],
            x['DisplayName'],
        ]
        external_ids = x.get('ExternalIds') or []
        external_id = ''
        if external_ids:
            external_id = external_ids[0]['Id']
        rg.append(external_id)
        rows.append(rg)
    print_table(header, rows)


@task(klass=AwsTask)
def export_permission_sets(ctx, filename, session=None, prefix=None, **kwargs):
    """
    exports permission set to cloud formation
    """
    if not filename.endswith('.yml'):
        filename = f'{filename}.yml'
    notice('getting instance arns')
    sso_admin = session.client('sso-admin')
    instances = sso_admin.list_instances()
    instances = instances['Instances']
    permission_sets = defaultdict(list)
    notice_end(f'{len(instances)}')
    for instance in instances:
        instance_arn = instance['InstanceArn']
        notice(f'permission sets for {instance_arn}')
        g = yielder(
            sso_admin,
            'list_permission_sets',
            InstanceArn=instance_arn)
        rg = list(g)
        notice_end(f'{len(rg)}')
        permission_sets[instance_arn] = rg
    exports = {}
    n = 0
    for instance_arn, permission_set_arns in permission_sets.items():
        for permission_set_arn in permission_set_arns:
            n += 1
            notice(f'exporting {permission_set_arn}')
            permission_set = sso_admin.describe_permission_set(
                PermissionSetArn=permission_set_arn,
                InstanceArn=instance_arn,
            )['PermissionSet']
            managed_policies = sso_admin.list_managed_policies_in_permission_set(
                InstanceArn=instance_arn,
                PermissionSetArn=permission_set_arn,
                MaxResults=100,
            )['AttachedManagedPolicies']
            inline_policy = sso_admin.get_inline_policy_for_permission_set(
                InstanceArn=instance_arn,
                PermissionSetArn=permission_set_arn,
            )['InlinePolicy']
            exported_permission_set = dict(
                InstanceArn=instance_arn,
                Name=permission_set['Name'],
                SessionDuration=permission_set['SessionDuration'],
            )
            description = permission_set.get('Description')
            if description:
                exported_permission_set['Description'] = description
            managed_policies = [ x['Arn'] for x in managed_policies ]
            if managed_policies:
                exported_permission_set['ManagedPolicies'] = managed_policies
            if inline_policy:
                exported_permission_set['InlinePolicy'] = json.loads(inline_policy)
            exports[f'PermissionSet{n:02d}'] = dict(
                Type='AWS::SSO::PermissionSet',
                Properties=exported_permission_set
            )
            notice_end()
    p = os.path.join(prefix, 'cfn', filename)
    with open(p, 'w') as f:
        from convocations.base.utils import yaml_serializer
        template = dict(
            AWSTemplateFormatVersion='2010-09-09',
            Resources=exports,
        )
        yaml_serializer().dump(template, f)


@task(klass=AwsTask)
def export_assignments(ctx, identity_store_id, filename, session=None, prefix=None, **kwargs):
    """
    exports permission set to cloud formation
    """
    if not filename.endswith('.yml'):
        filename = f'{filename}.yml'
    notice('getting instance arns')
    sso_admin = session.client('sso-admin')
    instances = sso_admin.list_instances()
    instances = instances['Instances']
    notice_end(f'{len(instances)}')

    identity_store = session.client('identitystore')
    user_map = {}
    group_map = {}
    accounts = list_org_accounts(session)
    exports = {}
    n = 0
    for instance in instances:
        instance_arn = instance['InstanceArn']
        for account in accounts:
            account_id = account['Id']
            g = yielder(
                sso_admin,
                'list_permission_sets_provisioned_to_account',
                InstanceArn=instance_arn,
                AccountId=account_id,
                PaginationConfig=dict(MaxItems=100))
            for permission_set_arn in g:
                h = yielder(
                    sso_admin,
                    'list_account_assignments',
                    InstanceArn=instance_arn,
                    AccountId=account_id,
                    PermissionSetArn=permission_set_arn,
                    PaginationConfig=dict(PageSize=100))
                for assignment in h:
                    n += 1
                    principal_id = assignment['PrincipalId']
                    principal_type = assignment['PrincipalType']
                    if principal_type == 'GROUP':
                        if principal_id not in group_map:
                            r = identity_store.describe_group(
                                IdentityStoreId=identity_store_id,
                                GroupId=principal_id
                            )
                            group_map[principal_id] = r['DisplayName']
                        principal_id = group_map.get(principal_id)
                    else:
                        if principal_id not in user_map:
                            r = identity_store.describe_user(
                                IdentityStoreId=identity_store_id,
                                UserId=principal_id
                            )
                            user_map[principal_id] = r['UserName']
                        principal_id = user_map[principal_id]
                    props = dict(
                        InstanceArn=instance_arn,
                        TargetType='AWS_ACCOUNT',
                        TargetId=account_id,
                        PermissionSetArn=permission_set_arn,
                        PrincipalId=principal_id,
                        PrincipalType=principal_type,
                    )
                    exports[f'Assignment{n:03}'] = dict(
                        Type='AWS::SSO::Assignment',
                        Properties=props,
                    )

    p = os.path.join(prefix, 'cfn', filename)
    with open(p, 'w') as f:
        from convocations.base.utils import yaml_serializer
        template = dict(
            AWSTemplateFormatVersion='2010-09-09',
            Resources=exports,
        )
        yaml_serializer().dump(template, f)
