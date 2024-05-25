from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("WeBHOOK_Key")
publickey =  os.getenv("STRIPE_PUBLIC_KEY")
import stripe
# Create your views here.
class StripeWebhook(APIView):
    def post(self, request, format=None):
        event = None
        payload = request.data
        sig_header = request.headers['STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            raise e
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            raise e

        # Handle the event
        print('Unhandled event type {}'.format(event['type']))
        data= request.data
        print("==>dt coming:",data)
        return Response("Success", status=status.HTTP_200_OK)
     
