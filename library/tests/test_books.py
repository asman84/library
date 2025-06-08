from django.urls import reverse
from rest_framework import status

from accounts.tests import USER_TOKEN
from toolkit.tests import BaseTestCase


class BookTest(BaseTestCase):
    auth_token = USER_TOKEN
    fixtures = (
        'book.yaml',
        'author.yaml',
    )


    def test_list(self):
        response = self.client.get(reverse('library:book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
