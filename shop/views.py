from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'shop/index.html')


def shop(request):
    books = Book.objects.all()
    return render(request, 'shop/shop.html', {'books': books})
