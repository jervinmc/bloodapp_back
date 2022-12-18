from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Channel
from .serializers import ChannelSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
from chat.models import Chat
from chat.serializers import ChatSerializer
import pusher
from decouple import config
pusher_client = pusher.Pusher(
  app_id=config('pusher_id'),
  key=config('pusher_key'),
  secret=config('secret_key'),
  cluster='ap1',
  ssl=True
)
class ChannelView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    def create(self,request):
        res = request.data
        items = Channel.objects.filter(hospital_id = res.get('hospital_id'), finder_id = res.get('finder_id')).count()
        items1 = Channel.objects.filter(finder_id = res.get('hospital_id'), hospital_id = res.get('finder_id')).count()
        if(items==0 and items1==0):
            print(res)
            serializer = ChannelSerializer(data=res)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=res.get('channel'))
        else:
            item = Channel.objects.filter(hospital_id = res.get('hospital_id'), finder_id = res.get('finder_id')).count()
            # serializer = ChannelSerializer(item,many=True)
            if(item==0):
                item = Channel.objects.filter(finder_id = res.get('hospital_id'), hospital_id = res.get('finder_id'))
                serializer = ChannelSerializer(item,many=True)
                return Response(data=serializer.data[0]['channel'])
            else:
                item = Channel.objects.filter(finder_id = res.get('hospital_id'), hospital_id = res.get('finder_id'))
                serializer = ChannelSerializer(item,many=True)
                return Response(data=serializer.data[0]['channel'])

    # def list(self,request,format=None,email=None):
    #     try:
    #         if self.request.user.account_type=='Seller':
    #             items = Channel.objects.filter(seller_id=self.request.user.id)
    #             items = ChannelSerializer(items,many=True)
    #             for x in items.data:
    #                 user = User.objects.filter(id=x['customer_id'])
    #                 user = GetUserSerializer(user,many=True)
    #                 x['users']=user.data[0]
    #         elif self.request.user.account_type=='Customer':
    #             items = Channel.objects.filter(customer_id=self.request.user.id)
    #             items = ChannelSerializer(items,many=True)
    #             for x in items.data:
    #                 user = User.objects.filter(id=x['seller_id'])
    #                 user = GetUserSerializer(user,many=True)
    #                 x['users']=user.data[0]
    #         return Response(status=status.HTTP_200_OK,data=items.data)
    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class ChannelSend(generics.GenericAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        print(request.data)
        res = request.data
        pusher_client.trigger(request.data.get('channel'), 'my-test', {'message': request.data.get('message')})
        c_item = Chat.objects.filter(channel=request.data.get('channel'))
        c_item = ChatSerializer(c_item,many=True)
        for x in c_item.data:
            print(res.get('chat_user_id'))
            print(x['chat_user_id'])
            print(str(res.get('chat_user_id'))!=str(x['chat_user_id']))
            if(str(res.get('chat_user_id'))!=str(x['chat_user_id'])):
                print("okayyyy")
                print(x)
                pusher_client.trigger(x['chat_user_id'], 'my-test', {'message': request.data.get('message')})
                break
        try:
            serializer = ChatSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            print(e)
        return Response(data={})


class ChannelList(generics.GenericAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        res = request.data
        print(res)
        chatList = []
        typeAccount = ''
        objects = Channel.objects.filter(finder_id = res.get('id'))
        serializer = ChannelSerializer(objects,many=True)
        print(serializer.data)
        for x in serializer.data:
            item = User.objects.filter(id = x['hospital_id'])
            item = UserSerializer(item,many=True)
            if len(item.data)!=0:
                x['user_details'] = item.data[0]
            else:
                x['user_details'] = {"fullname":"No Name"}
            chatList.append(x)
        
        #2nd get
        objects = Channel.objects.filter(hospital_id = res.get('id'))
        serializer = ChannelSerializer(objects,many=True)
        print(serializer.data)
        for x in serializer.data:
            item = User.objects.filter(id = x['finder_id'])
            item = UserSerializer(item,many=True)
            if len(item.data)!=0:
                x['user_details'] = item.data[0]
            else:
                x['user_details'] = {"fullname":"No Name"}
            chatList.append(x)

        return Response(data=chatList)