from rest_framework import viewsets, mixins

from core.models import Tag, Ingredient
from recipe import serializers


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""
    queryset = Tag.objects.all().order_by('name')
    serializer_class = serializers.TagSerializer


class IngredientViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = serializers.IngredientSerializer
