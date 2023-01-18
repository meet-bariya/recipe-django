from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.items, name='items'),
    path('items/<int:item_id>', views.item_detail, name='item_detail'),
    path('add/', views.item_add, name='item_add'),
    path('delete/<int:item_id>', views.item_delete, name='item_delete'),
]
