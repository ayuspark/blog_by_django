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
            email = form.cleaned_data['email']
            psw = form.cleaned_data['psw']
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

    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', post_pk=post.pk)
    # else:
    #     form = PostForm()
    # return render(request, 'blog/post_edit.html', {'form': form})
