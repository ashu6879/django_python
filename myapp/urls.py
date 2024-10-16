from django.urls import path
from .views import item_list, item_create, item_delete

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/new/', item_create, name='item_create'),
    path('item/<int:item_id>/delete/', item_delete, name='item_delete'),  # New delete path
]
