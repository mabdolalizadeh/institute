from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Category")
    url_title = models.CharField(max_length=100, verbose_name="URL Book Category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Age(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Age")
    url_title = models.CharField(max_length=100, verbose_name="URL Book Age")

    def __str__(self):
        return self.title


class Level(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Level")
    url_title = models.CharField(max_length=100, verbose_name="URL Book Level")

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title}-{self.category}-{self.age}-{self.level}-{self.price}"