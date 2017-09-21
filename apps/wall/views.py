# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here.
def wall_index(request):
    return render(request, 'wall/wall_index.html', context=None)


def sign_in(request):
    if request.method == 'POST':
        form = 
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
