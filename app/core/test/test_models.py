from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating email user authentication"""

        email = 'test@gmail.com'
        password = 'test@1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'try@ISK.COM'
        user = get_user_model().objects.create_user(email, 'password123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_new_superuser(self):
        """Test for creating new supper user"""
        user = get_user_model().objects.create_superuser(
            'try@gmail.com',
            'password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
