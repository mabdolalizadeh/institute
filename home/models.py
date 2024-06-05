from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"