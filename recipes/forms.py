from django import forms
from .models import Recipe
from .models import Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'image', 'category', 'cook_time_minutes']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 6, 'placeholder': 'One ingredient per line'}),
            'steps': forms.Textarea(attrs={'rows': 8, 'placeholder': 'One step per line'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Leave a comment...'
            })
        }