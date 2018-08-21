from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status


class UserTestCase(TestCase):
    USER_INFO_URL = '/api/user-info/'

    def setUp(self):
        get_user_model().objects.create_user(
            username='bob',
            password='bob_secret',
        )

    def test_user_info_by_anonymous(self):
        response = self.client.get(self.USER_INFO_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_info_success(self):
        self.assertTrue(self.client.login(username='bob', password='bob_secret'))
        response = self.client.get(self.USER_INFO_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('username'), 'bob')
