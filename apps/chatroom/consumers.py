import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import *


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    try:
        get_path = message['path'].strip('/').split('/')
        prefix = get_path[1]
        label = get_path[2]
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            return
        room = Chatroom.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Chatroom.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return
    
    log.debug('chat connect room=%s client=%s:%s',
              room.label, message['client'][0], message['client'][1])

    # accept incoming connection
    message.reply_channel.send({"accept": True})

    # add to the chatting group
    Group('chat-' + label).add(message.reply_channel)

    # persist the chatroom label
    message.channel_session['room_label'] = room.label
    
    
@channel_session
def ws_receive(message):
    # check if room in channel_session or room exist
    try:
        label = message.channel_session['room_label']
        room = Chatroom.objects.get(label=label)
    except KeyError:
        log.debug('room not in channel_session')
        return
    except Chatroom.DoesNotExist:
        log.debug('received chat/message, but room does not exist')
        return
    
    # parse data sent from client
    try:
        data = json.loads(message.content['text'])
    except ValueError:
        log.debug("ws_message(chat_from_client) isn't json, chat=%s",
                  message.content['text'])
        return

    if set(data.keys()) != set(('handle', 'chat')):
        log.debug("ws_message(chat_from_client) unexpected format, data=%s", data)
        return

    if data:
        log.debug('data(chat_from_client) from client: room=%s handle=%s chat=%s',
                  room.label, data['handle'], data['chat'])
        chat_to_client = room.chats.create(**data)

    Group('chat-' + label).send({'text': json.dumps(chat_to_client.as_dict())})


def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Chatroom.objects.get(label=label)
        Group('chat-' + label).discard(message.reply_channel)
    except(KeyError, Chatroom.DoesNotExist):
        pass
