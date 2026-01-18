from django import forms
from .models import Recipe


class RecipeCreateForm(forms.ModelForm):
    """
    Форма добавления рецепта
    """

    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'description', 'category', 'step', 'cooking_time', 'preview')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
