from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Item

from recipe.serializers import ItemSerializer


ITEMS_URL = reverse('recipe:item-list')


class ItemApiTests(TestCase):
    """Test the items API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_items(self):
        """Test retrieving items"""
        Item.objects.create(name='Whiskey')
        Item.objects.create(name='Simple Syrup')

        res = self.client.get(ITEMS_URL)

        items = Item.objects.all().order_by('name')
        serializer = ItemSerializer(items, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_item_successful(self):
        """Test creating a new item"""
        payload = {'name': 'Bitters'}
        self.client.post(ITEMS_URL, payload)

        exists = Item.objects.filter(
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_item_invalid(self):
        """Test creating an invalid item"""
        payload = {'name': ''}
        res = self.client.post(ITEMS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
