from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from mysite.settings import COUNT_RND
from .models import Recipe, Category
from .forms import RecipeCreateForm


def random_recipies_view(request):
    # COUNT_RND количество случайных записей (установлен в mysite/settings.py)
    random_recipies = Recipe.objects.order_by('?')[:COUNT_RND]
    context = {
        'posts': random_recipies
    }
    return render(request, 'recipe_app/recipies-list.html', context)


class RecipeDetailView(DetailView):
    template_name = 'recipe_app/recipe-details.html'
    queryset = (
        Recipe.objects
        .select_related('author')
        .prefetch_related('category')
    )
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    template_name = 'recipe_app/recipe-form.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy("recipe_app:recipies_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи на сайт'
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response

