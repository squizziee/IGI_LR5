from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client


class CartTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_page_load(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        response = self.client.post('/cart/add/', data={
            'service_type_id': 1,
            'service_id': 1,
            'device_type_id': 1,
            'device_id': 1,
            'master_id': 1,
        })
        self.assertEqual(response.status_code, 302)

    def test_cart_remove(self):
        s = self.client.session
        s.update({
            'cart': {
                'items': [
                    {
                        'service_type_id': 1,
                        'service_id': 1,
                        'device_type_id': 1,
                        'device_id': 1,
                        'master_id': 1,
                    }
                ]
            }
        })

        s.save()
        response = self.client.post('/cart/remove/', data={
            'entry_index': 0
        })
        self.assertEqual(response.status_code, 302)

    def test_cart_checkout(self):
        response = self.client.post('/cart/checkout/', data={
            'items': [
                {
                    'service_type_id': 1,
                    'service_id': 1,
                    'device_type_id': 1,
                    'device_id': 1,
                    'master_id': 1,
                 }
            ]
        })
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        s = self.client.session
        s.update({
            'cart': {
                'items': [
                    {
                        'service_type_id': 1,
                        'service_id': 1,
                        'device_type_id': 1,
                        'device_id': 1,
                        'master_id': 1,
                    }
                ]
            }
        })

        s.save()

        self.client.post('/cart/create_order/', data={
            'email': "mail@mail.com",
            'password': "mnbv0987",
            'name': "test_client",
            'address': "some address",
            'phone_number': "4545451",
            'passport_serial': "test_serial",
        })
        response = self.client.post('/cart/remove/', data={
            'entry_index': 0
        })
        self.assertEqual(response.status_code, 302)

