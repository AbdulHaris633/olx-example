from django.urls import path
from .views import basket_detail,add_to_basket,remove_from_basket,delete_from_basket

urlpatterns = [
    path('', basket_detail, name='basket_detail'),  # View to display the basket
    path('add/<uuid:product_id>/', add_to_basket, name='add_to_basket'), 
    path('remove/<uuid:product_id>/', remove_from_basket, name='remove_from_basket'),
    path('delete/<uuid:product_id>/', delete_from_basket, name='delete_from_basket')   
]      