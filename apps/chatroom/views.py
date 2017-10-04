# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import *


# Create your views here.
def chatroom(request, label):
    # create room if not exists, otherwise get room
    room, created = Chatroom.objects.get_or_create(label=label)
    # show the lastest 50 chats, order: most recent last
    chats = reversed(room.chats.order_by('-timestamp')[:50])
    context = {
        'room': room,
        'chats': chats,
    }
    return render(request, 'chatroom/chatroom.html', context)