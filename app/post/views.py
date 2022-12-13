from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
import pusher
from decouple import config
class PostView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Post.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=PostSerializer

    def list(self,request):
        items = Post.objects.all()
        items = PostSerializer(items,many=True)
        for x in items.data:
            u_items = User.objects.filter(id=x['user_id'])
            u_items = UserSerializer(u_items,many=True)
            x['name'] = u_items.data[0]['fullname']
            x['longitude'] = u_items.data[0]['longitude']
            x['latitude'] = u_items.data[0]['latitude']
        return Response(data = items.data)
