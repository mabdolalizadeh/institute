from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/', views.product_detail, name='product', )
]