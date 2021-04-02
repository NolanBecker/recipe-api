from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Quantity

from recipe.serializers import QuantitySerializer


QTY_URL = reverse('recipe:quantity-list')


class QtyApiTests(TestCase):
    """Test the qty API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_qtys(self):
        """Test retrieving qtys"""
        Quantity.objects.create(amount=2.00)
        Quantity.objects.create(amount=0.75)

        res = self.client.get(QTY_URL)

        qtys = Quantity.objects.all()
        serializer = QuantitySerializer(qtys, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
