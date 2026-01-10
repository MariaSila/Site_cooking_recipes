from django.contrib.auth.models import User
from django.db import models


def recipe_preview_directory_path(instance: "Recipe", filename: str) -> str:
    return f"recipes/recipe_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Recipe(models.Model):
    """
    Модель Рецепты
    """
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(null=False, blank=True, verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления в минутах")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    preview = models.ImageField(
        null=True,
        blank=True,
        upload_to=recipe_preview_directory_path,
        verbose_name='Изображение рецепта'
    )

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title
