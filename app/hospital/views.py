from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Hospital
from .serializers import HospitalSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
import pusher
from decouple import config
class HospitalView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    queryset=Hospital.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=HospitalSerializer


