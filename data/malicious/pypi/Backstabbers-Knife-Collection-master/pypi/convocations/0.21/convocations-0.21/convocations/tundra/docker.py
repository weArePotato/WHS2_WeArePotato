import os
from raft import task
from convocations.aws.open_id import sso_login
from convocations.base.utils import notice, notice_end


@task
def download_drivers(ctx, profile=None, **kwargs):
    """
    downloads database drivers from s3 and install them

    ```yaml
    drivers:
      profiles:
        - profile1
        - profile2
      bucket: isos.example.com
      keys:
        - path/to/driver1.zip
        - path/to/driver2.tgz
    ```
    """
    from boto3 import Session
    session = Session()
    profiles = ctx.drivers.profiles
    bucket = ctx.drivers.bucket
    keys = ctx.drivers.keys
    if profile:
        profiles.insert(profile, 0)
    logged_in = set()
    d = './drivers'
    filenames = [ os.path.join(d, os.path.basename(key)) for key in keys ]
    os.makedirs(d, exist_ok=True)
    for x in profiles:
        if x not in session.available_profiles:
            continue
        try:
            if profile not in logged_in:
                sso_login(ctx, profile=profile)
                logged_in.add(profile)
            s3 = session.client('s3')
            for key, filename in zip(keys, filenames):
                notice(f'downloading {filename}')
                if not os.path.exists(filename):
                    s3.download_file(bucket, x, filename)
                    notice_end()
                else:
                    notice_end('already exists')
            break
        except:
            pass


@task
def build_base_image(ctx, profile=None):
    """
    builds the base docker image that we use with airflow.
    """
    download_drivers(ctx, profile)
    image_name = ctx.docker.image
    version = ctx.docker.version
    try:
        docker_file = ctx.docker.dockerfile
    except AttributeError:
        docker_file = 'Dockerfile'
    ctx.run(
        'docker build '
        f'  -t {image_name}:{version} '
        f'  -t {image_name}:latest '
        f'  -f {docker_file}'
        '  .'
    )
