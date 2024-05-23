from raft.tasks import task
from ...base.utils import print_table
from ..base import AwsTask, yielder

__all__ = [
    'search_s3',
    'add_name_tag_to_bucket',
]


@task(klass=AwsTask)
def search_s3(bucket, prefix, session=None, **kwargs):
    """
    searches the bucket at the given prefix, recursively, and prints
    matching content
    """
    s3 = session.client('s3')
    method = 'list_objects_v2'
    suffixes = [ 'b', 'kb', 'mb', 'gb', 'tb' ]
    config = dict(
        Bucket=bucket,
        Prefix=prefix,
        PaginationConfig={
            'PageSize': 1000,
        })
    header = [ 'key', 'last_modified', 'file_size' ]
    rows = []
    for x in yielder(s3, method, session, **config):
        file_size = x['Size']
        n_suffix = 0
        while file_size > 1024 and n_suffix < len(suffixes):
            n_suffix += 1
            file_size /= 1024
        rows.append([
            x['Key'],
            x['LastModified'].isoformat(),
            f"{file_size:.2f}{suffixes[n_suffix]}"
        ])
    print_table(header, rows)


@task(klass=AwsTask)
def add_name_tag_to_bucket(ctx, for_reals=False, session=None, profile=None, **kwargs):
    """
    adds a name tag to all s3 buckets with the same name as the bucket name
    """
    from botocore.exceptions import ClientError
    s3 = session.client('s3')
    response = s3.list_buckets()
    for x in response['Buckets']:
        bucket = x['Name']
        try:
            tagging = s3.get_bucket_tagging(Bucket=bucket)
            tags = { tag['Key']: tag['Value'] for tag in tagging['TagSet'] }
        except ClientError:
            tags = {}
        if 'Name' not in tags:
            print(f'[{bucket}] adding Name tag')
            tags['Name'] = bucket
            tag_set = [ dict(Key=key, Value=value) for key, value in tags.items() ]
            if for_reals:
                s3.put_bucket_tagging(
                    Bucket=bucket,
                    Tagging=dict(TagSet=tag_set))
