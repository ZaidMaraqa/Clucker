from django.test import TestCase
from microblogs.forms import LogInForm
from django.urls import reverse
from django.contrib import messages
from .helpers import LogInTester
from microblogs.models import User

class LogInViewTestCase(TestCase, LogInTester):

    def setUp(self):
        self.url = reverse('log_in')
        self.user = User.objects.create_user('@johndoe',
        first_name = 'John',
        last_name = 'Doe',
        email = 'johndoe@example.org',
        bio = 'Hello, I am John Doe.',
        password = 'Password123',
        is_active = True,
        )

    def test_log_in_url(self):
        self.assertEqual(self.url, '/log_in/')
