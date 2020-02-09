from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@isk.com',
            password='password123'
        )
        self.Client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@isk.com',
            password='password123',
            name='user 1'
        )

    def test_users_listed(self):
        """Test users listed"""
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_users_change_page(self):
        """Test edit page"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.Client.get(url)

        self.assertEqual(res.status_code, 200)
