from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('mains', 'Mains'),
        ('desserts', 'Desserts'),
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('snacks', 'Snacks'),
        ('drinks', 'Drinks'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text='One per line')
    steps = models.TextField(help_text='One step per line')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cook_time_minutes = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
