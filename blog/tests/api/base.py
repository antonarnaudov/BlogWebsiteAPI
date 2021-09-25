from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class BaseApiTests(TestCase):
    password = 'mypassword'
    user = {}

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser('testuser', 'test@test.com', cls.password)
        cls.user.save()

    def setUp(self):
        self.client = APIClient()
        self.client.login(username=self.user.username, password=self.password)

        token_url = reverse('token_obtain_pair')
        login_data = {
            "username": self.user.username,
            "password": self.password
        }

        token = self.client.post(token_url, login_data, format='json')
        self.client.credentials(Authorization="Blog " + token.data["token"])

