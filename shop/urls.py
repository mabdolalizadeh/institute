from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<slug:slug>/', views.product_detail, name='product', )
]