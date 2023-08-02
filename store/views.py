from django.shortcuts import render
from .models import Item, Operation


def item(request, id):
    item = Item.objects.get(id=id)
    history = Operation.objects.filter(item=item)
    return render(request, 'store/item.html', {'item': item, 'history': history})


def category(request, category):
    pass

def catalog(request):
    items = Item.objects.all()
    return render(request, 'store/catalog.html', {'items': items})