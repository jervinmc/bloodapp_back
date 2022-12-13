from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Request
from .serializers import RequestSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.serializers import UserSerializer
from users.models import User
import pusher
from decouple import config
class RequestView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Request.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=RequestSerializer




class GetDetails(generics.GenericAPIView):
    def get(self,request,hospital_id=None):
        res = request.data
        items = Request.objects.filter(hospital_id=hospital_id)
        items = RequestSerializer(items,many=True)
        for x in items.data:
            u_item = User.objects.filter(id=x['user_id'])
            u_item = UserSerializer(u_item,many=True)
            x['fullname'] = u_item.data[0]['fullname']
        return Response(data=items.data)

