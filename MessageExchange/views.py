from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import MessageSerializer
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient 
import requests
from decouple import config
# Create your views here.
@api_view(['GET','POST'])
def sendMessage(request):
    if request.method == "POST":
        #The next 4 lines are changeable
        api_id = config('api_id')
        api_hash = config('api_hash')
        token = config('token')
        chat_id = config('chat_id')
        phone = config('phone')
        # client = TelegramClient('session', api_id, api_hash)
        # client.connect()
        # if not client.is_user_authorized():
        #     client.send_code_request(phone)
        #     # signing in the client
        #     client.sign_in(phone, input('Enter the code: ')) 
        # try:
        #     # receiver user_id and access_hash, use
        #     # my user_id and access_hash for reference
        #     receiver = InputPeerUser('user_id', 'user_hash')
        #     if request.data != None:
        #         serialized_data = MessageSerializer(data=request.data)
        #         client.send_message(receiver,serialized_data.message,parse_mode='html')
                 
        # except Exception as e:
        #     print(e)
        # client.disconnect()
        
        print(request.data)
        message = request.data['message']
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(url)
        print(requests.get(url).json())
        return Response("The message was sent")
    else:
        return Response()
    
        
        
            
    