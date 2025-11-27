from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe



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
            recipe.owner = request.user
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

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'category', 'image']  # adjust to your model fields
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')  # or wherever you want to redirect after saving


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
    def get_queryset(self):
        # Limit deletion to recipes created by the logged-in user
        return super().get_queryset().filter(created_by=self.request.user)