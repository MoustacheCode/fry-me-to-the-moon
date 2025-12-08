from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe, Comment
from .forms import CommentForm
from django.db.models import Q
from .forms import SignUpForm




@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user:
        messages.warning(request, "You can only delete your own recipes.")
        return redirect('recipe_list') 

    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user:
        messages.warning(request, "You can only edit your own recipes.")
        return redirect('recipe_list') 

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)   # don't save yet
            recipe.owner = request.user        # set the owner
            recipe.save()                      # now save
            return render(
                request,
                "recipes/recipe_form.html",
                {"form": RecipeForm(), "recipe_success": True}
            )
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Render the same template with success flag to show popup
            return render(
                request,
                "registration/signup.html",
                {"form": SignUpForm(), "registered_success": True}
            )
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

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

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['comments'] = recipe.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.author = request.user
                comment.save()
                messages.success(request, "Comment added successfully!")
                return redirect('recipe_detail', pk=recipe.pk)
        else:
            messages.warning(request, "You must be logged in to comment.")
            return redirect('login')
        return self.get(request, *args, **kwargs)

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm   # use your custom form
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

    def get_queryset(self):
        # Only allow editing recipes owned by the current user
        return super().get_queryset().filter(owner=self.request.user)



class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
    def get_queryset(self):
        # Limit deletion to recipes created by the logged-in user
        return super().get_queryset().filter(owner=self.request.user)
    
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    recipe = comment.recipe
    if request.user == comment.author or request.user == recipe.owner:
        comment.delete()
        messages.success(request, "Comment deleted.")
    else:
        messages.warning(request, "You can only delete your own comments.")
    return redirect('recipe_detail', pk=recipe.pk)

