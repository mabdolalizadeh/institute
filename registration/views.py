from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth import login, logout


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
                user_password: str = form.cleaned_data.get('password')
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
            user: User = User.objects.filter(phone_number__iexact=phone_number).first()
            if user is None:
                form.add_error('phone_number', 'شماره تلفن ثبت نام نشده :((')
            elif not user.is_verified:
                form.add_error('phone_number', 'کاربر تایید نشده :((')
            else:
                password = form.cleaned_data.get('password')
                check: bool = user.password == password
                if not check:
                    form.add_error("password", "رمز اشتباهه")
                else:
                    login(request, user)
                    return redirect(reverse('home'))

        return render(request, 'registration/register.html', {'form': form,
                                                              'login': True})


def phone_verification_page(request, phone_verification_code):
    user: User = User.objects.filter(phone_verification_code__iexact=phone_verification_code).first()
    if user is not None:
        if not user.is_verified:
            user.is_verified = True
            user.phone_verification_code = get_random_string(7)
            user.save()
            return redirect(reverse('login'))

    raise Http404
