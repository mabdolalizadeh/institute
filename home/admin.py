from django.contrib import admin
from .models import Course, SimpleSignup


class SimpleSignupAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'is_checked']
    list_editable = ['is_checked']


admin.site.register(SimpleSignup, SimpleSignupAdmin)
admin.site.register(Course)
