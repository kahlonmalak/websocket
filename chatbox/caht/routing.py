from django.urls import path
from .import consumer

websocket_urlpatterns = [
    path(r'^ws/notification/broadcast/', consumer.ChatConsumer.as_asgi()),
]