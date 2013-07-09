import datetime

from django.utils import timezone
from django.test import TestCase

from apps.polls.models import Poll


class PollMethodTests(TestCase):

    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently_with_future_poll() should return False for for polls whose
        pub_date is is the future
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)