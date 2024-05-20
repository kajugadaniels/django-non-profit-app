from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import *
from django.contrib import messages
from backend.models import *
from backend.forms import *

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
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('backend:getStudents')  # Redirect to the student list page or another appropriate page
        else:
            messages.error(request, 'Error creating student. Please check the form.')
    else:
        form = StudentForm()
    return render(request, 'backend/students/create.html', {'form': form})

@login_required
def editStudent(request):
    return render(request, 'backend/students/edit.html')

@login_required
def getTeam(request):
    return render(request, 'backend/team/index.html')

@login_required
def addTeam(request):
    return render(request, 'backend/team/create.html')

@login_required
def editTeam(request):
    return render(request, 'backend/team/edit.html')