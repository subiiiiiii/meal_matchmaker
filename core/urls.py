from django.urls import path
from .views import home, generate_recipe, recipe_detail, recommended_recipe, get_random_recipe

urlpatterns = [
    path('', home, name='home'),
    path('recipe/list/', generate_recipe, name='recipe_list'),
    path('random/recipe/', get_random_recipe, name='get_random_recipe'),
    path('recipe/recommended/', recommended_recipe, name='recommended_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe-detail'),
]