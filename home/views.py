from django.shortcuts import render, redirect
from django.views import View
from shop.models import Book
from .models import Course
from .forms import SimpleSignupModelForm


class HomeView(View):
    courses = Course.objects.all()
    shop_elements = Book.objects.all().filter(category__title="Learning").order_by("-id")[:4]

    def get(self, request):
        form = SimpleSignupModelForm()
        return render(request, 'home/home.html', {
            "shop_elements": self.shop_elements,
            "courses": self.courses,
            "form": form,
        })

    def post(self, request):
        form = SimpleSignupModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'home/home.html', {
            "shop_elements": self.shop_elements,
            "courses": self.courses,
            "form": form,
        })


