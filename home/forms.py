from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import UserAccount

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


class DonationForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    email = forms.EmailField()
    fullname = forms.CharField(max_length=100, required=True)
    paymentOptions = forms.CharField(max_length=100, required=True)
    