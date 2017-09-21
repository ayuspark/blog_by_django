from django import forms
from .models import *


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        exclude = ['is_admin']


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('msg',)
        # manually fill in other fields upon form submit


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        # manually fill in other fields upon form submit
