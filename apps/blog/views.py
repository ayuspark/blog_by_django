# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_pk):
    # Post.obejct.get(pk=<post_pk>)
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'blog/post_detail.html', {'post': post})