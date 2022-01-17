
from django.urls import path
from .views import product_details, store

urlpatterns = [
    
    path('',store,name='store'),
    path('<slug:category_slug>/',store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',product_details,name='product_details'),
]