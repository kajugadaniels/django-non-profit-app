from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class StripeWebhook(APIView):
    def post(self, request, format=None):
        data= request.data
        print("==>dt coming:",data)
        return Response("Success", status=status.HTTP_200_OK)
     
