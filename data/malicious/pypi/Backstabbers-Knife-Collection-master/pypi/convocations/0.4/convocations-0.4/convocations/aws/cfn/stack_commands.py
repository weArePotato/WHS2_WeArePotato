import json
import os
from datetime import datetime
from botocore.exceptions import WaiterError
from botocore.exceptions import ClientError
from raft.tasks import task

from ...base.utils import notice_end, notice, print_table, confirm
from ...base.utils import load_yaml
from ..base import AwsTask
from ..base import post_to_slack


__all__ = [
    'upsert',
    'delete_stack',
    'test',
    'sync_template',
    'show_parameters',
    'push_template_to_s3',
    'tail_stack',
]


def cloud_formation_bucket(session):
    s3 = session.resource('s3')
    for x in s3.buckets.all():
        if x.name.startswith('cf-templates') and x.name.endswith(session.region_name):
            return x
    return None


def list_events(stack_name, stack, last_event):
    try:
        events = list(stack.events.all())[::-1]
        n = 0
        found = False
        for x in events:
            if x.id == last_event:
                found = True
                break
            n += 1
        if not found:
            n = -1
        for x in events[n + 1:]:
            status = x.resource_status
            if status.startswith('UPDATE_COMPLETE_'):
                status = status[16:]
            if x.resource_status_reason:
                print(f'{x.logical_resource_id:30} {status:20}'
                      f' {x.resource_status_reason}')
            else:
                print(f'{x.logical_resource_id:30} {status:20}')
        if events:
            event = events[-1]
            resource_status = event.resource_status
            logical_resource_id = event.logical_resource_id
            if logical_resource_id == stack_name and resource_status.endswith('_COMPLETE'):
                return False
            last_event = event.id
    except:
        pass
    return last_event


def wait_for_event(session, stack_name, event_name, last_event=None, n_max=720, delay=3):
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    client = session.client('cloudformation')
    waiter = client.get_waiter(event_name)
    waiter.config.delay = delay
    waiter.config.max_attempts = 1
    n = 0
    while True:
        n += 1
        if n > n_max:
            break
        try:
            waiter.wait(StackName=stack_name)
            list_events(stack_name, stack, last_event)
            break
        except Exception:
            last_event = list_events(stack_name, stack, last_event)
            if last_event is False:
                return


def load_cfn_parameters(ctx, initial=None, prefix=None):
    params = {}
    global_params = os.path.join(prefix, 'params/global.yml')
    files = [ global_params ]
    try:
        files = ctx.aws.global_parameter_files + files
    except AttributeError:
        pass
    for x in files:
        notice(f'loading {os.path.basename(x)}')
        loaded = False
        if os.path.exists(x):
            try:
                y = load_yaml(x)
                if y:
                    params.update(y)
                notice_end()
                loaded = True
            except UnicodeDecodeError:
                pass
        if not loaded:
            notice_end('not found, skipping')
    params.update(initial)
    return params


def push_template_to_s3(stack_name, filename, session):
    """
    filename can be either a filename (/path/to/file or a buffer like io.BytesIO)
    """
    notice('getting cfn bucket')
    bucket = cloud_formation_bucket(session)
    if bucket is None:
        notice_end('not found')
        if isinstance(filename, str):
            with open(filename, 'r') as f:
                data = f.read()
        else:
            data = filename.getvalue()
        return None, data

    notice_end(bucket.name)
    key = datetime.now().strftime(f'{stack_name}/%Y.%m.%d@%H.%I.%S.yml')
    notice('pushing template to s3')
    if isinstance(filename, str):
        with open(filename, 'rb') as data:
            bucket.upload_fileobj(data, key)
    else:
        bucket.upload_fileobj(filename, key)

    template_url = (
        f'https://s3.{session.region_name}.amazonaws.com/'
        f'{bucket.name}/{key}' )
    notice_end(template_url)
    return template_url, None


def template(url, body):
    if url:
        return { 'TemplateURL': url }
    return { 'TemplateBody': body }


