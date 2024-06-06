# Generated by Django 5.0.4 on 2024-06-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_remove_student_spo_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('guidelines', 'Guidelines'), ('brochures', 'Brochures'), ('social_media', 'Social Media'), ('photos', 'Photos')], max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='resources/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]