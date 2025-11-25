from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Recipe

def recipe_list(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    recipes = Recipe.objects.all()
    if category:
        recipes = recipes.filter(category=category)
    if query:
        recipes = recipes.filter(
            models.Q(title__icontains=query) |
            models.Q(ingredients__icontains=query) |
            models.Q(description__icontains=query)
        )

    categories = dict(Recipe.CATEGORY_CHOICES)
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'query': query,
        'category': category,
        'categories': categories,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
