from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category=<str:ctegory>', views.category, name='category'),
    path('item-id=<int:id>', views.item, name='item'),
]