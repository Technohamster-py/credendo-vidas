from django.shortcuts import render
import sys
from operator import attrgetter
from itertools import chain
from .models import News
sys.path.append('..')
from blog.models import Post


def index(request):
    resent_posts = Post.objects.order_by('-date')[:3]
    resent_articles = Post.objects.order_by('-date')[3:10]
    resent_news = News.objects.order_by('-date')[:10]

    event_list = sorted(
        list(chain(resent_articles, resent_news))[:10],
        key=attrgetter('date'),
        reverse=True
    )

    context = {
        "resent_posts": resent_posts,
        "resent_news" : event_list
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


def news_detail(request, id):
    news = News.objects.get(id=id)
    context = {
        'post': news
    }
    return render(request, 'blog/post.html', context)