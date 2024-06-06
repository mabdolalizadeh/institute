from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.name


class SignupInHome(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    text = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}-{self.phone}-{self.is_checked}'