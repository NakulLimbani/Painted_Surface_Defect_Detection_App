from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from defect_detection_app.consumers import LiveDetectionConsumer
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
    path('ws://localhost:8000/ws/live_detection/', LiveDetectionConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
