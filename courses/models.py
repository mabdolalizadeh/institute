from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ages = models.CharField(max_length=100, default="All")
    level = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title}-{self.category}-{self.ages}-{self.level}-{self.price}"
