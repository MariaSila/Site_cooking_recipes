from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def recipe_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipe_app/recipe-index.html')
