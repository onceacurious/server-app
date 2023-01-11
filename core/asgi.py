import django

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewereStack
from channels.security.websocket import AllowedHostsOriginValidator
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

import base.routing

application = ProtocolTypeRouter({
  'http':  get_asgi_application(),
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewereStack(
      URLRouter(
        base.routing.websocket_urlpatterns
      )
    )
  ),
})


