# Generated by Django 5.0.4 on 2024-05-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
