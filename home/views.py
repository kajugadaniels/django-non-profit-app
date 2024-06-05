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

def get_logos():
    logos = {
        'color_logo': Logo.objects.filter(section='color_logo').first(),
        'black_logo': Logo.objects.filter(section='black_logo').first(),
        'white_logo': Logo.objects.filter(section='white_logo').first(),
        'favicon': Logo.objects.filter(section='favicon').first(),
    }
    return logos

def index(request):
    students = Student.objects.all().order_by('-created_at')[:6]
    blog = Blog.objects.all().order_by('-created_at')[:4]
    slides = Slide.objects.filter(status=True).order_by('-created_at')[:3]
    student_count = Student.objects.count()
    projects = Project.objects.all().order_by('-created_at')[:3]
    project_count = Project.objects.count()
    testimony_count = News.objects.count()

    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()

    sections = [mission, vision, values]
    
    logos = get_logos()

    context = {
        'students': students,
        'blog': blog,
        'slides': slides,
        'student_count': student_count,
        'project_count': project_count,
        'testimony_count': testimony_count,
        'sections': sections,
        'projects': projects,
        **logos
    }

    return render(request, 'frontend/index.html', context)

def history(request):
    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()

    sections = [mission, vision, values]
    
    logos = get_logos()
    
    context = {
        'sections': sections,
        **logos
    }

    return render(request, 'frontend/history.html', context)

def missionVisionValues(request):
    mission = MissionVisionValues.objects.filter(section='mission').first()
    vision = MissionVisionValues.objects.filter(section='vision').first()
    values = MissionVisionValues.objects.filter(section='values').first()
    
    logos = get_logos()
    
    context = {
        'mission': mission,
        'vision': vision,
        'values': values,
        **logos
    }

    return render(request, 'frontend/mission-vision-values.html', context)

def team(request):
    team = Team.objects.all().order_by('-created_at')
    
    logos = get_logos()

    context = {
        'team': team,
        **logos
    }

    return render(request, 'frontend/team.html', context)

def aboutRwanda(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/about-rwanda.html', context)

def whatWeDo(request):
    logos = get_logos()
    
    context = {
        **logos
    }
    return render(request, 'frontend/what-we-do/index.html', context)

def education(request):
    news = News.objects.filter(category='education', status=True).order_by('-created_at')
    testimonies = Testimony.objects.all().order_by('-created_at')[:3]
    logos = get_logos()
    
    context = {
        'news': news,
        'testimonies': testimonies,
        **logos
    }

    return render(request, 'frontend/what-we-do/education.html', context)

def vocationalTraining(request):
    news = News.objects.filter(category='vocational-training', status=True).order_by('-created_at')
    logos = get_logos()

    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/vocational-training.html', context)

def medicalCare(request):
    news = News.objects.filter(category='medical-care', status=True).order_by('-created_at')
    logos = get_logos()

    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/medical-care.html', context)

def communityEmpowerment(request):
    news = News.objects.filter(category='community-empowerment', status=True).order_by('-created_at')
    testimonies = Testimony.objects.all().order_by('-created_at')[:6]
    logos = get_logos()

    context = {
        'news': news,
        'testimonies': testimonies,
        **logos
    }

    return render(request, 'frontend/what-we-do/community-empowerment.html', context)

def tungaWomen(request):
    news = News.objects.filter(category='tunga-mothers', status=True).order_by('-created_at')
    logos = get_logos()

    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/tunga-women-initiative.html', context)

def story(request, slug):
    story = News.objects.get(slug=slug)
    logos = get_logos()

    context = {
        'story': story,
        **logos
    }

    return render(request, 'frontend/what-we-do/story.html', context)

def students(request):
    student_list = Student.objects.all().order_by('-created_at')
    paginator = Paginator(student_list, 12)

    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    logos = get_logos()

    context = {
        'students': students,
        **logos
    }

    return render(request, 'frontend/students/index.html', context)

def getStudent(request, slug):
    student = Student.objects.get(slug=slug)
    logos = get_logos()
    
    context = {
        'student': student,
        **logos
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
    logos = get_logos()

    context = {
        'projects': projects,
        **logos
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
    logos = get_logos()

    context = {
        'students': students,
        'projects': projects,
        **logos
    }

    if request.method == 'POST':
        # TODO: sanitize data
        amoun = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        interval =  request.POST['paymentOptions']
        donate= donateFund(request,amoun, interval,"", fullname, email,'frontend/sponsor/index.html',"")
        return donate
    return render(request, 'frontend/sponsor/index.html', context)


def store(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    logos = get_logos()

    context = {
        'products': products,
        **logos
    }

    return render(request, 'frontend/store/index.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    logos = get_logos()
    
    context = {
        'product': product,
        **logos
    }

    return render(request, 'frontend/store/product.html', context)

def monthlyDonating(request):
    testimonies = Testimony.objects.all().order_by('-created_at')[:6]
    logos = get_logos()

    context = {
        'testimonies': testimonies,
        **logos
    }

    return render(request, 'frontend/monthly-donating.html', context)

def projects(request):
    project_list = Project.objects.all().order_by('-created_at')
    paginator = Paginator(project_list, 12)

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    
    logos = get_logos()

    context = {
        'projects': projects,
        **logos
    }

    return render(request, 'frontend/project/index.html', context)

def viewProject(request, slug):
    project = get_object_or_404(Project, slug=slug)
    logos = get_logos()
    
    context = {
        'project': project,
        **logos
    }

    return render(request, 'frontend/project/show.html', context)

def blog(request):
    blog_list = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog_list, 12)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    logos = get_logos()

    context = {
        'blogs': blogs,
        **logos
    }

    return render(request, 'frontend/blog/index.html', context)

def viewBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    logos = get_logos()
    
    context = {
        'blog': blog,
        **logos
    }

    return render(request, 'frontend/blog/show.html', context)

def faq(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/faq.html', context)

def prayWithUs(request):
    return render(request, 'frontend/pray-with-us.html')

def contact(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/contact.html', context)

@csrf_protect
def checkout(request):
    cart = request.session.get('cart', [])
    logos = get_logos()

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
        'cart': cart,
        **logos
    }

    return render(request, 'frontend/checkout.html', context)

def checkoutpay(request):
    cart = request.session.get('cart', [])
    logos = get_logos()
    context = {
            'cart': cart,
            **logos
        }
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        phonenumber = request.POST['phonenumber']
        state = request.POST['state']
        street = request.POST['street']
        street1 = request.POST['street1']
        zip = request.POST['zip']
        amount = request.POST['amount']
        donate= donateFund(request,amount, 'one',"", firstname, email,'frontend/checkout.html',"")
        gift = DonateGifts()
        gift.email = email
        gift.firstname = firstname
        gift.phoneNumber = phonenumber
        gift.lastname= lastname
        gift.streetAddress = street
        gift.city = city
        gift.zip = zip
        gift.state= state
        gift.streetAddressCity =street1
        gift.save()
        return donate

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

def getInvolved(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/get-involved.html', context)

def termsAndConditions(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/term-and-condition.html', context)

def privacyPolicy(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/privacy-policy.html', context)

def resources(request):
    logos = get_logos()
    
    context = {
        **logos
    }

    return render(request, 'frontend/resources.html', context)