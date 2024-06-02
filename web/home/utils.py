import uuid
from django.shortcuts import redirect,render
import stripe
import requests
from .models import * 
def donateFund(request, amount,interval,slug, fullname,email,template,gift):
    print(amount)
    amoun = int(float(amount) * 100)
    if interval is not None :
            try:
                if slug is not None and slug:
                    student = Student.objects.get(slug=slug)
                    product = stripe.Product.create(
                        name="Donate to "+str(student.name)+"",
                        description="Your gift of $"+str(amount)+" to "+str(student.name)+" is a life-changing."
                    ) 
                else:
                    if gift is not None and gift:
                        product = stripe.Product.create(
                        name="AOF Foundation- Giving a gift",
                        description="Your gift of $"+str(amount)+" is life-changing as it makes it possible for ONE hungry child to eat, be able to go to school in a safe environment, receive medical care, and learn about the life-changing love of Jesus."
                        )   
                    else:

                        product = stripe.Product.create(
                            name="AOF Foundation",
                            description="Your gift of $"+str(amount)+" is life-changing as it makes it possible for ONE hungry child to eat, be able to go to school in a safe environment, receive medical care, and learn about the life-changing love of Jesus."
                        )
                productId = product.id
                if amoun:
                    # Process donation logic here, such as saving the donation amount to the database
                    price=""
                    if interval=='one':

                        price = stripe.Price.create(
                            product=productId,
                            unit_amount=amoun,
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
                        if slug is not None and slug:
                            donation = DonateToStudents()
                            donation.amount= amoun
                            donation.email= email
                            donation.paidBy = fullname
                            donation.paymentMode = interval
                            donation.donationId = payment.id
                            donation.productId= productId,
                            donation.beneficiary= student
                            donation.save()
                        else: 
                            if gift is None:
                                donation = Donate()
                                donation.amount= amoun
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
                        unit_amount=amoun,
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
                   return render(request, template, { 
                    'error_message':'Amount should not be empty'
                })
            except stripe.error.CardError as e:
                return redirect('donate')

            except stripe.error.StripeError as e:
                error_message = str(e)
                return render(request, template, { 
                    'error_message': error_message
                })
                
            except Exception as e:
                print(e)
                error_message = 'An error occurred while processing your payment.'
               
                return render(request, template, { 
                    'error_message': error_message
                })
    else:
            
            return render(request,template, { 
                    'error_message': 'Please select donation type '
                })

