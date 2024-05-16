import datetime

from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client

from mainapp.models import CompanyInfo
from news_app.models import NewsArticle


class MasterTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_master_orders(self):
        # user = User.objects.create_user("test_user", "mail@mail.com", "mnbv0987")
        # self.client.login(username="test_user", password="mnbv0987")
        article = NewsArticle()
        article.title = "Title"
        article.author = "Nobody"
        article.date = datetime.datetime.today()
        article.save()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

