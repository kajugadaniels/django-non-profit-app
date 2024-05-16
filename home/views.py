from random import sample
from backend.models import *
from django.shortcuts import render

def index(request):
    all_students = list(Student.objects.all())

    # Select 7 students randomly
    random_students = sample(all_students, 7)
    
    context = {
        'students': random_students,
    }

    return render(request, 'frontend/index.html', context)

def history(request):
    return render(request, 'frontend/history.html')

def whatWeDo(request):
    return render(request, 'frontend/what-we-do/index.html')

def students(request):
    students = Student.objects.all();
    
    context = {
        'students': students
    }

    return render(request, 'frontend/students/index.html', context)

def getStudent(request, slug):
    student = Student.objects.get(slug=slug)
    
    context = {
        'student': student
    }
    
    return render(request, 'frontend/students/show.html', context)

def donate(request):
    students = Student.objects.all()
    
    context = {
        'students': students
    }

    return render(request, 'frontend/sponsor/index.html', context)

def store(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'frontend/store/index.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    
    context = {
        'product': product
    }

    return render(request, 'frontend/store/product.html', context)