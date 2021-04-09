from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            name='Gin'
        )

        self.assertEqual(str(tag), tag.name)

    def test_item_str(self):
        """Test the item string representation"""
        item = models.Item.objects.create(
            name='Whiskey'
        )

        self.assertEqual(str(item), item.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            name='Old Fashioned'
        )

        self.assertEqual(str(recipe), recipe.name)

    def test_unit_str(self):
        """Test the unit string representation"""
        unit = models.Unit.objects.create(
            name='oz'
        )

        self.assertEqual(str(unit), unit.name)

    def test_qty_str(self):
        """Test the quantity string representation"""
        qty = models.Quantity.objects.create(
            amount=1.00
        )

        self.assertEqual(str(qty), str(qty.amount))

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            quantity=models.Quantity.objects.create(amount=1.00),
            unit=models.Unit.objects.create(name='oz'),
            item=models.Item.objects.create(name='Whiskey')
        )

        ingredientStr = (str(ingredient.quantity.amount) + " "
                         + ingredient.unit.name + " "
                         + ingredient.item.name)
        self.assertEqual(str(ingredient), ingredientStr)
