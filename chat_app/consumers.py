import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()
    
    self.send(text_data = json.dumps({
      'type': 'Conexion establecida',
      'message': 'Tu estas conectado ahora!'
    }))