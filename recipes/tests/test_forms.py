from django.test import TestCase
from recipes.forms import RecipeForm

class RecipeFormTests(TestCase):
    def test_valid_form(self):
        form = RecipeForm(data={
            "title": "Soup",
            "description": "Warm and cozy",
            "ingredients": "Water\nCarrots\nSalt",
            "steps": "Boil water\nAdd carrots\nSeason",
            "category": "mains",
            "cook_time_minutes": 30,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_ingredients(self):
        form = RecipeForm(data={
            "title": "Soup",
            "description": "Warm and cozy",
            "ingredients": "",  # ❌ empty
            "steps": "Boil water\nAdd carrots\nSeason",
            "category": "mains",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("ingredients", form.errors)
        self.assertEqual(form.errors["ingredients"][0], "Please enter at least one ingredient.")

    def test_invalid_form_missing_steps_empty(self):
        form = RecipeForm(data={
            "title": "Soup",
            "description": "Warm and cozy",
            "ingredients": "Water\nCarrots\nSalt",
            "steps": "",  # empty
            "category": "mains",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("steps", form.errors)
        self.assertEqual(form.errors["steps"][0], "Please enter at least one step.")

    def test_invalid_form_missing_steps_whitespace(self):
        """Whitespace-only steps triggers custom validation error."""
        form = RecipeForm(data={
            "title": "Soup",
            "description": "Warm and cozy",
            "ingredients": "Water\nCarrots\nSalt",
            "steps": "   \n   ",  # ❌ whitespace only
            "category": "mains",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("steps", form.errors)
        self.assertEqual(form.errors["steps"][0], "Please enter at least one step.")

    def test_cleaned_data_strips_blank_lines(self):
        form = RecipeForm(data={
            "title": "Soup",
            "description": "Warm and cozy",
            "ingredients": "Water\n\nCarrots\n   \nSalt",
            "steps": "Boil water\n\nAdd carrots\nSeason",
            "category": "mains",
        })
        self.assertTrue(form.is_valid())
        cleaned_ingredients = form.cleaned_data["ingredients"]
        cleaned_steps = form.cleaned_data["steps"]
        self.assertEqual(cleaned_ingredients, "Water\nCarrots\nSalt")
        self.assertEqual(cleaned_steps, "Boil water\nAdd carrots\nSeason")
