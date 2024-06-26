from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    phone_verification_code = models.CharField(max_length=7, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)

    def check_password(self, password):
        hashed_password = hash(password)
        return hashed_password == self.password

    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'