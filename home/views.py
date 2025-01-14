from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from backend.models import *
from home.models import *
from sponsor.models import *
from django.contrib import messages
from django.db.models import Sum
import stripe
from django.core.paginator import Paginator
from dotenv import load_dotenv
load_dotenv()
import os
from home.forms import *
from backend.forms import *
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
    projects = ProjectDetails.objects.filter(category="Special Projects").order_by('-created_at')[:3]
    projectRegular = ProjectDetails.objects.filter(category="Regular Projects").order_by('-created_at')[:3]
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
        'sections': sections,
        'projects': projects,
        'projectRegular': projectRegular,
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
    localStaff = Team.objects.filter(category='Rwanda Staff').order_by('created_at')
    statesideStaff = Team.objects.filter(category='Stateside Staff').order_by('created_at')
    logos = get_logos()
    context = {
        'localStaff': localStaff,
        'statesideStaff': statesideStaff,
        **logos
    }
    return render(request, 'frontend/team/index.html', context)

def teamMember(request, slug):
    member = get_object_or_404(Team, slug=slug)
    logos = get_logos()
    context = {
        'member': member,
        **logos
    }
    return render(request, 'frontend/team/show.html', context)

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
    news = News.objects.filter(category='Education').order_by('-created_at')
    logos = get_logos()
    
    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/education.html', context)

def vocationalTraining(request):
    news = News.objects.filter(category='Vocational Training').order_by('-created_at')
    logos = get_logos()

    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/vocational-training.html', context)

def medicalCare(request):
    news = News.objects.filter(category='Medical Care').order_by('-created_at')
    logos = get_logos()

    context = {
        'news': news,
        **logos
    }

    return render(request, 'frontend/what-we-do/medical-care.html', context)

def communityEmpowerment(request):
    news = News.objects.filter(category='Community Empowerment').order_by('-created_at')
    testimonies = Testimony.objects.all().order_by('-created_at')[:6]
    logos = get_logos()

    context = {
        'news': news,
        'testimonies': testimonies,
        **logos
    }

    return render(request, 'frontend/what-we-do/community-empowerment.html', context)

def tungaWomen(request):
    news = News.objects.filter(category='Tunga Women Initiative').order_by('-created_at')
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
    student = get_object_or_404(Student, slug=slug)
    logos = get_logos()
    
    context = {
        'student': student,
        'slug': slug,
        **logos
    }

    if request.method == 'POST':
        # Handle donation logic if this is a donation request
        if 'amount' in request.POST:
            amount = request.POST['amount']
            email = request.POST['email']
            fullname = request.POST['fullname']
            interval = request.POST['paymentOptions']
            donate = donateFund(request, amount, interval, slug, fullname, email, 'frontend/students/show.html', '')
            return donate
        
        # Handle favorite student logic
        if 'favorite_student' in request.POST:
            try:
                favorite, created = FavoriteStudent.objects.get_or_create(sponsor=request.user, student=student)
                if created:
                    messages.success(request, 'You have successfully added this student to your favorites.')
                else:
                    messages.info(request, 'This student is already in your favorites.')
            except Exception as e:
                messages.error(request, 'An error occurred while trying to add this student to your favorites.')
            return redirect('sponsor:students')

    return render(request, 'frontend/students/show.html', context)

def give(request):
    projects = ProjectDetails.objects.all().order_by('-created_at')[:4]
    logos = get_logos()

    context = {
        'projects': projects,
        **logos
    }

    return render(request, 'frontend/give.html', context)

