from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book


def shop(request):
    books = Book.objects.all()
    return render(request, 'shop/shop.html', {
        'books': books,
        'counter': 0
    })