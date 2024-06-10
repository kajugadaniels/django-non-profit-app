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

class DonateToStudentForm(forms.ModelForm):
    class Meta:
        model = DonateToStudent
        fields = [
            'donationTitle',
            'donationId',
            'productId',
            'amount',
            'status',
            'beneficiary',
            'paymentMode',
            'donatedBy',
            'email',
        ]

        widgets = {
            'donationTitle': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Donation Title'}),
            'donationId': forms.HiddenInput(),
            'productId': forms.HiddenInput(),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'status': forms.Select(attrs={'class': 'form-control', 'value': 'Pending'}),
            'beneficiary': forms.HiddenInput(attrs={'class': 'form-control'}),
            'paymentMode': forms.Select(attrs={'class': 'form-control'}),
            'donatedBy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

        labels = {
            'donationTitle': 'Donation Title',
            'amount': 'Amount',
            'status': 'Status',
            'beneficiary': 'Beneficiary',
            'paymentMode': 'Payment Mode',
            'donatedBy': 'Fullname',
            'email': 'Email',
        }