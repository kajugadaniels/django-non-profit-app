# Generated by Django 5.0.4 on 2024-06-06 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_student_benefits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='spo_cover',
        ),
    ]
