from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from service_app.models import ServiceType, Service


class vacancyTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_vacancy(self):
        st = ServiceType()
        st.name = "dfqd"
        st.description = "fafadf"
        st.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_vacancy2(self):
        st = ServiceType()
        st.name = "dfqd"
        st.description = "fafadf"
        st.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_vacancy3(self):
        st = ServiceType()
        st.name = "dfqd"
        st.description = "fafadf"
        st.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_vacancy4(self):
        st = ServiceType()
        st.name = "dfqd"
        st.description = "fafadf"
        st.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

