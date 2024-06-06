from django.shortcuts import render, redirect
from shop.models import Book
from .models import Course
from .forms import SimpleSignupModelForm


def home(request):
    courses = Course.objects.all()
    shop_elements = Book.objects.all().filter(category__title="Learning").order_by("-id")[:4]
    if request.method == "POST":
        form = SimpleSignupModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SimpleSignupModelForm()

    return render(request, 'home/home.html', {
        "shop_elements": shop_elements,
        "courses": courses,
        "form": form,
    })
