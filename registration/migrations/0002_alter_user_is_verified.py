# Generated by Django 5.0.4 on 2024-06-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]