def fill_parameter_values(
        ctx, stack_name, template_url, template_body, stack_parameters,
        b_create, session, prefix):
    client = session.client('cloudformation')

    result = client.validate_template(**template(template_url, template_body))
    stack_parameters = stack_parameters or {}
    current_parameters = set()
    if not b_create:
        try:
            stacks = client.describe_stacks(StackName=stack_name)
            for x in stacks['Stacks'][0]['Parameters']:
                current_parameters.add(x['ParameterKey'])
        except:
            pass
    result = result['Parameters']
    local_values = load_cfn_parameters(ctx, stack_parameters, prefix=prefix)
    values = []
    for parameter in result:
        x = parameter['ParameterKey']
        if x in local_values:
            values.append({
                'ParameterKey': x,
                'ParameterValue': local_values[x],
            })
        elif x in current_parameters:
            values.append({
                'ParameterKey': x,
                'UsePreviousValue': True,
            })
    return values


def parameters(ctx, session, prefix, stack_name, filename, b_create=False):
    """
    :param session: a boto3 session
    :param prefix: the dir name
    :param stack_name: the stack name
    :param filename: the /path/to the yaml cloudformation file
     :type filename: str
    :param b_create: whether the parameters should be specified for a
           a create operation or for an update operation
     :type b_create: bool
    :return: a tuple with the yaml file contents as well as the parameter array
     :rtype: (str, str, list[dict])
    """
    template_url, template_body = push_template_to_s3(stack_name, filename, session)
    values = fill_parameter_values(
        ctx, stack_name, template_url, template_body, None,
        b_create, session, prefix)
    return template_url, template_body, values


def parameterized(ctx, session, prefix, stack_name, filename, b_create=False):
    """
    :param session: a boto3 session that can be used to create clients
    :param prefix: the directory name that precedes the `templates` directory
    :param stack_name: the stack name
    :param filename: the /path/to the yaml cloudformation file
     :type filename: str
    :param b_create: whether the parameters should be specified for a
           a create operation or for an update operation
     :type b_create: bool
    :return: a tuple with the yaml file contents as well as the parameter array
     :rtype: (str, bytes, list[dict])
    """
    stack_definition = load_yaml(filename)
    cfn_filename = stack_definition['template']
    template_dir = os.path.join(prefix, 'cfn')
    cfn_filename = os.path.join(template_dir, f'{cfn_filename}.yml')
    stack_parameters = stack_definition['parameters']
    template_url, template_body = push_template_to_s3(
        stack_name, cfn_filename, session)
    values = fill_parameter_values(
        ctx, stack_name, template_url, template_body, stack_parameters,
        b_create, session, prefix)

    return template_url, template_body, values


@task(klass=AwsTask)
def upsert(
        ctx, stack_name, filename=None, force_delete=False,
        timeout=60, disable_rollback=False,
        session=None, prefix='', **kwargs):
    """
    Creates/Updates the cloud formation named <stack_name>
    with the <filename> template
    :param stack_name: The name of the cloud formation stack
    :param filename: The /path/to/the/cloudformation.template
    :param force_delete: <true|false> If the stack exists whether to delete the stack and recreate it
    :param int timeout: Number of minutes for the timeout for cloudformation
    :return:
    """
    cfn = session.resource('cloudformation')
    stack = cfn.Stack(stack_name)
    stack_exists = False
    prefix = prefix or ctx.upholstery.prefix
    original_filename = filename
    params_dir = os.path.join(prefix, 'params')
    template_dir = os.path.join(prefix, 'cfn')
    if not filename:
        filename = os.path.join(params_dir, f'{stack_name}.yml')
    if filename.startswith(params_dir) and os.path.exists(filename):
        parameterized_upsert(
            ctx,
            session,
            prefix,
            stack_name,
            original_filename,
            force_delete,
            timeout)
        return
    if not original_filename:
        filename = os.path.join(template_dir, f'{stack_name}.yml')
    if isinstance(force_delete, str):
        force_delete = force_delete.lower() in [ 'yes', 'true' ]
    try:
        stack.load()
        stack_exists = True
    except:
        pass
    client = session.client('cloudformation')
    if stack_exists and force_delete:
        delete_stack(ctx, stack_name, session=session, prefix=prefix)
        stack_exists = False
    last_event = None
    event_name = 'stack_create_complete'
    post_to_slack(
        ctx, session, 'infrastructure',
        f'[*{prefix}/{stack_name}*] upserting')
    template_url, template_body, values = parameters(
        ctx, session, prefix, stack_name, filename, not stack_exists)
    if not stack_exists:
        notice(f'creating stack [{stack_name}]')
        client.create_stack(
            StackName=stack_name,
            Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
            Parameters=values,
            # OnFailure='DELETE',
            DisableRollback=disable_rollback,
            TimeoutInMinutes=timeout,
            **template(template_url, template_body)
        )
    else:
        notice(f'updating stack [{stack_name}]')
        last_event = next(iter(stack.events.all())).id
        try:
            stack.update(
                Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
                DisableRollback=disable_rollback,
                Parameters=values,
                **template(template_url, template_body)
            )
        except ClientError as ex:
            response = ex.response
            error = response['Error']
            m = error['Message']
            if 'No updates are to be performed' in f'{ex}':
                notice_end('nothing to be done')
                return
            rollback_complete = error['Code'] == 'ValidationError'
            rollback_complete = rollback_complete and 'ROLLBACK_COMPLETE' in m
            if rollback_complete:
                notice_end('state is rollback_complete, nothing doing')
                return
            raise ClientError from ex
        event_name = 'stack_update_complete'

    notice_end('initiated')
    wait_for_event(session, stack_name, event_name, last_event)
    notice(f'{stack_name} upsert')
    notice_end('complete')
    post_to_slack(
        ctx, session, 'infrastructure',
        f'[*{prefix}/{stack_name}*] upserted')
    if stack_name.endswith('-ami'):
        from ..ami_helpers import wait_for_ami
        wait_for_ami(ctx, stack_name[:-4], session=session, prefix=prefix)


