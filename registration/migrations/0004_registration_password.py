# Generated by Django 5.0.4 on 2024-06-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_registration_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]