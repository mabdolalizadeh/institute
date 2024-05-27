from django.contrib import admin
from . import models


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'price', 'level', 'is_active']
    list_filter = ['price', 'is_active']
    list_editable = ['is_active']


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Category)
admin.site.register(models.Level)
admin.site.register(models.Age)

