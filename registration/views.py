from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout


class SignUp(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form,
                   'login': False}
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            check = User.objects.filter(username=form.cleaned_data['phone_number']).exists()
            if check:
                form.add_error("phone_number", "شماره تکراریه؛ فکر کنم قبلا ثبت نام کردی...")
            else:
                user = User.objects.create_user(username=form.cleaned_data['phone_number'],
                                                password=form.cleaned_data['password'])
                profile = form.save(commit=False)
                profile.user = user
                profile.phone_verification_code = get_random_string(7)
                profile.save()
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
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=phone_number, password=password)
            if user:
                login(request, user)
                return redirect(reverse('home'))
            else:
                form.add_error('password', 'شماره یا رمزتون اشتباه :((')
                render(request, 'registration/register.html', {'form': form,
                                                               'login': True})

        return render(request, 'registration/register.html', {'form': form,
                                                              'login': True})


def phone_verification_page(request, phone_verification_code):
    user: Profile = Profile.objects.filter(phone_verification_code__iexact=phone_verification_code).first()
    if user is not None:
        if not user.is_verified:
            user.is_verified = True
            user.phone_verification_code = get_random_string(7)
            user.save()
            return redirect(reverse('login'))

    raise Http404
