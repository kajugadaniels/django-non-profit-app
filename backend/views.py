from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from home.forms import UserLoginForm
from django.contrib import messages
from backend.models import Student
from backend.forms import StudentForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('backend:dashboard')

    form = UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.email}!')
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please check your email and password.')
            return redirect('backend:login')
    return render(request, 'backend/auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('backend:login')

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required
def getStudents(request):
    students = Student.objects.all()
    
    context = {
        'students': students,
    }

    return render(request, 'backend/students/index.html', context)

@login_required
def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        spo_cover = request.POST.get('spo_cover')
        description = request.POST.get('description')

        # Create the slug based on the student name
        slug = slugify(name)

        # Create the student object
        student = Student.objects.create(
            name=name,
            slug=slug,
            image=image,
            birthday=birthday,
            gender=gender,
            spo_cover=spo_cover,
            description=description
        )

        # Redirect to a success page or another view
        return redirect('backend:getStudents')  # Change 'success_page' to your actual URL name or view
    else:
        return render(request, 'backend/students/create.html')

@login_required
def editStudent(request):
    return render(request, 'backend/students/edit.html')