from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from mysite.settings import COUNT_RND
from .models import Recipe, Category
from .forms import RecipeCreateForm


class RecipeListView(ListView):
    template_name = 'recipe_app/recipies-list.html'
    model = Recipe
    context_object_name = 'recipies'
    paginate_by = COUNT_RND


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

