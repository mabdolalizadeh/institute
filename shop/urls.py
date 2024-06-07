from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
]
