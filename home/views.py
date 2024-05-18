from random import sample
from backend.models import *
from django.shortcuts import render,redirect
import stripe
from dotenv import load_dotenv
load_dotenv()
import os
from .forms import *
# Create your  views here.

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
publickey =  os.getenv("STRIPE_PUBLIC_KEY")
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
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():

            amoun = form.cleaned_data['amount']
            email =  form.cleaned_data['email']
            fullname=  form.cleaned_data['fullname']
            amount = int(float(amoun) * 100)
            interval =  form.cleaned_data['paymentOptions']
            if interval is not None :
                try:
                
                    
                    product = stripe.Product.create(
                            name="KYRO Training Center",
                            description="Your contribution towards the future Training Center for KYRO will enable us to make a more profound impact in the community we serve. We envision the Training Center as a dynamic hub for innovation, poised to continuously evolve and expand our positive community impact throughout Rwanda."
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
                            donation = ProjectDonation()
                            donation.donation= amount
                            donation.honoreefullname= honoreefullname
                            donation.email= email
                            donation.message= message
                            donation.recepientemail= recipientemail
                            donation.recepientfullname= receipientfullname
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
                        messages.error(request, "Please provide a donation amount.")
                        return redirect('donate')
                except stripe.error.CardError as e:
                    messages.error(request, e.message)
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
        else:
            form = DonationForm()
    return render(request, 'frontend/sponsor/index.html', context)
def donateRequest(request):
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