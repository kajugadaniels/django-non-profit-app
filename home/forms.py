from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from home.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ("email", 'firstname', 'lastname','user_type')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = fields = ("email", 'firstname', 'lastname','user_type')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ("email", "password")

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

class MonthlyPrayerForm(forms.ModelForm):
    class Meta:
        model = MonthlyPrayer
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border-color-transparent-white-very-light bg-transparent placeholder-light form-control required',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border-color-transparent-white-very-light bg-transparent placeholder-light form-control required',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'border-color-transparent-white-very-light bg-transparent placeholder-light form-control required',
                'placeholder': 'Enter your phone number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'border-color-transparent-white-very-light bg-transparent placeholder-light form-control',
                'placeholder': 'Your message',
                'rows': 4
            })
        }
