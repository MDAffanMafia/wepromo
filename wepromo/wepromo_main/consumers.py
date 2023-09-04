#from channels.consumer import SyncConsumer,AsyncConsumer
#from channels.exceptions import StopConsumer
import json
#from asgiref.sync import async_to_sync
from wepromo_main.models import  Comments,User,Post,Chat
from channels.generic.websocket import AsyncWebsocketConsumer
class MySyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("channel layer..",self.channel_layer)
        print("channel_name",self.channel_name)
        #adding channel to a group
        await self.channel_layer.group_add(
            'programmers',
            self.channel_name
        )
        await self.accept()
        
        
    async def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['msg']
        #user=text_data_json['user']
        #print('type of text..',type(text_data['msg']))
        print("that is recieve",text_data[1])
        
        await self.channel_layer.group_send(
            'programmers',
            {
            'type':'chatmessage',
            'message':message,
            }
        )
    async def chatmessage(self,event):
        print("hellokk")
        print(event['message'])
        message=event['message']
        await self.send(text_data=json.dumps({"message":message}))       
    async def disconnect(self,event):
        print("that is disconnect",event)        
        print("channel layer..",self.channel_layer)
        print("channel_name",self.channel_name)
        await self.channel_layer.group_discard('programmers',self.channel_name)