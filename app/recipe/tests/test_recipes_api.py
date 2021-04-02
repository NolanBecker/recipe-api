from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_tag(name='Vodka'):
    """Create and return a sample tag"""
    return Tag.objects.create(name=name)


def sample_ingredient(name='Lime Juice'):
    """Create and return a sample ingredient"""
    return Ingredient.objects.create(name=name)


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

    def test_view_recipe_detail(self):
        """Test viewing a recipe detail"""
        recipe = sample_recipe()
        recipe.tags.add(sample_tag())
        recipe.ingredients.add(sample_ingredient())

        url = detail_url(recipe.id)
        res = self.client.get(url)
        serializer = RecipeDetailSerializer(recipe)

        self.assertEqual(res.data, serializer.data)
