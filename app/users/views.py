from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import User
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework import status, viewsets
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import string
import random
import string
from rest_framework.response import Response
class UserView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_type','price','name','descriptions']
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    # def create(self,request): 
    #     res = request.data
    #     serializers = UserSerializer(data=res)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     message = get_template('otp.html').render({"email":request.data.get('email')})
    #     msg = EmailMultiAlternatives('OTP', message,'naidtngcolo@gmail.com', [request.data.get('email')])
    #     html_content = f'<p>This is an<strong>important</strong> message.</p>'
    #     msg.content_subtype = "html"
    #     msg.send()
    #     return Response()
        


class Login(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            items = User.objects.filter(email=res.get('email'),password=res.get('password')).count()
            if(items>0):
               items = User.objects.filter(email=res.get('email'),password=res.get('password')) 
               items = UserSerializer(items,many=True)       
               return Response(status=status.HTTP_200_OK,data=items.data)
            else:
               return Response(status=status.HTTP_404_NOT_FOUND,data=items.data)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class VerifyUser(generics.GenericAPIView):
    def get(self,request,format=None,email=None):
        User.objects.filter(email=email).update(is_verified=True)
        return Response()



class ResetPassword(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        password = id_generator()
        User.objects.filter(email=res.get('email')).update(password=password)
        message = get_template('forgot_pass.html').render({"password":password})
        msg = EmailMultiAlternatives('OTP', message,'naidtngcolo@gmail.com', [request.data.get('email')])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))