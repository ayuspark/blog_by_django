# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import bcrypt
import json
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from .models import *
from .forms import *


# Create your views here.
def wall_index(request):
    return render(request, 'wall/wall_index.html', context=None)


def sign_in(request):
    # See if user already signed in
    try:
        if request.session['email']:
            messages.success(request, 'You are signed in as %s' % (request.session['email']))
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
                # check against bcrypted password
                hashed_psw = get_user.psw
                hashed_psw_bool = bcrypt.checkpw(psw.encode(), hashed_psw.encode())
                if hashed_psw_bool:
                    messages.success(request, 'Success! You are signed in as %s' % (get_user.email))
                    try:
                        request.session['email'] = email
                        request.session['user_id'] = get_user.id
                    except KeyError:
                        request.session['email'] = ''
                        request.session['user_id'] = 0
                        request.session['email'] = email
                        request.session['user_id'] = get_user.id
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
            # bcrypt password
            psw = form.cleaned_data.get('psw')
            hashed_psw = bcrypt.hashpw(psw.encode(), bcrypt.gensalt())
            new_user = form.save(commit=False)
            try:
                MyUser.objects.get(email=new_user.email)
                messages.error(request, 'Email exists, please sign in')
            except MyUser.DoesNotExist:
                new_user.psw = hashed_psw
                form.save()
                messages.success(request, 'Success!')
                register_state = True
    else:
        form = RegisterForm()
    return render(request, 'wall/register.html', {'form': form, 'register': register_state})


def check_email(request):
    email = request.GET.get('email', None)
    response = {
        'exists': MyUser.objects.filter(email=email).exists()
    }
    print response
    return JsonResponse(response)

def dashboard(request):
    is_admin = False
    all_users = MyUser.objects.all()
    return render(request, 'wall/dashboard.html', {'is_admin': is_admin, 'all_users': all_users})


def dashboard_admin(request):
    is_admin = True
    all_users = MyUser.objects.all()
    return render(request, 'wall/dashboard.html', {'is_admin': is_admin, 'all_users': all_users})


def user_show(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)
    posted_messages = Message.objects.order_by('-created_date').filter(posted_to_user_id=user_id)
    comments = Comment.objects.order_by('created_date').all()
    msg_form = MessageForm()
    comment_form = CommentForm()
    context = {
        'user': user,
        'posted_messages': posted_messages,
        'comments': comments,
        'msg_form': msg_form,
        'comment_form': comment_form,
    }
    return render(request, 'wall/user_wall.html', context) 



def user_delete(request, user_id):
    pass


def user_edit(request, user_id):
    pass


def message_post(request, user_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # save form info into ORM
            posted_by_user = MyUser.objects.get(id=request.session['user_id'])
            posted_to_user = MyUser.objects.get(id=user_id)
            new_msg = form.save(commit=False) 
            new_msg.posted_by_user = posted_by_user
            new_msg.posted_to_user = posted_to_user
            new_msg.created_date = timezone.now()
            new_msg.save() 
            msg_for_ajax = Message.objects.get(created_date=new_msg.created_date)
            context = {
                'message': msg_for_ajax,
                'user_id': request.session['user_id'],
                'comment_form': CommentForm(),
            }
            return render(request, 'wall/a_msg_section.html', context)


def comment(request, user_id, for_msg_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            posted_by_user = MyUser.objects.get(id=request.session['user_id'])
            parent_message = Message.objects.get(id=for_msg_id)
            new_comment = form.save(commit=False)
            new_comment.posted_by_user = posted_by_user
            new_comment.parent_message = parent_message
            new_comment.created_date = timezone.now()
            new_comment.save()
            comment_for_ajax = Comment.objects.get(created_date=new_comment.created_date)
            context = {
                'comment': comment_for_ajax,
                'user_id': request.session['user_id'],
            }
    print context
    return render(request, 'wall/a_comment_div.html', context)

