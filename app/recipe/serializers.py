from rest_framework import serializers

from core.models import Tag, Recipe, Unit, Quantity, Item


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


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Item.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'items', 'tags', 'directions', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serialize a recipe detail"""
    items = ItemSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'items', 'tags', 'directions', 'link')
        read_only_fields = ('id',)
