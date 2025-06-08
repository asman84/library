from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from toolkit.tests import BaseTestCase

USER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5MjI4MDIxLCJpYXQiOjE3NDkyMTcyMjEsImp0aSI6Ijk5ODUwNGNkNGI2NzRmMzhhNmY3YjY0MjQ2ZjI3OTQ5IiwidXNlcl9pZCI6MX0.kBK5IjIS7d5-yu-ZKskGh2pZGyqICuxLWtOT0D0liw4'


class UserTest(BaseTestCase):
    auth_token = USER_TOKEN
    fixtures = ('user.yaml',)


class UserCreateTest(APITestCase):
    def test_user_creation(self):
        url = reverse('user-register')
        data = {
            'username': 'testuser',
            'password': 'Test1234!',
            'email': 'test@example.com'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.first().username, 'testuser')

        self.assertNotEqual(get_user_model().objects.first().password, 'Test1234!')
        self.assertTrue(get_user_model().objects.first().check_password('Test1234!'))
        self.assertNotIn('password', response.data)


class UserLoginTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='Test1234!'
        )
        self.url = reverse('token_obtain_pair')

    def test_successful_login(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'Test1234!'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_login(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'WrongPassword!'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        