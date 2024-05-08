from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.category} - {self.level} - {self.price}"
