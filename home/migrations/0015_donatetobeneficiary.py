# Generated by Django 5.0.4 on 2024-06-11 07:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0038_alter_team_category'),
        ('home', '0014_remove_donatetostudent_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateToBeneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationTitle', models.CharField(max_length=255)),
                ('donationId', models.TextField(max_length=255)),
                ('productId', models.TextField(max_length=255)),
                ('amount', models.FloatField()),
                ('status', models.CharField(default='Pending', max_length=40)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentMode', models.CharField(max_length=40)),
                ('donatedBy', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
        ),
    ]