import pytz
import datetime
from django.test import TestCase
from schedule.models import Calendar, Rule, Event


class TestEvent(TestCase):
    def setUp(self):
        self.cal = Calendar(name="cal", slug="cal")
        self.cal.save()
        self.rule = Rule(frequency="DAILY", name="Daily", description="will recur once every Day")
        self.rule.save()

    def test_create_event(self):
        event_one = Event.objects.create(
            title="Event one",
            start=datetime.datetime(2019, 1, 5, 8, 0, tzinfo=pytz.utc),
            end=datetime.datetime(2019, 1, 5, 9, 0, tzinfo=pytz.utc),
            calendar=self.cal,
        )
        self.assertEqual(event_one.title, "Event one")

