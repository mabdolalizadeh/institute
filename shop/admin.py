from django.contrib import admin
from . import models


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'image', 'category', 'type', 'price', 'level', 'is_active']
    list_filter = ['price', 'is_active']
    list_editable = ['is_active', 'image']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_title': ['title']}


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Level)
admin.site.register(models.Age)
admin.site.register(models.Type)
