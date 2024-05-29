from django.http import JsonResponse
from django.utils import timezone
from backend.models import *
from home.models import *
from django.shortcuts import render, redirect, get_object_or_404
import stripe
from django.core.paginator import Paginator
from dotenv import load_dotenv
load_dotenv()
import os
from home.forms import *
from django.views.decorators.csrf import csrf_protect
from .utils import *
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
publickey =  os.getenv("STRIPE_PUBLIC_KEY")

def index(request):
    students = Student.objects.all().order_by('-created_at')[:6]
    blog = Blog.objects.all().order_by('-created_at')[:4]
    slides = Slide.objects.filter(status=True).order_by('-created_at')[:3]
    student_count = Student.objects.count()
    projects = Project.objects.all().order_by('-created_at')
    project_count = Project.objects.count()
    testimony_count = Testimony.objects.count()
    
    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()

    sections = [mission, vision, values]

    context = {
        'students': students,
        'blog': blog,
        'slides': slides,
        'student_count': student_count,
        'project_count': project_count,
        'testimony_count': testimony_count,
        'sections': sections,
        'projects': projects
    }

    return render(request, 'frontend/index.html', context)

def history(request):
    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()

    sections = [mission, vision, values]
    
    context = {
        'sections': sections
    }

    return render(request, 'frontend/history.html', context)

def missionVisionValues(request):
    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()
    
    context = {
        'mission': mission,
        'vision': vision,
        'values': values,
    }

    return render(request, 'frontend/mission-vision-values.html', context)

def team(request):
    team = Team.objects.all().order_by('-created_at')

    context = {
        'team': team
    }

    return render(request, 'frontend/team.html', context)

def aboutRwanda(request):
    return render(request, 'frontend/about-rwanda.html')

def whatWeDo(request):
    return render(request, 'frontend/what-we-do/index.html')

def education(request):
    testimonies = Testimony.objects.all().order_by('-created_at')[:3]
    
    context = {
        'testimonies': testimonies
    }

    return render(request, 'frontend/what-we-do/education.html', context)

def vocationalTraining(request):
    return render(request, 'frontend/what-we-do/vocational-training.html')

def medicalCare(request):
    return render(request, 'frontend/what-we-do/medical-care.html')

def communityEmpowerment(request):
    return render(request, 'frontend/what-we-do/community-empowerment.html')

def teenMother(request):
    return render(request, 'frontend/what-we-do/teen-mother.html')

def students(request):
    student_list = Student.objects.all().order_by('-created_at')
    paginator = Paginator(student_list, 12)

    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {
        'students': students
    }

    return render(request, 'frontend/students/index.html', context)

def getStudent(request, slug):
    student = Student.objects.get(slug=slug)
    
    context = {
        'student': student
    }
    if request.method == 'POST':
        # TODO: sanitize data
        amoun = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        interval =  request.POST['paymentOptions']
        donate= donateFund(request,amoun, interval,slug, fullname, email,'frontend/students/show.html')
        return donate
    
    return render(request, 'frontend/students/show.html', context)

def give(request):
    projects = Project.objects.all().order_by('-created_at')[:4]

    context = {
        'projects': projects
    }

    return render(request, 'frontend/give.html', context)

def donate(request):
    student_list = Student.objects.all().order_by('-created_at')
    paginator = Paginator(student_list, 9)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 9)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'students': students,
        'projects': projects
    }

    if request.method == 'POST':
        # TODO: sanitize data
        amoun = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        interval =  request.POST['paymentOptions']
        donate= donateFund(request,amoun, interval,"", fullname, email,'frontend/sponsor/index.html')
        return donate
    return render(request, 'frontend/sponsor/index.html', context)


def store(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

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

def monthlyDonating(request):
    testimonies = Testimony.objects.all().order_by('-created_at')[:6]

    context = {
        'testimonies': testimonies
    }

    return render(request, 'frontend/monthly-donating.html', context)

def projects(request):
    project_list = Project.objects.all().order_by('-created_at')
    paginator = Paginator(project_list, 12)

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'projects': projects
    }

    return render(request, 'frontend/project/index.html', context)

def viewProject(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'project': project
    }

    return render(request, 'frontend/project/show.html', context)

def blog(request):
    blog_list = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog_list, 12)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    context = {
        'blogs': blogs
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

def prayWithUs(request):
    return render(request, 'frontend/pray-with-us.html')

def contact(request):
    return render(request, 'frontend/contact.html')

@csrf_protect
def checkout(request):
    cart = request.session.get('cart', [])

    if request.method == 'POST':
        amount = request.POST.get('selectedAmount')
        project_id = request.POST.get('selectedProject')
        project = Project.objects.get(id=project_id)

        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'].append({'project_id': project.id, 'title': project.title, 'amount': amount, 'image_url': project.image.url})
        request.session.modified = True
        
        return redirect('frontend:checkout')
    
    context = {
        'cart': cart
    }

    return render(request, 'frontend/checkout.html', context)

def get_cart_details(request):
    cart = request.session.get('cart', [])
    
    # Check if session has expired
    last_activity_time_str = request.session.get('_session_last_activity')
    last_activity_time = timezone.datetime.fromisoformat(last_activity_time_str) if last_activity_time_str else None
    
    if last_activity_time is not None and timezone.now() > last_activity_time + timezone.timedelta(hours=1):
        request.session['cart'] = []
        cart = []
    
    total_amount = sum(float(item['amount']) for item in cart)
    
    # Update last activity time as a string
    request.session['_session_last_activity'] = str(timezone.now())
    
    return JsonResponse({
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    })

def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if 'cart' in request.session and item_id in request.session['cart']:
            del request.session['cart'][item_id]
            request.session.modified = True  # Mark the session as modified
            return JsonResponse({'message': 'Item removed successfully'})
        else:
            return JsonResponse({'error': 'Item not found in cart'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def termsAndConditions(request):
    return render(request, 'frontend/term-and-condition.html')

def privacyPolicy(request):
    return render(request, 'frontend/privacy-policy.html')