from django.shortcuts import render


def item(request, id):
    return render(request, 'store/item.html')


def catalog(request):
    return render(request, 'store/catalog.html')