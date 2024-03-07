import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Mascota
class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.room_group_name = 'test'
    print(self.scope)
    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )
    self.accept()
  
  async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    nombre = text_data_json['nombre']
    mascota_tipo = text_data_json['mascota_tipo']
    raza = text_data_json['raza']
    mascota = Mascota(nombre = nombre,mascota_tipo = mascota_tipo, raza = raza )
    mascota.save()
    
    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type':'chat_message',
        'nombre':nombre,
        'mascota_tipo': mascota_tipo,
        'raza': raza
      }
    )

  async def chat_message(self, event):
    nombre = event['nombre']
    mascota_tipo = event['mascota_tipo']
    raza = event['raza']
    query = Mascota.objects.all()
    data = {
      'nombre':nombre,
      'mascota_tipo':mascota_tipo,
      'raza':raza,
      'data': []
    }
    for i in query:
      data['data'].append(
      {'id': i.id,
       'nombre': i.nombre,
       'mascota_tipo': mascota_tipo,
       'raza': raza
      })
    print(data)
    self.send(text_data = json.dumps(data))
    
    