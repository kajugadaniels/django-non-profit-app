from django.http import JsonResponse
import uuid
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

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
publickey =  os.getenv("STRIPE_PUBLIC_KEY")

def index(request):
    students = Student.objects.all()
    blog = Blog.objects.all()
    
    context = {
        'students': students,
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
    # testimonial = Testimonial.objects.all()
    
    context = {
        # 'testimonial': testimonial
    }
    
    return render(request, 'frontend/what-we-do/gospel-teaching.html', context)

def students(request):
    student_list = Student.objects.all()
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
    
    return render(request, 'frontend/students/show.html', context)

def give(request):
    projects = Project.objects.all()[:6]

    context = {
        'projects': projects
    }

    return render(request, 'frontend/give.html', context)

def donate(request):
    students = Student.objects.all()
    projects = Project.objects.all()
    
    context = {
        'students': students,
        'projects': projects
    }
    if request.method == 'POST':
        # TODO: sanitize data
        amoun = request.POST['amount']
        email =  request.POST['email']
        fullname= request.POST['fullname']
        amount = int(float(amoun) * 100)
        interval =  request.POST['paymentOptions']
        if interval is not None :
            try:
                product = stripe.Product.create(
                        name="AOF Foundation",
                        description="Your gift of $"+str(amount)+" is life-changing as it makes it possible for ONE hungry child to eat, be able to go to school in a safe environment, receive medical care, and learn about the life-changing love of Jesus."
                    )
                productId = product.id
                if amount:
                    # Process donation logic here, such as saving the donation amount to the database
                    price=""
                    if interval=='one':

                        price = stripe.Price.create(
                            product=productId,
                            unit_amount=amount,
                            currency='usd',
                        )
                        payment=stripe.PaymentLink.create(
                        line_items=[{"price": price, "quantity": 1}],
                        currency="USD",
                        customer_creation="always",
                        allow_promotion_codes=False,
                        submit_type='donate',
                        billing_address_collection="auto",
                        metadata={"order_id": str(uuid.uuid4())},
                        )
                        donation = Donate()
                        donation.amount= amount
                        donation.email= email
                        donation.paidBy = fullname
                        donation.paymentMode = interval
                        donation.donationId = payment.id
                        donation.productId= productId
                        donation.save()
                        
                        return redirect(payment.url)
                    else:
                        price=stripe.Price.create(
                        product=productId,
                        unit_amount=amount,
                        currency='usd',
                        recurring={
                            'interval': interval,
                        },
                        )
                        payment=stripe.PaymentLink.create(
                        line_items=[{"price": price, "quantity": 1}],
                        currency="USD",
                        allow_promotion_codes=False,
                        billing_address_collection="auto",
                        metadata={"order_id": str(uuid.uuid4())},
                        )
                        
                        
                        return redirect(payment.url)
                    
                else:
                   return render(request, 'frontend/sponsor/index.html', { 
                    'error_message':'Amount should not be empty'
                })
            except stripe.error.CardError as e:
                return redirect('donate')

            except stripe.error.StripeError as e:
                error_message = str(e)
                return render(request, 'frontend/sponsor/index.html', { 
                    'error_message': error_message
                })
                
            except Exception as e:
                error_message = 'An error occurred while processing your payment.'
                print(e)
                return render(request, 'frontend/sponsor/index.html', { 
                    'error_message': error_message
                })
            

        else:
            return render(request, 'frontend/sponsor/index.html', { 
                    'error_message': 'Please select donation type '
                })
   


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

def projects(request):
    projects= Project.objects.all()

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
    total_amount = sum(float(item['amount']) for item in cart)
    return {
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    }

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