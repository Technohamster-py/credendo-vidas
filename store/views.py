from django.shortcuts import render
from .models import Item, Operation, Category


def item(request, id):
    item = Item.objects.get(id=id)
    history = Operation.objects.filter(item=item)
    return render(request, 'store/item.html', {'item': item, 'history': history})


def category(request, category):
    active_category = Category.objects.get(slug=category)
    items = Item.objects.filter(category=active_category)
    categories = Category.objects.all()
    return render(request, 'store/catalog.html', {'items': items, 'categories': categories})


def catalog(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'store/catalog.html', {'items': items, 'categories': categories})
