# Generated by Django 4.1.3 on 2024-05-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programlar', '0003_program_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='category',
        ),
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
