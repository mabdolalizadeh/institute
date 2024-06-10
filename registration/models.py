from django.db import models
from django.core.validators import MinValueValidator


class Registration(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=100, blank=True)
    phone_verification_code = models.CharField(max_length=7, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'