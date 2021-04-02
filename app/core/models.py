from django.db import models


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient used in a recipe"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
