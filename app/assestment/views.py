from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Assestment
from .serializers import AssestmentSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
import pusher
from decouple import config
class AssestmentView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Assestment.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=AssestmentSerializer
    
    # def list(self,request):
    #     items = Assestment.objects.filter(status='Pending',hostpi)
    #     items = AssestmentSerializer(items,many=True)
    #     for x in items.data:
    #         user = User.objects.filter(id = x['user_id'])
    #         user = UserSerializer(user,many=True)
    #         x['name'] = user.data[0]['fullname']
    #         x['gender'] = user.data[0]['gender']
    #         x['address'] = user.data[0]['permanent_address']
    #     return Response(data = items.data)






class AssessmentByHospital(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request,hospital_id = None,status='Pending'):
        items = Assestment.objects.filter(status=status,hospital_id=hospital_id)
        items = AssestmentSerializer(items,many=True)
        print(items.data)
        print("log")
        for x in items.data:
            user = User.objects.filter(id = x['user_id'])
            user = UserSerializer(user,many=True)
            x['name'] = user.data[0]['fullname']
            x['gender'] = user.data[0]['gender']
            x['address'] = user.data[0]['permanent_address']
        return Response(data = items.data)

class AssessmentVerification(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request,user_id = None):
        items = Assestment.objects.filter(user_id=user_id)
        items = AssestmentSerializer(items,many=True)
        return Response(status=status.HTTP_200_OK,data=items.data)
