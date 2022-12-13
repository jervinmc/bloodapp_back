from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Donation
from .serializers import DonationSerializer
from rest_framework import filters
from rest_framework import status, viewsets
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from users.models import User
from users.serializers import UserSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import string
import random
import string
from rest_framework.response import Response
class DonationView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['hospital_name','location','blood_type']
    queryset=Donation.objects.all()
    serializer_class=DonationSerializer



class DoctorDonation(generics.GenericAPIView):
    def get(self,request):
        items = User.objects.filter(user_type='Institution')
        items = UserSerializer(items,many=True)
        return Response(status=status.HTTP_200_OK,data=items.data)




