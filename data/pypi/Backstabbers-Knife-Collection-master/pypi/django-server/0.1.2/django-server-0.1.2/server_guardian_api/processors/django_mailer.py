"""django-mailer related processors."""

from django.utils.timezone import now, timedelta

from mailer.models import Message, PRIORITY_DEFERRED

from ..constants import SERVER_STATUS

# TODO find way to make these into settings (maybe dict? only clean namespace?)
# From here up it counts as WARNING
DEFERRED_WARNING_THRESHOLD = 1
# From here up it counts as DANGER
DEFERRED_DANGER_THRESHOLD = 10

QUEUE_WARNING_THRESHOLD = 1
QUEUE_DANGER_THRESHOLD = 100
# time in minutes, when an email is considered "stuck" in the queue and should
# have been sent already
QUEUE_TIMEOUT = 20


def deferred_emails():
    """Checks for deferred email, that otherwise fill up the queue."""
    status = SERVER_STATUS['OK']
    count = Message.objects.deferred().count()

    if DEFERRED_WARNING_THRESHOLD <= count < DEFERRED_DANGER_THRESHOLD:
        status = SERVER_STATUS['WARNING']
    if count >= DEFERRED_DANGER_THRESHOLD:
        status = SERVER_STATUS['DANGER']

    return {
        'label': 'Deferred Email',
        'status': status,
        'info': 'There are currently {0} deferred messages.'.format(count)
    }


def email_queue():
    """Checks for emails, that fill up the queue without getting sent."""
    status = SERVER_STATUS['OK']
    count = Message.objects.exclude(priority=PRIORITY_DEFERRED).filter(
        when_added__lte=now() - timedelta(minutes=QUEUE_TIMEOUT)).count()

    if QUEUE_WARNING_THRESHOLD <= count < QUEUE_DANGER_THRESHOLD:
        status = SERVER_STATUS['WARNING']
    if count >= QUEUE_DANGER_THRESHOLD:
        status = SERVER_STATUS['DANGER']

    return {
        'label': 'Queued Email',
        'status': status,
        'info': 'There are currently {0} messages in the mail queue.'.format(
            count)
    }
