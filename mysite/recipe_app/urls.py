from django.urls import path
from .views import recipe_index

app_name = "recipe_app"

urlpatterns = [
    path("", recipe_index, name='index'),
]