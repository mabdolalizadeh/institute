# Generated by Django 5.0.4 on 2024-06-15 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_user_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
