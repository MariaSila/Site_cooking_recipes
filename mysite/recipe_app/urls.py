from django.urls import path
from .views import RecipiesListView, RecipeCreateView, RecipeDetailView, RecipeUpdateView

app_name = "recipe_app"

urlpatterns = [
    path("", RecipiesListView.as_view(), name='recipies_list'),
    path("create/", RecipeCreateView.as_view(), name='recipe_create'),
    path("<int:pk>/", RecipeDetailView.as_view(), name='recipe_details'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
]