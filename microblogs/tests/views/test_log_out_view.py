from django.test import TestCase
from microblogs.forms import LogInForm
from django.urls import reverse
from django.contrib import messages
from microblogs.tests.helpers import LogInTester
from microblogs.models import User

class LogInViewTestCase(TestCase, LogInTester):

    fixtures = ['microblogs/tests/fixtures/default_user.json']

    def setUp(self):
        self.url = reverse('log_in')
        self.user = User.objects.get(username = '@johndoe')

    def test_log_in_url(self):
        self.assertEqual(self.url, '/log_in/')