def donate(request):
    student_list = Student.objects.all().order_by('-created_at')
    paginator = Paginator(student_list, 12)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    project_list = ProjectDetails.objects.all()
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
        amount = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        interval =  request.POST['paymentOptions']
        donate= donateFund(request,amount, interval,"", fullname, email,'frontend/sponsor/index.html',"")
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
        'slug': slug,
        **logos
    }
    if request.method == 'POST':
        amount = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        interval =  request.POST['paymentOptions']
        donate= donateFund(request,amount, interval,slug, fullname, email,'frontend/store/product.html',slug)
        return donate


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
    project_list = ProjectDetails.objects.all().order_by('-created_at')
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
    project = get_object_or_404(ProjectDetails, slug=slug)
    logos = get_logos()
    
    raised_amount = DonateGifts.objects.filter(productid=project.id).aggregate(Sum('amount'))['amount__sum'] or 0
    total_donations = DonateGifts.objects.filter(productid=project.id).count()
    recent_donation = DonateGifts.objects.filter(productid=project.id).order_by('-id').first()
    highest_donor = DonateGifts.objects.filter(productid=project.id).order_by('-amount').first()
    first_donor = DonateGifts.objects.filter(productid=project.id).order_by('id').first()
    
    if project.target:
        try:
            target = float(project.target)
            percentage_raised = (raised_amount / target) * 100
        except (ValueError, ZeroDivisionError):
            percentage_raised = 0
    else:
        percentage_raised = 0
    
    context = {
        'project': project,
        'raised_amount': raised_amount,
        'total_donations': total_donations,
        'recent_donation': recent_donation,
        'highest_donor': highest_donor,
        'first_donor': first_donor,
        'percentage_raised': percentage_raised,
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
    if request.method == 'POST':
        form = SendPrayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We have successfully received your prayer')
            return redirect('frontend:prayWithUs')
    else:
        form = SendPrayerForm()
    
    logos = get_logos()
    
    context = {
        **logos,
        'form': form
    }

    return render(request, 'frontend/pray-with-us.html', context)

def jobVacancy(request):
    job_list = JobVacancy.objects.all().order_by('-created_at')
    paginator = Paginator(job_list, 12)

    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    
    logos = get_logos()

    context = {
        'jobs': jobs,
        **logos
    }

    return render(request, 'frontend/job-vacancy/index.html', context)

def viewJobVacancy(request, slug):
    job = JobVacancy.objects.get(slug=slug)
    logos = get_logos()
    
    if request.method == 'POST':
        form = JobApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job_vacancy = job
            applicant.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('frontend:viewJobVacancy', slug=job.slug)
        else:
            messages.error(request, 'There was an error in your application. Please check the form and try again.')
    else:
        form = JobApplicantForm()
    
    context = {
        'job': job,
        'form': form,
        **logos
    }

    return render(request, 'frontend/job-vacancy/show.html', context)

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
        project = ProjectDetails.objects.get(id=project_id)

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

    return render(request, 'frontend/get-involved/index.html', context)

def visitUs(request):
    if request.method == 'POST':
        form = VisitingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your visit request has been submitted successfully.')
            return redirect('frontend:visitUs')
    else:
        form = VisitingRequestForm()

    logos = get_logos()
    
    context = {
        **logos,
        'form': form,
    }

    return render(request, 'frontend/get-involved/visit-us.html', context)

def volunteers(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You application have sent successfully')
            return redirect('frontend:volunteers')
    else:
        form = VolunteerForm()

    logos = get_logos()
    
    context = {
        **logos,
        'form': form,
    }

    return render(request, 'frontend/get-involved/volunteers.html', context)

def campaigns(request):
    campaign_list = Campaign.objects.all().order_by('-created_at')
    paginator = Paginator(campaign_list, 6)

    page_number = request.GET.get('page')
    campaigns = paginator.get_page(page_number)
    logos = get_logos()

    
    context = {
        'campaigns': campaigns,
        **logos
    }

    return render(request, 'frontend/get-involved/campaign/index.html', context)

def viewCampaign(request, slug):
    campaign = get_object_or_404(Campaign, slug=slug)
    logos = get_logos()

    if request.method == 'POST':
        form = FundraisingForm(request.POST)
        if form.is_valid():
            fundraising = form.save(commit=False)
            fundraising.campaign = campaign
            fundraising.save()
            messages.success(request, 'Your fundraising request has been submitted successfully.')
            return redirect(f'/campaigns/{slug}?success=true')
    else:
        form = FundraisingForm()

    context = {
        'campaign': campaign,
        'form': form,
        **logos
    }

    return render(request, 'frontend/get-involved/campaign/show.html', context)

def termsAndConditions(request):
    logos = get_logos()
    policies = Policy.objects.filter(category='Terms & Conditions')
    
    context = {
        **logos,
        'policies': policies
    }

    return render(request, 'frontend/term-and-condition.html', context)

def privacyPolicy(request):
    policies = Policy.objects.filter(category='Privacy Policy')
    context = {'policies': policies}
    return render(request, 'frontend/privacy-policy.html', context)

def childProtectionPolicy(request):
    logos = get_logos()
    policies = Policy.objects.filter(category='Child Protection Policy')
    
    context = {
        **logos,
        'policies': policies
    }

    return render(request, 'frontend/child-protection-policy.html', context)

def resources(request):
    logos = get_logos()

    guidelines = Resource.objects.filter(category='guidelines')
    brochures = Resource.objects.filter(category='brochures')
    social_media = Resource.objects.filter(category='social_media')
    photos = Resource.objects.filter(category='photos')
    
    context = {
        **logos,
        'guidelines': guidelines,
        'brochures': brochures,
        'social_media': social_media,
        'photos': photos,
    }

    return render(request, 'frontend/resources.html', context)

def referenceSheet(request):
    logos = get_logos()
    referenceSheet = ReferenceSheet.objects.all().order_by('-created_at')
    
    context = {
        **logos,
        'referenceSheet': referenceSheet,
    }

    return render(request, 'frontend/reference-sheet.html', context)