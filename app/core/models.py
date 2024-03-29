from django.db import models


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    """Item used in an ingredient"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    """Unit used in a recipe"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    """Qty used in a recipe"""

    class Meta:
        verbose_name_plural = 'Quantities'

    amount = models.DecimalField(max_digits=5, decimal_places=2, unique=True)

    def __str__(self):
        return str(self.amount)


class Recipe(models.Model):
    """Recipe"""
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    directions = models.TextField(blank=True)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient for use in a recipe"""
    quantity = models.ForeignKey('Quantity', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.quantity.amount) + " " + self.unit.name
                + " " + self.item.name)
