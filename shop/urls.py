from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<slug:slug>/', views.product_page, name='product'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
]
