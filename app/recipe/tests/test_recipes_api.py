from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient, Quantity, Unit, Item

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_tag(name='Vodka'):
    """Create and return a sample tag"""
    return Tag.objects.create(name=name)


def sample_unit(name='oz'):
    """Create and return a sample unit"""
    return Unit.objects.create(name=name)


def sample_quantity(amount='1.00'):
    """Create and return a sample quantity"""
    return Quantity.objects.create(amount=amount)


def sample_item(name='Lime Juice'):
    """Create and return a sample item"""
    return Item.objects.create(name=name)


def sample_ingredient(
    quantity=sample_quantity(),
    unit=sample_unit(),
    item=sample_item()
):
    """Create and return a sample ingredient"""
    return Ingredient.objects.create(quantity=quantity, unit=unit, item=item)


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
        recipe.ingredients.add(Ingredient.objects.create(
            quantity=Quantity.objects.create(amount=0.5),
            unit=Unit.objects.create(name='tsp'),
            item=Item.objects.create(name='Sugar')
        ))

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
        ingredient1 = Ingredient.objects.create(
            quantity=Quantity.objects.create(amount=2.00),
            unit=Unit.objects.create(name='oz'),
            item=Item.objects.create(name='Whiskey')
        )
        ingredient2 = Ingredient.objects.create(
            quantity=Quantity.objects.create(amount=3.00),
            unit=Unit.objects.create(name='dash'),
            item=Item.objects.create(name='Bitters')
        )
        payload = {
            'name': 'Painkiller',
            'ingredients': [ingredient1.id, ingredient2.id]
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)
