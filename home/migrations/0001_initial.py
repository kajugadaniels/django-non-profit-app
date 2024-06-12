# Generated by Django 5.0.4 on 2024-06-12 00:17

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationTitle', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('donationId', models.TextField(max_length=255)),
                ('productId', models.TextField(max_length=255)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentMode', models.TextField(max_length=255)),
                ('donatedby', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonateGifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('streetAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('streetAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('zip', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('productid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDonationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaryName', models.CharField(max_length=255)),
                ('beneficiaryId', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donatedBy', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('paymentMode', models.CharField(max_length=100)),
                ('paymentId', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=255, verbose_name='First name')),
                ('lastname', models.CharField(max_length=255, verbose_name='Last name')),
                ('phonenumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='phonenumber')),
                ('user_type', models.CharField(blank=True, choices=[('user', 'users'), ('admin', 'admin')], max_length=255, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.project')),
            ],
        ),
    ]
