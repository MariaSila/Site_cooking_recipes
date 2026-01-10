from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description", "cooking_time"
    list_display_links = "pk", "title"
