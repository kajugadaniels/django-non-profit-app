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

class SendPrayerForm(forms.ModelForm):
    class Meta:
        model = SendPrayer
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

class JobApplicantForm(forms.ModelForm):
    class Meta:
        model = JobApplicant
        fields = ['name', 'email', 'phone', 'nationality', 'city', 'town', 'country', 'social_media_handles',
                  'is_married', 'has_children', 'church_name', 'is_church_member', 'ministry_areas',
                  'available_date', 'message', 'found_out_via']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Your Name', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Your Email', 'required': 'true'}),
            'phone': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Your Phone Number', 'required': 'true'}),
            'nationality': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Your Nationality', 'required': 'true'}),
            'city': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'City', 'required': 'true'}),
            'town': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Town', 'required': 'true'}),
            'country': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Country', 'required': 'true'}),
            'social_media_handles': forms.Textarea(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Social Media Handles', 'required': 'true'}),
            'is_married': forms.Select(choices=JobApplicant.YES_NO_CHOICES, attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required'}),
            'has_children': forms.Select(choices=JobApplicant.YES_NO_CHOICES, attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required'}),
            'church_name': forms.TextInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Church Name', 'required': 'true'}),
            'is_church_member': forms.Select(choices=JobApplicant.YES_NO_CHOICES, attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required'}),
            'ministry_areas': forms.Textarea(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Ministry Areas'}),
            'available_date': forms.DateInput(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'type': 'date', 'required': 'true'}),
            'message': forms.Textarea(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'placeholder': 'Your Message', 'required': 'true'}),
            'found_out_via': forms.Select(attrs={'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required', 'required': 'true'}),
        }