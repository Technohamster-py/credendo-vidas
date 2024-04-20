from django.shortcuts import render
from .models import Post


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)