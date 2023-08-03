from django.shortcuts import render
from .models import Item, Operation, Category


def item(request, id):
    item = Item.objects.get(id=id)
    history = Operation.objects.filter(item=item)
    return render(request, 'store/item.html', {'item': item, 'history': history})


def category(request, category):
    items = Item.objects.filter(category=category)
    categories = Category.objects.all()



def catalog(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'store/catalog.html', {'items': items, 'categories': categories})
