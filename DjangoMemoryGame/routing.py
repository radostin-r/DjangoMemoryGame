from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url

from DjangoMemoryGame.consumers import GameConsumer
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        URLRouter(
            [
                url('', GameConsumer)
            ]
        )
    )
})