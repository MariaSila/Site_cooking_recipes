from django.urls import path
from .views import recipe_index, RecipeListView, RecipeCreateView

app_name = "recipe_app"

urlpatterns = [
    path("", recipe_index, name='index'),
    path("recipies/", RecipeListView.as_view(), name='recipies_list'),
    path("recipies/create/", RecipeCreateView.as_view(), name='recipe_create'),
]