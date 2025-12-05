from django import forms
from .models import Recipe
from .models import Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'steps',
            'image',
            'category',
            'cook_time_minutes',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter recipe title',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Optional description',
                'rows': 3,
                'class': 'form-control'
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'Enter one ingredient per line (e.g. 200g flour)',
                'rows': 6,
                'class': 'form-control'
            }),
            'steps': forms.Textarea(attrs={
                'placeholder': 'Enter one step per line (e.g. Preheat oven to 180°C)',
                'rows': 8,
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'cook_time_minutes': forms.NumberInput(attrs={
                'placeholder': 'Cooking time in minutes',
                'class': 'form-control'
            }),
        }


    def clean_ingredients(self):
        data = self.cleaned_data['ingredients']
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        if not lines:
            raise forms.ValidationError("Please enter at least one ingredient.")
        return "\n".join(lines)

    def clean_steps(self):
        data = self.cleaned_data['steps']
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        if not lines:
            raise forms.ValidationError("Please enter at least one step.")
        return "\n".join(lines)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'id': 'comment-box',                # matches your CSS
                'class': 'form-control',            # keep Bootstrap base class
                'rows': 3,
                'placeholder': 'Leave a comment...',
            }),
        }
