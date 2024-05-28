from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book
import random


def shop(request):
    active = Book.objects.get(title='Evolve-full pack')
    vizheh = Book.objects.get(title='Evolve 1')
    some_book = [Book.objects.get(title='Teen2Teen-full pack'),
                 Book.objects.get(title='Family & Friends-full pack'),]
    books = Book.objects.all()
    learnings = Book.objects.filter(category__title="Learning")
    skills = Book.objects.filter(category__title='Skill')
    stories = Book.objects.filter(category__title='Story')

    return render(request, 'shop/shop.html', {
        'books': books,
        'learnings': learnings,
        'skills': skills,
        'stories': stories,
        'active': active,
        'vizheh': vizheh,
        'some_book': some_book
    })


def product(request, slug):
    product = get_object_or_404(Book, slug=slug)
    return render(request, 'shop/product.html', {'product': product})
