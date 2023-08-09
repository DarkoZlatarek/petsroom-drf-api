from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='rob', password='pass')

    def test_can_list_profiles(self):
        rob = User.objects.get(username='rob')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
