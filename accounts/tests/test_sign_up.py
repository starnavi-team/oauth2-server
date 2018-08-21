from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTestCase(TestCase):
    SIGN_UP_URL = '/signup/'

    def setUp(self):
        get_user_model().objects.create_user(
            username='tom',
            password='tom_secret',
        )

    def test_sign_up_success(self):
        response = self.client.post(
            self.SIGN_UP_URL,
            {
                'username': 'bob',
                'password1': 'bob_secret',
                'password2': 'bob_secret',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertTrue(get_user_model().objects.filter(username='bob').exists())

    def test_sign_up_exist_username(self):
        response = self.client.post(
            self.SIGN_UP_URL,
            {
                'username': 'tom',
                'password1': 'tom_secret',
                'password2': 'tom_secret',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'A user with that username already exists.',
            response.context['form'].errors['username'],
        )

    def test_sign_up_password_mismatch(self):
        response = self.client.post(
            self.SIGN_UP_URL,
            {
                'username': 'bob',
                'password1': 'tom_secret',
                'password2': 'bob_secret',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'The two password fields didn\'t match.',
            response.context['form'].errors['password2'],
        )
