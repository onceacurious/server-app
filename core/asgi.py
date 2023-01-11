import django

from channels.routing import ProtocolTypeRouter, URLRuter
from channels.auth import AuthMiddlewereStack
from channels.security.websocket import AllowedHostsOriginValidator
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

import base.routing

application = ProtocolTypeRouter({
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewereStack(
      URLRuter(
        base.routing.websocket_urlpatterns
      )
    )
  ),
  'http':  get_asgi_application()
})


