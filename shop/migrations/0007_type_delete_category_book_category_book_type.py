# Generated by Django 5.0.4 on 2024-05-24 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Book Type')),
                ('url_title', models.CharField(max_length=100, verbose_name='URL Book Type')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='Learning', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.type'),
        ),
    ]
