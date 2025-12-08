from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe

class RecipeViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

        # Create a recipe owned by testuser
        self.recipe = Recipe.objects.create(
            title="Soup",
            description="Warm and cozy",
            ingredients="Water\nCarrots\nSalt",
            steps="Boil water\nAdd carrots\nSeason",
            category="mains",
            owner=self.user
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse("recipe_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Soup")

    def test_recipe_detail_view(self):
        response = self.client.get(reverse("recipe_detail", args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Warm and cozy")

    def test_recipe_create_view_post(self):
        response = self.client.post(reverse("recipe_create"), {
            "title": "Cake",
            "description": "Sweet dessert",
            "ingredients": "Flour\nSugar\nEggs",
            "steps": "Mix\nBake",
            "category": "desserts",
        })
        self.assertEqual(response.status_code, 200)  # renders recipe_form again
        self.assertTrue(Recipe.objects.filter(title="Cake").exists())

    def test_recipe_edit_view(self):
        response = self.client.post(reverse("recipe_edit", args=[self.recipe.pk]), {
            "title": "Soup Updated",
            "description": "Even warmer",
            "ingredients": "Water\nCarrots\nSalt\nPepper",
            "steps": "Boil water\nAdd carrots\nSeason\nAdd pepper",
            "category": "mains",
        })
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, "Soup Updated")

    def test_recipe_delete_view_post(self):
        response = self.client.post(reverse("recipe_delete", args=[self.recipe.pk]))
        self.assertRedirects(response, reverse("recipe_list"))
        self.assertFalse(Recipe.objects.filter(pk=self.recipe.pk).exists())

    def test_recipe_delete_view_get(self):
        response = self.client.get(reverse("recipe_delete", args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete:")