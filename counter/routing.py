from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns= [
    path("counter/", WSConsumer.as_asgi())
]