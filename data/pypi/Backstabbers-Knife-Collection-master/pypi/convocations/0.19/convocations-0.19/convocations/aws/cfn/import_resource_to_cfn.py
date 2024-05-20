import os
from collections import OrderedDict
from uuid import uuid4
from ...base.utils import notice, notice_end


def to_pascal_case(m, exclude=None):
    """
    the cfn for many ecs resources closely resembles the
    structure needed by cloudformation.  we can easily convert
    api format to cloudformation format by pascal casing the
    values we get back from the api.

    recursively works across lists and dicts as needed to
    pascal case all keys.  Returns scalars as-is.

    e.g., roleArn => RoleArn
    """
    if not m:
        return None
    if isinstance(m, (dict, OrderedDict)):
        result = {}
        for key, value in m.items():
            key = f'{key[0].upper()}{key[1:]}'
            if isinstance(value, (dict, OrderedDict, list)):
                if not exclude or key not in exclude:
                    value = to_pascal_case(value, exclude)
                if value is not None:
                    result[key] = value
            else:
                result[key] = value
        return result or None
    if isinstance(m, list):
        result = [ to_pascal_case(x, exclude) for x in m ]
        return result or None
    return m


def cfn_filename(prefix, stack_name):
    filename = stack_name or f'{stack_name}.yml'
    if not filename.endswith('.yml'):
        filename = f'{filename}.yml'
    stack_name, _ = os.path.splitext(filename)
    filepath = os.path.join(prefix, 'cfn', filename)
    return filepath, stack_name


def update_template(filepath, data):
    from ruamel.yaml import load, RoundTripLoader
    from ...base.utils import yaml_serializer
    notice(f'updating {filepath}')
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            template_body = load(f, RoundTripLoader)
        template_body['Resources'].update(data)
    else:
        template_body = dict(
            AWSTemplateFormatVersion='2010-09-09',
            Description='imported via upholstery',
            Resources=data,
        )
        notice_end('not found')
    with open(filepath, 'w') as f:
        yaml_serializer().dump(template_body, f)
    notice_end()


def import_resource_to_cfn(
        data, resources_to_import,
        filename, name, skip_review=False,
        session=None, prefix=None):
    from .stack_commands import wait_for_event
    from .stack_commands import push_template_to_s3
    filepath, stack_name = cfn_filename(prefix, filename or name)
    update_template(filepath, data)
    url, template_body = push_template_to_s3(stack_name, filepath, session)
    cfn = session.client('cloudformation')
    cfn_resource = session.resource('cloudformation')
    kwargs = {}
    try:
        stack = cfn_resource.Stack(stack_name)
        stack.load()
        kwargs['Parameters'] = [
            dict(
                ParameterKey=param['ParameterKey'],
                UsePreviousValue=True)
            for param in stack.parameters ]
    except:
        pass
    change_set_name = f'{stack_name}-{uuid4().hex}'
    notice('creating change set')
    if url:
        kwargs['TemplateURL'] = url
    else:
        kwargs['TemplateBody'] = template_body
    cfn.create_change_set(
        StackName=stack_name,
        ChangeSetName=change_set_name,
        ChangeSetType='IMPORT',
        ResourcesToImport=resources_to_import,
        **kwargs
    )
    notice_end(change_set_name)
    if skip_review:
        waiter = cfn.get_waiter('change_set_create_complete')
        kwargs = dict(
            ChangeSetName=change_set_name,
            StackName=stack_name
        )
        waiter.wait(WaiterConfig=dict(Delay=1), **kwargs)
        notice(f'executing {change_set_name}')
        cfn.execute_change_set(**kwargs)
        notice_end()
        wait_for_event(session, stack_name, 'stack_import_complete', None)


def sync_resource(prefix, filename, data):
    """
    fixes drift in a template by updating one resource with the data provided
    """
    filepath, _ = cfn_filename(prefix, filename)
    update_template(filepath, data)


def filtered_tags(obj):
    """
    removes cloudformation tags from the tags array
    """
    tags = obj.get('tags') or []
    return [ x for x in tags if x['key'][:4] != 'aws:' ]
