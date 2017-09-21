from django import forms
from .models import *


class SignInForm(forms.Form):
    email = forms.EmailField()
    psw = forms.CharField(widget=forms.PasswordInput,
                          label='Password')


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = MyUser
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

