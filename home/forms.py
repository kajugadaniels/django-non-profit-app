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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': 'true'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number', 'required': 'true'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Nationality', 'required': 'true'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'required': 'true'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town', 'required': 'true'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country', 'required': 'true'}),
            'social_media_handles': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Media Handles'}),
            'is_married': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_children': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'church_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Church Name', 'required': 'true'}),
            'is_church_member': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ministry_areas': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ministry Areas'}),
            'available_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'true'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'required': 'true'}),
            'found_out_via': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        }
