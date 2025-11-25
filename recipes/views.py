from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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
