import datetime

from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from mainapp.models import CompanyInfo
from news_app.models import NewsArticle
from service_app.models import ServiceType


class MainTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_news(self):
        article = NewsArticle()
        article.title = "Title"
        article.author = "Nobody"
        article.date = datetime.datetime.today()
        article.cover = ""
        article.save()
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        # user = User.objects.create_user("test_user", "mail@mail.com", "mnbv0987")
        # self.client.login(username="test_user", password="mnbv0987")
        article = NewsArticle()
        article.title = "Title"
        article.author = "Nobody"
        article.date = datetime.datetime.today()
        article.save()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        info = CompanyInfo()
        info.description = "info smth smth"
        info.save()
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    from django.test import TestCase
    from django.test import TestCase
    from django.contrib.auth.models import AnonymousUser, User
    from django.test import RequestFactory, TestCase, Client

    from service_app.models import ServiceType, Service

    class ServiceTest(TestCase):
        def setUp(self):
            # Every test needs access to the request factory.
            self.factory = RequestFactory()
            self.client = Client()

        def test_service_types(self):
            st = ServiceType()
            st.name = "dfqd"
            st.description = "fafadf"
            st.save()
            response = self.client.get('/services/')
            self.assertEqual(response.status_code, 200)

        def test_service_types3(self):
            st = ServiceType()
            st.name = "dfqd"
            st.description = "fafadf"
            st.save()
            response = self.client.get('/services/')
            self.assertEqual(response.status_code, 200)

        def test_service_types4(self):
            st = ServiceType()
            st.name = "dfqd"
            st.description = "fafadf"
            st.save()
            response = self.client.get('/services/')
            self.assertEqual(response.status_code, 200)



