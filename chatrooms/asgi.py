import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
import rooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatrooms.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(rooms.routing.websocket_urlpatterns))
})
