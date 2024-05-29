from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *

age_list = []
category_list = []
level_list = []
type_list = []

for a in Age.objects.all():
    age_list.append(a.slug)

for c in Category.objects.all():
    category_list.append(c.slug)

for l in Level.objects.all():
    level_list.append(l.slug)

for t in Type.objects.all():
    type_list.append(t.slug)


def shop(request):
    active = Book.objects.get(title='Evolve-full pack')
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
        'some_book': some_book
    })


def product_page(request, slug):
    product = get_object_or_404(Book, slug=slug)
    same_products = Book.objects.filter(category__title=product.category.title)
    return render(request, 'shop/product.html', {
        'product': product,
        'same_products': same_products
    })


def category_detail(request, slug):
    if slug in category_list:
        category = get_object_or_404(Category, slug=slug)
        products = Book.objects.filter(category__title=category.title)
    elif slug in level_list:
        category = get_object_or_404(Level, slug=slug)
        products = Book.objects.filter(level__title=category.title)
    elif slug in type_list:
        category = get_object_or_404(Type, slug=slug)
        products = Book.objects.filter(type__type=category.type)
    elif slug in age_list:
        category = get_object_or_404(Age, slug=slug)
        products = Book.objects.filter(age__title=category.title)
    else:
        raise Http404

    return render(request, 'shop/category.html', {
        'category': category,
        'products': products
    })