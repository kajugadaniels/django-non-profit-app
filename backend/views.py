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
            return redirect('backend:getStudents')
        else:
            messages.error(request, 'Error creating student. Please check the form.')
    else:
        form = StudentForm()
    
    context = {
        'form': form
    }

    return render(request, 'backend/students/create.html', context)

@login_required
def editStudent(request, slug):
    student = Student.objects.get(slug=slug)
    
    context = {
        'student': student
    }

    return render(request, 'backend/students/edit.html', context)

@login_required
def getTeam(request):
    team = Team.objects.all()
    
    context = {
        'team': team,
    }
    
    return render(request, 'backend/team/index.html', context)

@login_required
def addTeam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team Member created successfully!')
            return redirect('backend:getTeam')
        else:
            messages.error(request, 'Error creating a team member. Please check the form.')
    else:
        form = TeamForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/team/create.html', context)

@login_required
def editTeam(request, slug):
    person = Team.objects.get(slug=slug)
    
    context = {
        'person': person
    }

    return render(request, 'backend/team/edit.html', context)

@login_required
def getBlog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'backend/blog/index.html', context)

@login_required
def addBlog(request):
    return render(request, 'backend/blog/create.html')

@login_required
def editBlog(request, slug):
    return render(request, 'backend/blog/edit.html')