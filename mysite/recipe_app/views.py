from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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


class RecipeCreateView(LoginRequiredMixin, CreateView):
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


class RecipeUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name_suffix = '_update_form'
    success_message = 'Рецепт был успешно обновлен!'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        return reverse('recipe_app:recipe_details', kwargs={'pk': self.object.pk},)


class RecipeDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe_app:recipies_list")
    success_message = 'Рецепт был успешно удалён!'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        success_url = self.get_success_url()
        # self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
