from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets

from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    birthdate = forms.DateField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'password1',
            'password2',
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture']
        widgets={
            'profile_picture':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})
        }