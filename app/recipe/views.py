from rest_framework import viewsets, mixins

from core.models import Tag, Ingredient, Recipe, Unit, Quantity
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


class UnitViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Manage units in the database"""
    queryset = Unit.objects.all().order_by('name')
    serializer_class = serializers.UnitSerializer


class QuantityViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """Manage qtys in the database"""
    queryset = Quantity.objects.all()
    serializer_class = serializers.QuantitySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class