def parameterized_upsert(
        ctx, session, prefix, stack_name, filename=None,
        force_delete=False, timeout=30):
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    stack_exists = False
    if not filename:
        filename = os.path.join(prefix, 'params', stack_name + '.yml')
    if not os.path.exists(filename):
        notice_end(f'Could not find file named {filename}')
    if force_delete and isinstance(force_delete, str):
        force_delete = force_delete.lower() in [ 'yes', 'true' ]
    try:
        stack.load()
        stack_exists = True
    except:
        pass
    client = session.client('cloudformation')
    if stack_exists and force_delete:
        delete_stack(ctx, stack_name, session=session, prefix=prefix)
        stack_exists = False
    last_event = None
    event_name = 'stack_create_complete'
    post_to_slack(
        ctx, session, 'infrastructure',
        f'[*{prefix}/{stack_name}*] upserting',)
    template_url, template_body, values = parameterized(
        ctx, session, prefix, stack_name, filename, not stack_exists)
    if not stack_exists:
        notice(f'Creating stack {stack_name}')
        client.create_stack(
            StackName=stack_name,
            Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
            Parameters=values,
            # OnFailure='DELETE',
            TimeoutInMinutes=timeout,
            **template(template_url, template_body)
        )
    else:
        notice(f'Updating stack {stack_name}')
        last_event = next(iter(stack.events.all())).id
        try:
            stack.update(
                Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
                Parameters=values,
                **template(template_url, template_body),
            )
            event_name = 'stack_update_complete'
        except ClientError as ex:
            message = f'{ex}'
            if 'No updates' in message:
                notice_end('no updates')
                post_to_slack(
                    ctx, session, 'infrastructure',
                    f'[*{prefix}/{stack_name}*] nothing done',)
                return
            post_to_slack(
                ctx, session, 'infrastructure',
                f'[*{prefix}/{stack_name}*] nothing done / error')
            raise ex

    notice_end('initiated')
    wait_for_event(session, stack_name, event_name, last_event)
    notice(f'{stack_name} upsert')
    notice_end('complete')
    post_to_slack(
        ctx, session, 'infrastructure',
        f'[*{prefix}/{stack_name}*] upserted')


