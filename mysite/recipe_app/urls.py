from django.urls import path
from .views import RecipeListView, RecipeCreateView

app_name = "recipe_app"

urlpatterns = [
    path("", RecipeListView.as_view(), name='recipies_list'),
    path("recipies/create/", RecipeCreateView.as_view(), name='recipe_create'),
]