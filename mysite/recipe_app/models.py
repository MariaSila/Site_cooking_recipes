from django.contrib.auth.models import User
from django.db import models


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


class Step(models.Model):
    """
    Шаг приготовления
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='steps',
        verbose_name='Рецепт'
    )
    description = models.TextField(verbose_name='Описание шага')
    step_number = models.PositiveIntegerField(verbose_name='Номер шага')

    class Meta:
        ordering = ['step_number']
        verbose_name = 'Шаг приготовления'
        verbose_name_plural = 'Шаги приготовления'

    def __str__(self):
        return f"Шаг {self.step_number}: {self.description[:20]}..."


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
