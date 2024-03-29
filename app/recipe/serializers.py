from rest_framework import serializers

from core.models import Tag, Recipe, Unit, Quantity, Item, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for item objects"""

    class Meta:
        model = Item
        fields = ('id', 'name')
        read_only_fields = ('id',)


class UnitSerializer(serializers.ModelSerializer):
    """Serializer for unit objects"""

    class Meta:
        model = Unit
        fields = ('id', 'name')
        read_only_fields = ('id',)


class QuantitySerializer(serializers.ModelSerializer):
    """Serializer for qty objects"""

    class Meta:
        model = Quantity
        fields = ('id', 'amount')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serialize an ingredient"""
    quantity = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Quantity.objects.all()
    )
    unit = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Unit.objects.all()
    )
    item = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Item.objects.all()
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'quantity', 'unit', 'item')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'tags', 'directions', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'tags', 'directions', 'link')
        read_only_fields = ('id',)
