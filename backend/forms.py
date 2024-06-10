from django import forms
from django_quill.forms import QuillFormField
from backend.models import *

class StudentForm(forms.ModelForm):
    # description = QuillFormField()

    class Meta:
        model = Student
        fields = ['name', 'image', 'birthday', 'gender', 'benefits', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}, choices=Student.GENDER_CHOICES),
            'benefits': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Benefits Of Sponsorship'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Information'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'position', 'category', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Position'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
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

class VisitingRequestForm(forms.ModelForm):
    class Meta:
        model = VisitingRequest
        fields = ['name', 'email', 'phone', 'org_name', 'n_visitors', 'req_visit', 'purpose']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'placeholder': 'Enter your phone number'
            }),
            'org_name': forms.TextInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'placeholder': 'Enter organization name'
            }),
            'n_visitors': forms.NumberInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'placeholder': 'Enter number of visitors'
            }),
            'req_visit': forms.DateInput(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control required',
                'type': 'date'
            }),
            'purpose': forms.Textarea(attrs={
                'class': 'fw-500 ps-0 border-radius-0px border-color-dark-gray bg-transparent form-control',
                'placeholder': 'Purpose of your visit',
                'rows': 4
            }),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'phone', 'dob', 'city', 'country', 'about']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control required',
                'placeholder': 'Enter your phone number'
            }),
            'dob': forms.DateInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control',
                'type': 'date'
            }),
            'city': forms.TextInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control',
                'placeholder': 'Enter city you live in'
            }),
            'country': forms.TextInput(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control',
                'placeholder': 'Enter country you live in'
            }),
            'about': forms.Textarea(attrs={
                'class': 'ps-0 border-radius-0px border-color-extra-medium-gray bg-transparent form-control',
                'placeholder': 'What specific talents or skills would you hope to utilize at African Oasis Foundation?',
                'rows': 4
            })
        }

class ResourceForm(forms.ModelForm):
    UPLOAD_TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
    ]

    upload_type = forms.ChoiceField(choices=UPLOAD_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Resource
        fields = ['category', 'title', 'upload_type', 'image', 'file']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/png,image/jpg'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError("Only JPG, JPEG, and PNG files are allowed.")
        return image

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.lower().endswith(('.pdf', '.docx')):
                raise forms.ValidationError("Only PDF and DOCX files are allowed.")
        return file

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campaign Title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class FundraisingForm(forms.ModelForm):
    class Meta:
        model = Fundraising
        fields = ['name', 'email', 'date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-name border-radius-4px form-control required',
                'placeholder': 'Enter your name*'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border-radius-4px form-control required',
                'placeholder': 'Enter your email address*'
            }),
            'date': forms.DateInput(attrs={
                'class': 'border-radius-4px form-control required',
                'placeholder': 'When will you want to start your fundraiser?',
                'type': 'date'
            }),
        }

class PolicyForm(forms.ModelForm):
    description = QuillFormField()

    class Meta:
        model = Policy
        fields = ['category', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description-container'}),
        }