from .models import Reviews
from django import forms
from django_starfield import Stars

class ReviewForm(forms.ModelForm):
    individual_rating = forms.IntegerField(widget=Stars)
    class Meta:
        model = Reviews
        fields = ['user','instructor','individual_rating','description']
