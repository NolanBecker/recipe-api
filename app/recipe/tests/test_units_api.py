from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Unit

from recipe.serializers import UnitSerializer


UNITS_URL = reverse('recipe:unit-list')


class UnitApiTests(TestCase):
    """Test the units API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_units(self):
        """Test retrieving unit"""
        Unit.objects.create(name='oz')
        Unit.objects.create(name='dash')

        res = self.client.get(UNITS_URL)

        units = Unit.objects.all().order_by('name')
        serializer = UnitSerializer(units, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_unit_successful(self):
        """Test creating a unit"""
        payload = {'name': 'Test unit'}
        self.client.post(UNITS_URL, payload)

        exists = Unit.objects.filter(
            name=payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_unit_invalid(self):
        """Test creating an invalid unit"""
        payload = {'name': ''}
        res = self.client.post(UNITS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
