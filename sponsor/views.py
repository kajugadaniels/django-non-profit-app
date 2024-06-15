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
    letters = Letter.objects.filter(sponsor=request.user)

    context = {
        'letters': letters
    }

    return render(request, 'backend/sponsor/letter/index.html', context)

@login_required
def writeLetter(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if not FavoriteStudent.objects.filter(sponsor=request.user, student=student).exists():
        messages.error(request, "You can only write letters to your favorite students.")
        return redirect('sponsor_dashboard')

    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.sponsor = request.user
            letter.sponsor_name = f"{request.user.firstname} {request.user.lastname}"
            letter.student = student
            letter.save()
            messages.success(request, 'Letter successfully sent!')
            return redirect('sponsor:getLetters')
    else:
        form = LetterForm()

    context = {
        'form': form,
        'student': student
    }

    return render(request, 'backend/sponsor/letter/create.html', context)

@login_required
def letterDelete(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    if request.method == 'POST':
        letter.delete()
        messages.success(request, 'Letter deleted successfully!')

    return redirect('sponsor:getLetters')

@login_required
def students(request):
    students = FavoriteStudent.objects.filter(sponsor=request.user).select_related('student')

    context = {
        'students': students,
    }

    return render(request, 'backend/sponsor/students/index.html', context)

def getStudent(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if not FavoriteStudent.objects.filter(sponsor=request.user, student=student).exists():
        messages.error(request, "You can only donate to your favorite students.")
        return redirect('sponsor:students')

    if request.method == 'POST':
        form = SponsorDonateStudentForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.sponsor = request.user
            donation.student = student
            donation.save()
            messages.success(request, 'Donation successfully made!')
            return redirect('sponsor:studentsDonationHistory')
    else:
        form = SponsorDonateStudentForm()
    
    context = {
        'form': form,
        'student': student,
    }
    
    return render(request, 'backend/sponsor/students/show.html', context)

@login_required
def donationHistory(request):
    donations = SponsorDonateStudent.objects.filter(sponsor=request.user).order_by('-created_at')

    context = {
        'donations': donations
    }

    return render(request, 'backend/sponsor/students/history.html', context)