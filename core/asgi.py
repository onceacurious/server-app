import django

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

import base.routing

application = ProtocolTypeRouter({
  'http':  get_asgi_application(),
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
      URLRouter(
        base.routing.websocket_urlpatterns
      )
    )
  ),
})


