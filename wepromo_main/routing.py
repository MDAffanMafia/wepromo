from . import consumers
from django.urls import path , include
print("happened")
websocket_urlpatterns = [
	path('' , consumers.MySyncConsumer.as_asgi()),
]

