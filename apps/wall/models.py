# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class MyUser(models.Model):
    # User model
    email = models.EmailField(max_length=254)
    fname = models.CharField(max_length=20, verbose_name='first name')
    lname = models.CharField(max_length=20, verbose_name='last name')
    psw = models.CharField(max_length=20, verbose_name='password')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Message(models.Model):
    # Message model
    msg = models.TextField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    posted_by_user = models.ForeignKey(MyUser, related_name='messages_posted_by')
    posted_to_user = models.ForeignKey(MyUser, related_name='messages_posted_to')
    
    def __str__(self):
        return self.msg

    def update(self):
        self.updated_date = timezone.now
        self.save()
        

class Comment(models.Model):
    # Comment model
    comment = models.TextField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)
    posted_by_user = models.ForeignKey(MyUser, related_name='comments_posted')
    parent_message = models.ForeignKey(Message, related_name='children_comments')

    def __str__(self):
        return self.comment
