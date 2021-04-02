from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from recipe.serializers import TagSerializer


TAGS_URL = reverse('recipe:tag-list')


class TagApiTests(TestCase):
    """Test the tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(name='Chicken')
        Tag.objects.create(name='Cocktail')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
