from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import CustomUser, Category, Data
from .serializers import CustomUserSerializer, CategorySerializer, DataSerializer


class CustomUserTest(APITestCase):
    def users(self):
        url = reverse('get_users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





   
                         











