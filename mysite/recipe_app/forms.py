from django import forms
from .models import Recipe
from django.forms import inlineformset_factory, modelformset_factory


class RecipeCreateForm(forms.ModelForm):
    """
    Форма добавления рецепта
    """

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'step', 'cooking_time', 'preview')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'step': forms.TextInput(attrs={'class': 'form-control'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }