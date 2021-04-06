from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Item

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_tag(name='Vodka'):
    """Create and return a sample tag"""
    return Tag.objects.create(name=name)


def sample_item(name='Lime Juice'):
    """Create and return a sample ingredient"""
    return Item.objects.create(name=name)


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
        recipe.items.add(sample_item())

        url = detail_url(recipe.id)
        res = self.client.get(url)
        serializer = RecipeDetailSerializer(recipe)

        self.assertEqual(res.data, serializer.data)

    def test_create_basic_recipe(self):
        """Test creating recipe"""
        payload = {
            'name': 'Old Fashioned',
            'directions': 'Combine all ingredients in a rocks glass and stir.'
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_create_recipe_with_tags(self):
        """Test creating a recipe with tags"""
        tag1 = sample_tag(name='Tiki')
        tag2 = sample_tag(name='Rum')
        payload = {
            'name': 'Painkiller',
            'tags': [tag1.id, tag2.id]
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        tags = recipe.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)

    def test_create_recipe_with_ingredients(self):
        """Test creating a recipe with ingredients"""
        item1 = sample_item(name='Rum')
        item2 = sample_item(name='Orange Juice')
        payload = {
            'name': 'Painkiller',
            'items': [item1.id, item2.id]
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        items = recipe.items.all()
        self.assertEqual(items.count(), 2)
        self.assertIn(item1, items)
        self.assertIn(item2, items)
