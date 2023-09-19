from django.shortcuts import render
from .models import Item, Operation, Category


def item(request, id):
    item = Item.objects.get(id=id)
    history = Operation.objects.filter(item=item)
    context = {'item': item,
               'history': history}
    return render(request, 'store/item.html', context)


def category(request, category):
    active_category = Category.objects.get(slug=category)
    items = Item.objects.filter(category=active_category)
    categories = Category.objects.all()
    context = {'items': items,
               'categories': categories,
               'active_category': active_category}
    return render(request, 'store/catalog.html', context)


def catalog(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {'items': items,
               'categories': categories}
    return render(request, 'store/catalog.html', context)
