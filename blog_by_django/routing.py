from channels.routing import route, route_class
from apps.chatroom.consumers import *

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_message),
    route('websocket.disconnect', ws_disconnect),
]
