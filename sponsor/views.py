from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sponsor.models import *
from sponsor.forms import *

def user_login(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('sponsor:dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('sponsor:login')
        else:
            messages.error(request, 'Login failed. Please check your input.')
            return redirect('sponsor:login')
    else:
        form = MemberLoginForm()

    context = {
        'form': form
    }

    return render(request, 'frontend/auth/account.html', context)

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(request, username=user.email, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'User registered and logged in successfully.')
                return redirect('sponsor:login')
            else:
                messages.error(request, 'User registration failed. Please try again.')
        else:
            messages.error(request, 'User registration failed. Please check your input.')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'frontend/auth/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('sponsor:login')

@login_required
def dashboard(request):
    return render(request, 'backend/sponsor/dashboard.html')

@login_required
def letter(request):
    letters = Letter.objects.filter(sender=request.user)

    context = {
        'letters': letters
    }

    return render(request, 'backend/sponsor/letter/index.html', context)

@login_required
def writeLetter(request):
    pass

@login_required
def letterEdit(request, slug):
    pass

@login_required
def letterDelete(request, slug):
    pass