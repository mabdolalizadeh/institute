# Generated by Django 5.0.4 on 2024-05-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
