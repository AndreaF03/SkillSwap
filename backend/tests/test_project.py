from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import User


class ProjectSmokeTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="Password123"
        )

    def test_user_model(self):
        self.assertEqual(self.user.username, "testuser")

    def test_register_url_exists(self):
        response = self.client.post(
            "/api/accounts/register/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password": "Password123"
            },
            format="json"
        )

        self.assertIn(response.status_code, [200, 201])

    def test_login_url_exists(self):
        response = self.client.post(
            "/api/accounts/login/",
            {
                "username": "testuser",
                "password": "Password123"
            },
            format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_profile_requires_auth(self):
        response = self.client.get(
            "/api/accounts/profile/"
        )

        self.assertIn(response.status_code, [401, 403])

    def test_admin_page_exists(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)