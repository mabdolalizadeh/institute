from django.shortcuts import render
from shop.models import Book
from .models import Course


def home(request):
    courses = Course.objects.all()
    shop_elements = Book.objects.all().filter(category__title="Learning").order_by("-id")[:4]
    return render(request, "home/home.html", {
        "shop_elements": shop_elements,
        "courses": courses,
    })


def contact_us(request):
    return render(request, 'home/contact_us.html')