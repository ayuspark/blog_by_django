# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import *


# Create your views here.
def new_room(request):
    # create a new chatroom if not exists
    new_room = None
    while not new_room:
        with transaction.atomic():
            # generate random chatroom names
            label = haikunator.Haikunator.haikunate()
            if Chatroom.objects.filter(label=label).exists():
                continue
            new_room = Chatroom.objects.create(label=label)
    return redirect('chatroom:chatroom', label=label)


def chatroom(request, label):
    # create room if not exists, otherwise get room
    room, created = Chatroom.objects.get_or_create(label=label)
    # show the lastest 10 chats, order: most recent last
    chats = reversed(room.chats.order_by('-timestamp')[:10])
    context = {
        'room': room,
        'chats': chats,
    }
    return render(request, 'chatroom/chatroom.html', context)
