# Generated by Django 5.0.4 on 2024-05-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(max_length=100, null=True),
        ),
    ]