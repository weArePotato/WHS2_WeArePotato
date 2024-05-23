def yield_logs(group, stream, start_time=None, session=None, client=None):
    """
    yields log lines from the specified group and stream from the specified
    start time onwards
    """
    client = client or session.client('logs')
    kwargs = {
        'logGroupName': group,
        'logStreamName': stream,
        'startFromHead': True,
    }
    if start_time:
        kwargs['startTime'] = start_time + 1
    next_token = 'sesame'
    while next_token:
        last_token = next_token
        response = client.get_log_events(**kwargs)
        if not response['events']:
            break
        yield from response['events']
        next_token = response.get('nextForwardToken')
        if next_token == last_token:
            break
        kwargs['nextToken'] = next_token
