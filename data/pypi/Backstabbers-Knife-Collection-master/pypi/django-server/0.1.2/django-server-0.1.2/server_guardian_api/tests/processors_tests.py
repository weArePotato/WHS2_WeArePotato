"""Tests for the processors for django-mailer."""
from django.test import TestCase
from django.utils.timezone import now, timedelta

from mailer.models import PRIORITY_DEFERRED, PRIORITY_MEDIUM
from mixer.backend.django import mixer

from ..constants import SERVER_STATUS
from ..processors.django_mailer import deferred_emails, email_queue


class MailerDeferredEmailsProcessorTestCase(TestCase):
    """Test case for the ``deferred_emails`` django-mailer processor."""
    longMessage = True

    def setUp(self):
        self.normal_messages = mixer.cycle(10).blend(
            'mailer.Message', priority=PRIORITY_MEDIUM)

    def test_deferred_emails(self):
        self.assertEqual(
            deferred_emails()['status'],
            SERVER_STATUS['OK'],
            msg='Without deferred emails, the status should be OK.'
        )

        mixer.cycle(1).blend('mailer.Message', priority=PRIORITY_DEFERRED)
        self.assertEqual(
            deferred_emails()['status'],
            SERVER_STATUS['WARNING'],
            msg='With 1 deferred email, the status should be WARNING.'
        )

        mixer.cycle(9).blend('mailer.Message', priority=PRIORITY_DEFERRED)
        self.assertEqual(
            deferred_emails()['status'],
            SERVER_STATUS['DANGER'],
            msg='With 10 deferred emails, the status should be DANGER.'
        )


class MailerEmailQueueProcessorTestCase(TestCase):
    """Test case for the ``email_queue`` django-mailer processor."""
    longMessage = True

    def setUp(self):
        self.deferred_messages = mixer.cycle(5).blend(
            'mailer.Message', priority=PRIORITY_DEFERRED)
        self.recently_added = mixer.cycle(5).blend(
            'mailer.Message', when_added=now(),
            priority=PRIORITY_MEDIUM)

    def test_deferred_emails(self):
        self.assertEqual(
            email_queue()['status'],
            SERVER_STATUS['OK'],
            msg='Without queued emails, the status should be OK.'
        )

        mixer.cycle(1).blend('mailer.Message',
                             when_added=now() - timedelta(minutes=40),
                             priority=PRIORITY_MEDIUM)
        self.assertEqual(
            email_queue()['status'],
            SERVER_STATUS['WARNING'],
            msg='With 1 queued email, the status should be WARNING.'
        )

        mixer.cycle(99).blend('mailer.Message',
                              when_added=now() - timedelta(minutes=40),
                              priority=PRIORITY_MEDIUM)
        self.assertEqual(
            email_queue()['status'],
            SERVER_STATUS['DANGER'],
            msg='With 100 queued emails, the status should be DANGER.'
        )
