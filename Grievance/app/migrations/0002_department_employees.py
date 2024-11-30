# Generated by Django 5.1.3 on 2024-11-30 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='assigned_department', to=settings.AUTH_USER_MODEL),
        ),
    ]
