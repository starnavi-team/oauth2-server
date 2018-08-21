from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTestCase(TestCase):
    USER_UPDATE_URL = '/user-update/'

    def setUp(self):
        get_user_model().objects.create_user(
            username='bob',
            password='bob_secret',
        )

    def test_update_user_by_anonymous(self):
        response = self.client.get(self.USER_UPDATE_URL)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/user-update/')

    def test_update_user_success(self):
        self.assertTrue(self.client.login(username='bob', password='bob_secret'))
        response = self.client.post(
            self.USER_UPDATE_URL,
            {
                'username': 'tom',
                'email': 'tom@test.com',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertFalse(get_user_model().objects.filter(username='bob').exists())
        self.assertTrue(get_user_model().objects.filter(username='tom').exists())
        self.assertEqual(get_user_model().objects.get(username='tom').email, 'tom@test.com')
