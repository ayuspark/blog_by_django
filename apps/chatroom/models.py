# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Chatroom(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.label
    

class Chat(models.Model):
    chatroom = models.ForeignKey(Chatroom, related_name='chats')
    handle = models.TextField()
    chat = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {chat}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-H:%M')

    def as_dict(self):
        return {'handle': self.handle, 'chat': self.chat, 'timestamp': self.formatted_timestamp}
