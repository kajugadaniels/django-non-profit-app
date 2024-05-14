from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import UserLoginForm
from django.contrib import messages

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