from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            name='Gin'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            name='Whiskey'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            name='Old Fashioned'
        )

        self.assertEqual(str(recipe), recipe.name)
