from django import forms
from .models import *


class SignInForm(forms.Form):
    email = forms.EmailField()
    psw = forms.CharField(widget=forms.PasswordInput,
                          label='Password')


class RegisterForm(forms.ModelForm):
    psw = forms.CharField(widget=forms.PasswordInput)
    confirm_psw = forms.CharField(widget=forms.PasswordInput,
                                  label='Confirm Password',)

    class Meta:
        model = MyUser
        exclude = ['is_admin']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        psw = cleaned_data.get('psw')
        confirm_psw = cleaned_data.get('confirm_psw')

        if psw != confirm_psw:
            msg = 'Password does not match'
            return self.add_error('confirm_psw', msg)


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