def print_summary(changes):
    resource_changes = [ x['ResourceChange'] for x in changes if x['Type'] == 'Resource' ]
    header = [ 'resource', 'action', 'replacement', 'type', 'changes', ]
    rows = []
    for x in resource_changes:
        name = x.get('LogicalResourceId')
        name = name or x.get('PhysicalResourceId')
        type_ = x['ResourceType'].split('::')[-1]
        action = x['Action']
        replacement = x.get('Replacement', ' ')
        if action.lower() == 'modify':
            details = x.get('Details') or []
            rg = []
            for change in details:
                evaluation = change.get('Evaluation')
                if evaluation.lower() == 'dynamic':
                    rg.append(change.get('CausingEntity') or '')
                else:
                    t = change['Target'].get('Name')
                    if not t:
                        t = change['Target']['Attribute']
                    rg.append(t)
            rg = filter(None, rg)
            change_summary = ', '.join(rg)
            change_summary = change_summary or ' '
        else:
            change_summary = ' '

        fields = [ name, action, replacement, type_, change_summary ]
        rows.append(fields)
    print_table(header, rows)


@task(klass=AwsTask)
def test(
        ctx, stack_name, filename=None, verbose=None, session=None,
        prefix=None, **kwargs):
    """
    Creates/Updates the cloud formation named <stack_name>
    with the <filename> template
    :param session: boto3 session (passed in from decorator)
    :param prefix: passed in from partial
    :param stack_name: The name of the cloud formation stack
    :param filename: The /path/to/the/cloudformation.template
    :param verbose: specify the verbose flag to indicate that you want verbose output instead of
      summary output
    :return:
    """
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    stack_exists = False
    prefix = prefix or ctx.upholstery.prefix
    original_filename = filename
    params_dir = os.path.join(prefix, 'params')
    template_dir = os.path.join(prefix, 'cfn')
    if not filename:
        filename = os.path.join(params_dir, f'{stack_name}.yml')
    if filename.startswith(params_dir) and os.path.exists(filename):
        parameterized_test(
            ctx, session, prefix, stack_name, original_filename, verbose)
        return
    if not original_filename:
        filename = os.path.join(template_dir, f'{stack_name}.yml')
    try:
        stack.load()
        stack_exists = True
    except:
        pass
    client = session.client('cloudformation')
    name = datetime.now().strftime(stack_name + '-%Y%m%d-%H%M')
    change_set_type = 'UPDATE' if stack_exists else 'CREATE'
    template_url, template_body, values = parameters(
        ctx, session, prefix, stack_name, filename, not stack_exists)
    notice(f'testing changes to [{stack_name}]')
    client.create_change_set(
        ChangeSetName=name,
        ChangeSetType=change_set_type,
        StackName=stack_name,
        Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
        Parameters=values,
        **template(template_url, template_body),
    )
    waiter = client.get_waiter('change_set_create_complete')
    try:
        waiter.wait(ChangeSetName=name, StackName=stack_name)
    except WaiterError:
        pass
    data = client.describe_change_set(
        ChangeSetName=name,
        StackName=stack_name,
    )
    if data:
        reason = data.get('StatusReason', '')
        if reason.startswith(
            "The submitted information didn't contain changes"
        ):
            notice_end('nothing to be done')
            return
        changes = data['Changes']
        if verbose:
            print(json.dumps(changes, indent=2))
        else:
            print_summary(changes)

        client.delete_change_set(
            ChangeSetName=name,
            StackName=stack_name,)
    notice_end('done')


def parameterized_test(ctx, session, prefix, stack_name,
                       filename=None, verbose=None):
    """
    <stack_name>,<filename>,verbose -- Creates/Updates the cloud formation named <stack_name>
    with the <filename> template
    :param session: the boto3 session passed in from the decorator
    :param prefix: the prefix (e.g., dbuy or leaseco) passed in from partial
    :param stack_name: The name of the cloud formation stack
    :param filename: The /path/to/the/cloudformation.template
    :param verbose: specify the verbose flag to indicate that you want verbose output instead of
      summary output
    :return:
    """
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    stack_exists = False
    params_dir = os.path.join(prefix, 'params')
    if not filename:
        filename = os.path.join(params_dir, stack_name + '.yml')
    if not os.path.exists(filename):
        notice(f'Could not find [{filename}]')
        notice_end('done')
        return
    try:
        stack.load()
        stack_exists = True
    except:
        pass
    client = session.client('cloudformation')
    name = datetime.now().strftime(stack_name + '-%Y%m%d-%H%M')
    change_set_type = 'UPDATE' if stack_exists else 'CREATE'
    template_url, template_body, values = parameterized(
        ctx, session, prefix, stack_name, filename, not stack_exists)
    notice(f'testing changes to [{stack_name}]')
    client.create_change_set(
        ChangeSetName=name,
        ChangeSetType=change_set_type,
        StackName=stack_name,
        Capabilities=[ 'CAPABILITY_NAMED_IAM' ],
        Parameters=values,
        **template(template_url, template_body),
    )
    try:
        waiter = client.get_waiter('change_set_create_complete')
        waiter.wait(ChangeSetName=name, StackName=stack_name)
        data = client.describe_change_set(
            ChangeSetName=name,
            StackName=stack_name,
        )
        changes = data['Changes']
        if verbose:
            print(f'{json.dumps(changes, indent=2)}')
        else:
            print_summary(changes)
        notice_end('done')
    except WaiterError:
        notice_end('up to date')
    client.delete_change_set(
        ChangeSetName=name,
        StackName=stack_name,
    )


