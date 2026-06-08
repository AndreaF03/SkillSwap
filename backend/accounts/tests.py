from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import User


class AccountTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_register(self):

        response = self.client.post(
            "/api/accounts/register/",
            {
                "username": "testuser",
                "email": "test@test.com",
                "password": "Password123"
            },
            format="json"
        )

        self.assertIn(response.status_code, [200, 201])

    def test_login(self):

        User.objects.create_user(
            username="testuser",
            password="Password123"
        )

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