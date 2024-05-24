from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ages = models.CharField(max_length=100, default="All")
    level = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title}-{self.category}-{self.ages}-{self.level}-{self.price}"
