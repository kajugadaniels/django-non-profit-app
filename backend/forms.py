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

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['image', 'status']
        widgets = {
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class MissionVisionValuesForm(forms.ModelForm):
    class Meta:
        model = MissionVisionValues
        fields = ['section', 'title', 'description', 'icon']
        widgets = {
            'section': forms.Select(choices=MissionVisionValues.SECTION_CHOICES, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['section', 'image']

class EditLogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['image']