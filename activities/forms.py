from .models import Review, Experience
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('name', 'slug', 'city', 'category', 'description', 'excerpt',
                  'price', 'directions', 'website', 'image', )
