# Generated by Django 5.0.4 on 2024-06-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_donatetostudent_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatetostudent',
            name='created_at',
        ),
    ]
