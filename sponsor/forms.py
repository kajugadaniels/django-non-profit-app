from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import *

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

class UserRegistrationForm(UserCreationForm):
    user_type_choices = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    user_type = forms.ChoiceField(
        choices=user_type_choices,
        initial='user',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = UserAccount
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'user_type', 'password1', 'password2']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Lastname'}),
            'email': forms.EmailInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Email'}),
            'phonenumber': forms.NumberInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Phone Number'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserAccount.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

class MemberLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'mb-20px bg-very-light-gray form-control required', 'placeholder': 'Enter your password'})
    )