from django.contrib import admin
from .models import SimpleSignup, Course


class SimpleSignupAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'is_checked']
    list_editable = ['is_checked']


admin.site.register(SimpleSignup, SimpleSignupAdmin)
admin.site.register(Course)
