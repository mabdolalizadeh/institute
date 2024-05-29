from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name="Slug", null=True, blank=True)

    def __str__(self):
        return self.tag


class Type(models.Model):
    type = models.CharField(max_length=200, verbose_name="Type")
    slug = models.SlugField(max_length=200, verbose_name="Slug", null=True, blank=True)

    def __str__(self):
        return self.type


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Category")
    slug = models.SlugField(max_length=100, verbose_name="Slug", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Categories"


class Age(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Age")
    slug = models.SlugField(max_length=100, verbose_name="Slug", null=True, blank=True)

    def __str__(self):
        return self.title


class Level(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Level")
    slug = models.SlugField(max_length=100, verbose_name="Slug", null=True, blank=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100, verbose_name="Book Title", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.ForeignKey(Age, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    type = models.ForeignKey(Type, verbose_name="Type", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name="Author", null=True, blank=True)
    image = models.CharField(max_length=200, verbose_name="Book Image", null=True, blank=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title}-{self.category}-{self.age}-{self.level}-{self.price}"
