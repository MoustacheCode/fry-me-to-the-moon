from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'created_at')
    search_fields = ('title', 'ingredients', 'description')
    list_filter = ('category', 'created_at')
