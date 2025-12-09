from django.test import SimpleTestCase
from django.urls import reverse, resolve
from recipes import views
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):
    def test_recipe_list_url_resolves(self):
        url = reverse("recipe_list")
        self.assertEqual(resolve(url).func, views.recipe_list)

    def test_recipe_detail_url_resolves(self):
        url = reverse("recipe_detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, views.RecipeDetailView)

    def test_recipe_create_url_resolves(self):
        url = reverse("recipe_create")
        self.assertEqual(resolve(url).func, views.recipe_create)

    def test_recipe_edit_url_resolves(self):
        url = reverse("recipe_edit", args=[1])
        self.assertEqual(resolve(url).func, views.recipe_edit)

    def test_recipe_delete_url_resolves(self):
        url = reverse("recipe_delete", args=[1])
        self.assertEqual(resolve(url).func, views.recipe_delete)

    def test_signup_url_resolves(self):
        url = reverse("signup")
        self.assertEqual(resolve(url).func, views.signup)

    def test_comment_delete_url_resolves(self):
        url = reverse("comment_delete", args=[1])
        self.assertEqual(resolve(url).func, views.comment_delete)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)
