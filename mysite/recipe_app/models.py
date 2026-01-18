from random import randint

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max, Min
from django.shortcuts import render

from mysite.settings import COUNT_RND


# class RandomManager(models.Manager):
#     def truly_random(self):
#         max_id = self.aggregate(max_id=Max("id"))['max_id']
#         if max_id:
#             min_id = self.aggregate(min_id=Min("id"))['min_id']
#             random_id = randint(min_id, max_id)
#             return self.filter(id__gte=random_id).first()
#
#
# class CountRandomManager(RandomManager):
#     def get_queryset(self):
#         return super().get_queryset().order_by('?').first()


def recipe_preview_directory_path(instance: "Recipe", filename: str) -> str:
    return f"recipes/recipe_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Recipe(models.Model):
    """
    Рецепт
    """
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(null=False, blank=True, verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления в минутах")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_recipe', verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    preview = models.ImageField(
        null=True,
        blank=True,
        upload_to=recipe_preview_directory_path,
        verbose_name='Изображение рецепта'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        related_name='recipes'
    )
    step = models.TextField(null=False, blank=True, verbose_name='Шаги приготовления')

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    # objects = models.Manager()
    # custom = CountRandomManager


class Category(models.Model):
    """
    Категория рецепта
    """
    name = models.CharField(
        max_length=50,
        help_text="Укажите категорию (например, завтрак, обед, на праздник, и т.д.)",
        verbose_name='Название категории'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
