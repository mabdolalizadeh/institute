from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from .models import User


class SignUp(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form,
                   'login': False}
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            check: bool = User.objects.filter(phone_number=form.cleaned_data['phone_number']).exists()
            if check:
                form.add_error("phone_number", "شماره تکراریه؛ فکر کنم قبلا ثبت نام کردی...")
            else:
                print(form.cleaned_data['phone_number'])
                user = form.save(commit=False)
                user.phone_verification_code = get_random_string(7)
                user.save()
                return redirect(reverse('login'))

        return render(request, 'registration/register.html', {'form': form,
                                                              'login': False})


class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form,
                   'login': True}
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            check: bool = User.objects.filter(phone_number__iexact=phone_number,
                                              password__iexact=password).exists()
            if not check:
                form.add_error("password", "رمز اشتباهه")
            else:
                return redirect(reverse('home'))

        return render(request, 'registration/register.html', {'form': form,
                                                              'login': True})
