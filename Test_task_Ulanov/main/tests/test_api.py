from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class BooksApiTestCase(APITestCase):
    def test_plus(self):
        url = 'http://127.0.0.1:8000/'
        print(url)
        response = self.client.get(url)
        print(response)
