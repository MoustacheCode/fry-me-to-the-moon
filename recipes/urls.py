from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.recipe_list, name="recipe_list"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("recipe/new/", views.recipe_create, name="recipe_create"),
    path("recipe/<int:pk>/edit/", views.recipe_edit, name="recipe_edit"),  # FBV
    path("recipe/<int:pk>/delete/", views.recipe_delete, name="recipe_delete"),  # FBV
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
]
