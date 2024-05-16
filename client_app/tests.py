from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client


class ClientTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_order_list(self):
        user = User.objects.create_user("test_user", "mail@mail.com", "mnbv0987")
        self.client.login(username="test_user", password="mnbv0987")

        response = self.client.get('/client/')
        self.assertEqual(response.status_code, 200)

    def test_cancel_order(self):
        user = User.objects.create_user("test_user", "mail@mail.com", "mnbv0987")
        self.client.login(username="test_user", password="mnbv0987")

        response = self.client.post('/client/cancel', data={
            'order_id': 0
        })
        self.assertEqual(response.status_code, 301)

