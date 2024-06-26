from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('active/<phone_verification_code>', views.phone_verification_page, name='verify'),
]