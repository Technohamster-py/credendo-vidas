from django.shortcuts import render
from .models import Item


def item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'store/item.html', {'item': item})


def catalog(request):
    items = Item.objects.all()
    return render(request, 'store/catalog.html', {'items': items})