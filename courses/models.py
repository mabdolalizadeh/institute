from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], default=1)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/images/')
    def __str__(self):
        return f"{self.name} - {self.book}"