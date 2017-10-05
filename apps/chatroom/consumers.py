from channels import Group
from channels.sessions import channel_session
from .models import *

@channel_session
def ws_connect(message, **kwargs):
    get_path = message['path'].strip('/').split('/')
    prefix = get_path[1]
    label = get_path[2]
    room = Chatroom.objects.get(label=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.label

def ws_message(message, **kwargs):
    pass

def ws_disconnect(message, **kwargs):
    pass
