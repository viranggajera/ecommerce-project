# Generated by Django 5.0.1 on 2024-01-19 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('profile_pic', models.FileField(default='anonymous.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('search_country', models.CharField(max_length=200)),
                ('order_address_line1', models.TextField(max_length=200)),
                ('order_address_line2', models.TextField(max_length=200)),
                ('order_city', models.CharField(max_length=20)),
                ('order_zipcode', models.CharField(max_length=20)),
                ('order_phone', models.CharField(max_length=20)),
                ('order_email', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
            ],
        ),
    ]
