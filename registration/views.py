from django.shortcuts import render
from django.views.generic import CreateView, View
from .forms import RegistrationForm
from .models import Registration

#
# class RegistrationView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = RegistrationForm
#     success_url = '/'


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            check: bool = Registration.objects.filter(phone_number__iexact=phone).exists()
            if check:
                form.add_error('phone_number', 'شماره تکراریه، فکر کنم قبلا ثبت نام کردی...')
            else:
                form.save()

        context = {'form': form}
        return render(request, 'registration/register.html', context)