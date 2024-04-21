from django.shortcuts import render
from operator import attrgetter
from itertools import chain
from .models import Post
import sys
sys.path.append('..')
from main.models import News


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def blog(request):
    posts = Post.objects.order_by('-date')
    news = News.objects.order_by('-date')

    events =sorted(
        list(chain(posts, news)),
        key=attrgetter('date'),
        reverse=True
    )

    context = {
        'posts': events
    }
    return render(request, 'blog/blog.html', context)