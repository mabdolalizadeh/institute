from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book


def shop(request):
    books = Book.objects.all()
    return render(request, 'shop/shop.html', {'books': books})


def product_detail(request, slug):
    product = get_object_or_404(Book, slug=slug)
    return render(request, 'shop/product.html', {'product': product})
