from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class SignUpForm(UserCreationForm):
    """docstring for signup"""
    class meta:
        models = User
        field = ("username","email")

class LoginForm(forms.Form):
    """docstring for LogInform"""
    email = forms.CharField()
    password = forms.CharField()

class EditProfileForm(forms.Form):
    """docstring for EditProfileForm"""
    username = forms.CharField()
    about_me = forms.CharField(widget = forms.Textarea())
    my_image = forms.ImageField(required=False)

def __init__(self, original_username, *args,**kwargs):
    super().__init__(*args,**kwargs)
    self.original_username = original_username

def clean_username(self):
    """this function clear username if already exist"""
    username = self.cleaned_data['username']
    if username != original_username:
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'A user with that username already exists'
            )

    
    
