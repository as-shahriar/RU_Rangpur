from django import forms
from django.contrib.auth.models import User
from ru.models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('img',)
        help_texts = {
            'img': None,
        }
