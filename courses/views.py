from django.shortcuts import render


def index(request):
    return render(request, 'courses/index.html')


def about(request):
    return render(request, 'courses/about.html')


def contact(request):
    return render(request, 'courses/contact.html')
