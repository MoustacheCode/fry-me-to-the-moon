from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe

class TestRecipeIntegration(TestCase):
    def test_full_user_flow(self):
        # 1. Sign up a new user
        signup_response = self.client.post(reverse("signup"), {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
        })
        self.assertEqual(signup_response.status_code, 200)
        self.assertTrue(User.objects.filter(username="newuser").exists())

        # 2. Log in
        login_success = self.client.login(username="newuser", password="strongpassword123")
        self.assertTrue(login_success)

        # 3. Create a recipe
        create_response = self.client.post(reverse("recipe_create"), {
            "title": "Cake",
            "description": "Sweet dessert",
            "ingredients": "Flour\nSugar\nEggs",
            "steps": "Mix\nBake",
            "category": "desserts",
            "cook_time_minutes": 45,
        })
        self.assertEqual(create_response.status_code, 200)
        recipe = Recipe.objects.get(title="Cake")
        self.assertEqual(recipe.owner.username, "newuser")

        # 4. Edit the recipe
        edit_response = self.client.post(reverse("recipe_edit", args=[recipe.pk]), {
            "title": "Chocolate Cake",
            "description": "Rich and sweet",
            "ingredients": "Flour\nSugar\nEggs\nCocoa",
            "steps": "Mix\nBake\nFrost",
            "category": "desserts",
            "cook_time_minutes": 50,
        })
        self.assertEqual(edit_response.status_code, 302)  # redirect to detail
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, "Chocolate Cake")

        # 5. Delete the recipe
        delete_response = self.client.post(reverse("recipe_delete", args=[recipe.pk]))
        self.assertRedirects(delete_response, reverse("recipe_list"))
        self.assertFalse(Recipe.objects.filter(pk=recipe.pk).exists())
