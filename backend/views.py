from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.forms import *
from django.contrib import messages
from home.models import *
from backend.models import *
from backend.forms import *

# Authentication Section

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

# Dashboard Section

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard.html')

# Student Section

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
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('backend:getStudents')
        else:
            messages.error(request, 'Error updating the student. Please check the form.')
    else:
        form = StudentForm(instance=student)
        
    context = {
        'form': form,
        'student': student
    }

    return render(request, 'backend/students/edit.html', context)

@login_required
def deleteStudent(request, slug):
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        student.delete()
        messages.success(request, 'Student deleted successfully!')

    return redirect('backend:getStudents')

# Team Section

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
    person = get_object_or_404(Team, slug=slug)

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team updated successfully!')
            return redirect('backend:getTeam')
        else:
            messages.error(request, 'Error updating the team member. Please check the form.')
    else:
        form = TeamForm(instance=person)
        
    context = {
        'form': form,
        'person': person
    }

    return render(request, 'backend/team/edit.html', context)

@login_required
def deleteTeam(request, slug):
    if request.method == 'POST':
        team = get_object_or_404(Team, slug=slug)
        team.delete()
        messages.success(request, 'Team deleted successfully!')

    return redirect('backend:getTeam')

# Product Section

@login_required
def getProduct(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'backend/store/index.html', context)

@login_required
def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('backend:getProduct')
        else:
            messages.error(request, 'Error creating a product. Please check the form.')
    else:
        form = ProductForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'backend/store/create.html', context)

@login_required
def editProduct(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('backend:getProduct')
        else:
            messages.error(request, 'Error updating the product. Please check the form.')
    else:
        form = ProductForm(instance=product)
        
    context = {
        'form': form,
        'product': product
    }
    
    return render(request, 'backend/store/edit.html', context)

@login_required
def deleteProduct(request, slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        messages.success(request, 'Product deleted successfully!')

    return redirect('backend:getProduct')

# Projects Section

@login_required
def getProjects(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }
    
    return render(request, 'backend/projects/index.html', context)

@login_required
def addProject(request):
    return render(request, 'backend/projects/create.html')

@login_required
def editProject(request):
    return render(request, 'backend/projects/edit.html')

@login_required
def deleteProject(request):
    pass

# Blog Section

@login_required
def getBlog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'backend/blog/index.html', context)

@login_required
def addBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog created successfully!')
            return redirect('backend:getBlog')
        else:
            messages.error(request, 'Error creating a blog. Please check the form.')
    else:
        form = BlogForm()
        
    context = {
        'form': form
    }

    return render(request, 'backend/blog/create.html', context)

@login_required
def editBlog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('backend:getBlog')
        else:
            messages.error(request, 'Error updating the blog. Please check the form.')
    else:
        form = BlogForm(instance=blog)
        
    context = {
        'form': form,
        'blog': blog
    }
    
    return render(request, 'backend/blog/edit.html', context)

@login_required
def deleteBlog(request, slug):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, slug=slug)
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        
    return redirect('backend:getBlog')

# Donate Section

@login_required
def donate(request):
    donate = Donate.objects.all()
    
    context = {
        'donate': donate
    }
    
    return render(request, 'backend/donate/donate.html', context)

@login_required
def donateToStudent(request):
    donate = DonateToStudents.objects.all()
    
    context = {
        'donate': donate
    }
    
    return render(request, 'backend/donate/donate-to-student.html', context)