from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from registration.models import User
from .models import *


class ShopView(TemplateView):
    template_name = 'shop/shop.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active = Book.objects.get(title='Evolve-full pack')
        some_book = [Book.objects.get(title='Teen2Teen-full pack'),
                     Book.objects.get(title='Family & Friends-full pack'), ]
        books = Book.objects.all()
        learnings = Book.objects.filter(category__title="Learning")
        skills = Book.objects.filter(category__title='Skill')
        stories = Book.objects.filter(category__title='Story')
        context['books'] = books
        context['learnings'] = learnings
        context['skills'] = skills
        context['stories'] = stories
        context['active'] = active
        context['some_book'] = some_book

        return context


class ProductView(TemplateView):
    template_name = 'shop/product.html'

    def get_context_data(self, **kwargs):
        slug = kwargs['slug']
        product = get_object_or_404(Book, slug=slug)
        same_products = Book.objects.filter(category__title=product.category.title)
        context = super().get_context_data(**kwargs)
        context['product'] = product
        context['same_products'] = same_products

        return context


class CategoryView(TemplateView):
    template_name = 'shop/category.html'

    age_list = []
    for a in Age.objects.all():
        age_list.append(a.slug)

    category_list = []
    for c in Category.objects.all():
        category_list.append(c.slug)

    level_list = []
    for le in Level.objects.all():
        level_list.append(le.slug)

    type_list = []
    for t in Type.objects.all():
        type_list.append(t.slug)

    def get_context_data(self, **kwargs):
        slug = kwargs['slug']
        context = super().get_context_data(**kwargs)

        if slug in self.category_list:
            category = get_object_or_404(Category, slug=slug)
            products = Book.objects.filter(category__title=category.title)
        elif slug in self.level_list:
            category = get_object_or_404(Level, slug=slug)
            products = Book.objects.filter(level__title=category.title)
        elif slug in self.type_list:
            category = get_object_or_404(Type, slug=slug)
            products = Book.objects.filter(type__type=category.type)
        elif slug in self.age_list:
            category = get_object_or_404(Age, slug=slug)
            products = Book.objects.filter(age__title=category.title)
        else:
            raise Http404

        context['products'] = products
        context['category'] = category

        return context
