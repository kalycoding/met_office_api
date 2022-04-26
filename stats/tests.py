from django.test import TestCase
from .models import MaxTemp
from .serializers import MaxTempSerializer
from django.core.management import call_command
from rest_framework import test
from django.urls import reverse
import sys
import json


# Create your tests here.


class TestProduct(TestCase):
    
   
    def test_get_met_endpoint(self):
        client = test.APIClient()
        response = client.get(
            reverse('max-temp')
        )
        self.assertEqual(response.status_code, 200)
