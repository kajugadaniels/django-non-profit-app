from random import sample
from backend.models import *
from django.shortcuts import render

def index(request):
    all_students = list(Student.objects.all())
    random_students = sample(all_students, 7)
    blog = Blog.objects.all()
    
    context = {
        'students': random_students,
        'blog': blog
    }

    return render(request, 'frontend/index.html', context)

def history(request):
    return render(request, 'frontend/history.html')

def team(request):
    team = Team.objects.all()

    context = {
        'team': team
    }

    return render(request, 'frontend/team.html', context)

def whatWeDo(request):
    return render(request, 'frontend/what-we-do/index.html')

def education(request):
    return render(request, 'frontend/what-we-do/education.html')

def farmingOutreach(request):
    return render(request, 'frontend/what-we-do/farming-outreach.html')

def feedingOutreach(request):
    return render(request, 'frontend/what-we-do/feeding-outreach.html')

def educationSponsorship(request):
    return render(request, 'frontend/what-we-do/educational-sponsorship.html')

def medicalCare(request):
    return render(request, 'frontend/what-we-do/medical-care.html')

def OasisAcademy(request):
    return render(request, 'frontend/what-we-do/oasis-academy.html')

def gospelTeaching(request):
    return render(request, 'frontend/what-we-do/gospel-teaching.html')

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

def give(request):

    return render(request, 'frontend/give.html')

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

def blog(request):
    blog = Blog.objects.all()

    context = {
        'blog': blog
    }

    return render(request, 'frontend/blog/index.html', context)

def viewBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    
    context = {
        'blog': blog
    }

    return render(request, 'frontend/blog/show.html', context)

def faq(request):
    return render(request, 'frontend/faq.html')