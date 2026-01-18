from django.urls import path
from .views import random_recipies_view, RecipeCreateView, RecipeDetailView

app_name = "recipe_app"

urlpatterns = [
    path("", random_recipies_view, name='recipies_list'),
    path("create/", RecipeCreateView.as_view(), name='recipe_create'),
    path("<int:pk>/", RecipeDetailView.as_view(), name='recipe_details'),
]