from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from recipe_app.models import Recipe


def recipe_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipe_app/recipe-index.html')


class RecipeListView(ListView):
    template_name = "recipe_app/recipies-list.html"
    model = Recipe
    context_object_name = "recipies_list"


class RecipeCreateView(CreateView):
    template_name = "recipe_app/recipe-form.html"
    model = Recipe
    #fields = 'title', 'description', 'cooking_time'
    fields = '__all__'
    #success_url = reverse_lazy("recipe_app: recipies_list")
