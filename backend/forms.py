from django import forms
from django_quill.forms import QuillFormField
from backend.models import *

class StudentForm(forms.ModelForm):
    # description = QuillFormField()

    class Meta:
        model = Student
        fields = ['name', 'image', 'birthday', 'gender', 'spo_cover', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}, choices=Student.GENDER_CHOICES),
            'spo_cover': forms.Select(attrs={'class': 'form-select'}, choices=Student.SPONSORSHIP_COVER_CHOICES),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Information'}),
        }

class TeamForm(forms.ModelForm):
    # description = QuillFormField()

    class Meta:
        model = Team
        fields = ['name', 'position', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Position'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class ProductForm(forms.ModelForm):
    # description = QuillFormField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }