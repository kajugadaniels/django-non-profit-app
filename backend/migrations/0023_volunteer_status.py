# Generated by Django 5.0.4 on 2024-06-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]