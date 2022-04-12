from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns= [
    path("ws/chat/<room_name>/", WSConsumer.as_asgi())
]