@task(klass=AwsTask)
def delete_stack(ctx, stack_name, session=None, prefix='', **kwargs):
    """
    <stack_name> -- Deletes the specified cloud formation stack named <stack_name>
    :param ctx: the convocation context
    :param stack_name: The name of the cloud formation stack
    :param session: the boto3 session passed in from the decorator
    :param prefix: the prefix passed in from partial
    """
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    stack_exists = False
    if not prefix:
        prefix = ctx.upholstery.prefix
    try:
        stack.load()
        stack_exists = True
    except:
        pass
    if stack_exists:
        if not confirm(f'You are requesting deletion of stack [{stack_name}]'):
            return
        post_to_slack(
            ctx, session, 'infrastructure',
            f'[*{prefix}/{stack_name}*] deleting')
        last_event = next(iter(stack.events.all())).id
        notice(f'Deleting existing stack {stack_name}')
        stack.delete()
        notice_end()
        wait_for_event(session, stack_name, 'stack_delete_complete', last_event)
        notice(f'{stack_name} deletion')
        notice_end('complete')
        post_to_slack(
            ctx, session, 'infrastructure',
            f'[*{prefix}/{stack_name}*] deleted')


@task(klass=AwsTask)
def sync_template(ctx, stack_name, with_parameters=False,
                  session=None, prefix=None, **kwargs):
    """
    pulls the latest template from cfn and saves it to the cfn directory
    """
    from convocations.base.utils import yaml_serializer
    cfn = session.client('cloudformation')
    response = cfn.get_template(StackName=stack_name)
    body = response['TemplateBody']
    prefix = prefix or ctx.upholstery.prefix
    filename = os.path.join(prefix, 'cfn', f'{stack_name}.yml')
    with open(filename, 'w') as f:
        if isinstance(body, dict):
            body = json.loads(json.dumps(body))
            yaml_serializer().dump(body, f)
        else:
            f.write(body)
            f.write('\n')
    if with_parameters:
        parameter_response = cfn.describe_stacks(StackName=stack_name)
        p = parameter_response['Stacks'][0]['Parameters']
        filename = os.path.join(prefix, 'params', f'{stack_name}.yml')
        data = dict(template=stack_name, parameters={
            x['ParameterKey']: x['ParameterValue']
            for x in p
        })
        with open(filename, 'w') as f:
            data = json.loads(json.dumps(data))
            yaml_serializer().dump(data, f)


@task(klass=AwsTask)
def show_parameters(ctx, name, session=None, **kwargs):
    cfn = session.client('cloudformation')
    result = cfn.describe_stacks(StackName=name)
    stack = result['Stacks'][0]
    mp = stack['Parameters']
    for x in mp:
        notice(x['ParameterKey'])
        notice_end(x['ParameterValue'])
    return mp


@task(klass=AwsTask)
def tail_stack(ctx, stack_name, event_name='stack_update_complete',
               n_max=360, delay=10,
               session=None, **kwargs):
    """
    tails all stack events for the given stack until event_name is reached
    delay is the delay between polling
    n_max is the max number of polls for events
    """
    last_event = None
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    stack.load()
    for x in list(stack.events.all())[:5]:
        last_event = x.id
    wait_for_event(session, stack_name, event_name, last_event, n_max, delay)
