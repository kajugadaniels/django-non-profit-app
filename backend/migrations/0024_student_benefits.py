# Generated by Django 5.0.4 on 2024-06-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_volunteer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='benefits',
            field=models.TextField(blank=True),
        ),
    ]
