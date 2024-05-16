import requests
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from auth_app import views


class AuthTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_details(self):
        response = self.client.get('/auth/')
        self.assertEqual(response.status_code, 200)
