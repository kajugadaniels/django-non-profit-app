# Generated by Django 5.0.4 on 2024-05-18 12:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_useraccount_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationTitle', models.CharField(max_length=255)),
                ('donation', models.FloatField()),
                ('donationId', models.TextField(max_length=255)),
                ('productId', models.TextField(max_length=255)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentMode', models.TextField(max_length=255)),
                ('paidBy', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
        ),
    ]