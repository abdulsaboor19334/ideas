from django import forms

from .models import Posts


class PostsForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    class Meta:
        model = Posts
        fields = ['topic', 'title', 'body', 'image', 'anonymous' ]
        