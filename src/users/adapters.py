from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
 
class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        extension = '@khi.iba.edu.pk'
        if extension not in email:
            raise ValidationError('please use your IBA email.\
                                                  email us at fluffcoding@gmail.com for more information')
        return email