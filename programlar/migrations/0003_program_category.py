# Generated by Django 4.1.3 on 2024-05-22 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programlar', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programlar.category'),
        ),
    ]
