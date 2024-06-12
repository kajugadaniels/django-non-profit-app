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

    return render(request, 'frontend/auth/login.html', context)

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
                error_message = 'User registration failed. '
                for field, errors in form.errors.items():
                    error_message += f"{field}: {', '.join(errors)}. "
                messages.error(request, error_message.strip())
        else:
            error_message = 'User registration failed. '
            for field, errors in form.errors.items():
                error_message += f"{field}: {', '.join(errors)}. "
            messages.error(request, error_message.strip())
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    
    return render(request, 'frontend/auth/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('sponsor:login')

@login_required
def dashboard(request):
    return render(request, 'backend/sponsor/dashboard.html')

@login_required
def getLetters(request):
    letters = Letter.objects.filter(sender=request.user)

    context = {
        'letters': letters
    }

    return render(request, 'backend/sponsor/letter/index.html', context)

@login_required
def writeLetter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Letter created successfully!')
            return redirect('sponsor:getLetters')
        else:
            error_message = 'Error creating a letter. '
            for field, errors in form.errors.items():
                error_message += f"{field}: {', '.join(errors)}. "
            messages.error(request, error_message.strip())
    else:
        form = LetterForm(user=request.user)

    context = {
        'form': form
    }

    return render(request, 'backend/sponsor/letter/create.html', context)

@login_required
def letterEdit(request, slug):
    pass

@login_required
def letterDelete(request, slug):
    pass