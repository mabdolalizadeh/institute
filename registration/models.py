from django.db import models
from django.core.validators import MinValueValidator



class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200, validators=[MinValueValidator(8)])
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Registrations\' list'

    def __str__(self):
        return f"{self.name} - {self.email}"