from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def sample_recipe(**params):
    """Create and return a sample recipe"""
    defaults = {
        'name': 'Sample Recipe',
        'directions': 'This is how you make it'
    }
    defaults.update(params)

    return Recipe.objects.create(**params)


class RecipeApiTests(TestCase):
    """Test recipe API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_recipes(self):
        """Test retrieving recipes"""
        sample_recipe()
        sample_recipe(name='Old Fashioned')

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
