# Generated by Django 5.0.1 on 2024-01-19 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_buyer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
