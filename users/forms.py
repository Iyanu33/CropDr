from django import forms
from django.contrib.auth.forms import UserCreationForm

def SignupForm(UserCreationForm):
    """docstring for signup"""
    Class meta:
        models = User
        field = ("username","email")

def LoginForm(forms.Form):
    """docstring for LogInform"""
    email = forms.Charfield()
    password = forms.Charfield()


def EditProfileForm(forms.Form):
    """docstring for EditProfileForm"""
    username = forms.Charfield()
    about_me = forms.Charfield(widget = forms.Textarea())
    my_image = forms.Imagefield(required=False)

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

    
    
