from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Soup",
            description="Warm and cozy",
            ingredients="Water\nCarrots\nSalt",
            steps="Boil water\nAdd carrots\nSeason",
            category="mains",
            cook_time_minutes=30,
            owner=self.user
        )
        # Basic field checks
        self.assertEqual(recipe.title, "Soup")
        self.assertEqual(recipe.category, "mains")
        self.assertEqual(recipe.owner.username, "testuser")

    def test_str_method_returns_title(self):
        recipe = Recipe.objects.create(
            title="Cake",
            description="Sweet dessert",
            ingredients="Flour\nSugar\nEggs",
            steps="Mix\nBake",
            category="desserts",
            owner=self.user
        )
        self.assertEqual(str(recipe), "Cake")

    def test_ordering_by_created_at(self):
        r1 = Recipe.objects.create(
            title="First",
            ingredients="A",
            steps="Step",
            category="snacks",
            owner=self.user
        )
        r2 = Recipe.objects.create(
            title="Second",
            ingredients="B",
            steps="Step",
            category="drinks",
            owner=self.user
        )
        recipes = Recipe.objects.all()
        # Because of Meta ordering = ['-created_at'], newest first
        self.assertEqual(recipes[0], r2)
        self.assertEqual(recipes[1], r1)

    def test_blank_description_allowed(self):
        recipe = Recipe.objects.create(
            title="No Description",
            ingredients="Ingredient",
            steps="Step",
            category="vegan",
            owner=self.user
        )
        self.assertEqual(recipe.description, "")
