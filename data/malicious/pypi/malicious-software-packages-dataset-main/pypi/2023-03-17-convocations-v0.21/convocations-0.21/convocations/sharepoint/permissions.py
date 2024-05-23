from typing import Iterable
from typing import List

from raft import task


@task(help=dict(perms='read, write, or manage'), iterable=['perms'])
def grant_access(ctx, site_name, app_name, perms=None):
    """
    grants the app with name app_name read and write permissions to the site_name sharepoint site

    this convocation is useful when you have created an azure application
    registration with api permission Sites.Selected and need to authorize
    the application to connect to a particular sharepoint site.
    """
    from msal import ConfidentialClientApplication
    from office365.graph_client import GraphClient
    from office365.directory.applications.application import Application
    from office365.sharepoint.sites.site import Site
    perms = perms or [ 'read', 'write' ]
    app = ConfidentialClientApplication(
        authority=f'https://login.microsoftonline.com/{ctx.tenant_id}',
        client_id=ctx.client_id,
        client_credential=ctx.client_secret,
    )
    sharepoint_base_url = f'https://{ctx.tenant_name}.sharepoint.com'
    token_json = app.acquire_token_for_client(scopes=[
        # f'{sharepoint_base_url}/.default',
        'https://graph.microsoft.com/.default',
    ])
    site_url = f'{sharepoint_base_url}/sites/{site_name}'
    session = GraphClient(lambda: token_json)
    result: Iterable[Application] = session.applications.get().execute_query()
    app_id = None
    for x in result:
        if x.display_name.lower() == app_name.lower():
            app_id = x.id
            break
    if not app_id:
        print(f'could not find {app_name} in azure application directory')
    print(f'{app_name} => {app_id}')
    site: Site = session.sites.get_by_url(site_url).execute_query()
    print(f'{site.name} => {site.id}')
    result = site.permissions.add(
        roles=perms,
        grantedToIdentities=[{
            'application': {
                'id': app_id,
                'displayName': app_name,
            }
        }],
    ).execute_query()
    print(result.roles)


@task
def check_access(ctx, site_name, app_name):
    """
    checks the permissions for the app with name app_name
    on the site_name sharepoint site

    this convocation is useful when you have created an azure application
    registration with api permission Sites.Selected and need to authorize
    the application to connect to a particular sharepoint site.
    """
    from msal import ConfidentialClientApplication
    from office365.graph_client import GraphClient
    from office365.directory.applications.application import Application
    from office365.sharepoint.sites.site import Site
    from office365.onedrive.permissions.permission import Permission
    from office365.directory.identities.identity_set import IdentitySet
    app = ConfidentialClientApplication(
        authority=f'https://login.microsoftonline.com/{ctx.tenant_id}',
        client_id=ctx.client_id,
        client_credential=ctx.client_secret,
    )
    sharepoint_base_url = f'https://{ctx.tenant_name}.sharepoint.com'
    token_json = app.acquire_token_for_client(scopes=[
        # f'{sharepoint_base_url}/.default',
        'https://graph.microsoft.com/.default',
    ])
    site_url = f'{sharepoint_base_url}/sites/{site_name}'
    session = GraphClient(lambda: token_json)
    result: Iterable[Application] = session.applications.get().execute_query()
    app_id = None
    for x in result:
        if x.display_name.lower() == app_name.lower():
            app_id = x.id
            break
    if not app_id:
        print(f'could not find {app_name} in azure application directory')
    print(f'{app_name} => {app_id}')
    site: Site = session.sites.get_by_url(site_url).execute_query()
    print(f'{site.name} => {site.id}')
    result: List[Permission] = site.permissions.get().execute_query()
    for x in result:
        p: Permission = x.get().execute_query()
        sets: List[IdentitySet] = p.granted_to_identities
        for identity_set in sets:
            print(
                p.roles,
                identity_set.application.id,
                identity_set.application.displayName)
