from django.test import TestCase

from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    def setUp(self):
        if hasattr(self, 'auth_token'):
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.auth_token)

