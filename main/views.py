from django.shortcuts import render
import sys
from .models import News
sys.path.append('..')
from blog.models import Post


def index(request):
    resent_posts = Post.objects.order_by('-date')[:3]
    resent_news = News.objects.order_by('-date')[:10]
    context = {
        "resent_posts": resent_posts,
        "resent_news" : resent_news
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def schedule(request):
    return render(request, 'main/schedule.html')

def archive(request):
    pass
