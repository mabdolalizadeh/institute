from django.views.generic.edit import FormView
from shop.models import Book
from .models import Course
from .forms import SimpleSignupModelForm
from django.contrib import messages


# class HomeView(View):
#     courses = Course.objects.all()
#     shop_elements = Book.objects.all().filter(category__title="Learning").order_by("-id")[:4]
#
#     def get(self, request):
#         form = SimpleSignupModelForm()
#         return render(request, 'home/home.html', {
#             "shop_elements": self.shop_elements,
#             "courses": self.courses,
#             "form": form,
#         })
#
#     def post(self, request):
#         form = SimpleSignupModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#         return render(request, 'home/home.html', {
#             "shop_elements": self.shop_elements,
#             "courses": self.courses,
#             "form": form,
#         })

class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = SimpleSignupModelForm
    success_url = '/#home'
    courses = Course.objects.all()
    shop_elements = Book.objects.all().filter(category__title="Learning").order_by("-id")[:4]

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'success')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_elements'] = self.shop_elements
        context['courses'] = self.courses
        return context




