from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient, Quantity, Unit, Item

from recipe.serializers import IngredientSerializer


INGREDIENTS_URL = reverse('recipe:ingredient-list')


class IngredientApiTests(TestCase):
    """Test ingredient API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_ingredients(self):
        """Test retrieving ingredients"""
        Ingredient.objects.create(
            quantity=Quantity.objects.create(amount=2.00),
            unit=Unit.objects.create(name='oz'),
            item=Item.objects.create(name='Whiskey')
        )
        Ingredient.objects.create(
            quantity=Quantity.objects.create(amount=1.25),
            unit=Unit.objects.create(name='cup'),
            item=Item.objects.create(name='Sugar')
        )

        res = self.client.get(INGREDIENTS_URL)

        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_ingredients(self):
        """Test creating ingredients"""
        qty1 = Quantity.objects.create(amount=1.00)
        unit1 = Unit.objects.create(name='oz')
        item1 = Item.objects.create(name='Whiskey')
        payload = {
            'quantity': qty1.id,
            'unit': unit1.id,
            'item': item1.id
        }
        res = self.client.post(INGREDIENTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        ingredient = Ingredient.objects.get(id=res.data['id'])
        qty2 = ingredient.quantity
        unit2 = ingredient.unit
        item2 = ingredient.item
        self.assertEqual(qty1, qty2)
        self.assertEqual(unit1, unit2)
        self.assertEqual(item1, item2)
