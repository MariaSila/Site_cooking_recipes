from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Recipe, Category
from .forms import RecipeCreateForm


class RecipiesListView(ListView):
    model = Recipe
    template_name = 'recipe_app/recipies-list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Recipe.objects.order_by('?')


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


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('recipe_app:recipe_details', kwargs={'pk': self.object.pk},)