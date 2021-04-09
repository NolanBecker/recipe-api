from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('items', views.ItemViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('units', views.UnitViewSet)
router.register('qtys', views.QuantityViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
