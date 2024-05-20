
import os
from glob import iglob

from raft import task


@task
def upload_files(ctx, source, site_name, destination):
    """
    uploads files specified by source to a specified sharepoint site folder

    source can be a glob
    """
    import adal
    from office365.runtime.auth.token_response import TokenResponse
    from office365.sharepoint.client_context import ClientContext
    from office365.sharepoint.folders.folder import Folder
    sharepoint_base_url = f'https://{ctx.tenant_name}.sharepoint.com'
    site_url = f'{sharepoint_base_url}/sites/{site_name}'
    authority = f'https://login.microsoftonline.com/{ctx.tenant_id}'
    app = adal.AuthenticationContext(authority)
    token_json = app.acquire_token_with_client_certificate(
        sharepoint_base_url,
        ctx.client_id,
        ctx.key,
        ctx.thumbprint,
    )
    session = ClientContext(site_url).with_access_token(
        lambda: TokenResponse.from_json(token_json)
    )
    destination = destination.replace('Documents', 'Shared Documents')
    destination = os.path.join('/sites', site_name, destination)
    folder = session.web.get_folder_by_server_relative_path(destination)
    folder: Folder = folder.get().execute_query()
    for x in iglob(source):
        print(f'uploading {x} => {folder.name}')
        with open(x, 'rb') as f:
            folder.upload_file(os.path.basename(x), f.read()).execute_query()
