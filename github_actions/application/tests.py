from rest_framework.test import APITestCase
from rest_framework.views import status

from django.shortcuts import resolve_url
from django.urls import reverse

class PhoneVerificationTestCase(APITestCase):
    def setUp(self):
        self.url_1 = '/question/'
        self.data = {
            "id": 1,
            "title": "테스트",
            # "name": "송지민",
            "content": "입니다",
            "created_at": "2023-07-16T17:15:03.288341Z",
            "updated_at": "2023-07-16T17:15:03.288501Z"
        }

    def test_post_phone_number_success(self):
        response = self.client.post(self.url_1, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
