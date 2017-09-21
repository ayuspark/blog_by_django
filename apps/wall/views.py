# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here.
def wall_index(request):
    return render(request, 'wall/wall_index.html', context=None)


def sign_in(request):
    # See if user already signed in
    try:
        if request.session['email']:
            messages.success(request, 'Success! You are signed in as %s' % (request.session['email']))
    except KeyError:
        request.session['email'] = ''

    # validate SignInForm
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            psw = form.cleaned_data.get('psw')
            try:
                get_user = MyUser.objects.get(email=email)
                if psw == get_user.psw:
                    messages.success(request, 'Success! You are signed in as %s' % (get_user.email))
                    try:
                        request.session['email'] = email
                    except KeyError:
                        request.session['email'] = ''
                        request.session['email'] = email
                    if get_user.is_admin:
                        return redirect('wall:dashboard_admin')
                    else:
                        return redirect('wall:dashboard')
                else:
                    messages.error(request, 'Something is wrong.')
            except MyUser.DoesNotExist:
                messages.error(request, 'Email not found, please register first.')
    # load SignInForm
    else:
        form = SignInForm()
    return render(request, 'wall/sign_in.html', {'form': form})

    
def register(request):
    register_state = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            psw = form.cleaned_data.get('psw')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            try:
                MyUser.objects.get(email=email)
                messages.error(request, 'Email exists, please sign in')
            except MyUser.DoesNotExist:
                form.save()
                messages.success(request, 'Success!')
                register_state = True
    else:
        form = RegisterForm()
    return render(request, 'wall/register.html', {'form': form, 'register': register_state})


def dashboard(request):
    return render(request, 'wall/dashboard.html')


def dashboard_admin(request):
    pass