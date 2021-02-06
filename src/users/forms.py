from allauth.account.forms import SignupForm
from django import forms

class CustomSignup(SignupForm):
    

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@khi.iba.edu.pk" not in data:   # any check you need
            raise forms.ValidationError("Must be a gmail address")
        return data