from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.name


class SimpleSignup(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'simple registration\'s name'
        verbose_name_plural = 'simple registrations\' name'

    def __str__(self):
        return f'{self.name}-{self.phone}-{self.is_checked}'
