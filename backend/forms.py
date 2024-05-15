from django import forms
from django_quill.forms import QuillFormField
from backend.models import Student

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