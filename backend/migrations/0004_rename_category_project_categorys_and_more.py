# Generated by Django 5.0.4 on 2024-06-12 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_project_category_project_target'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='categorys',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='target',
            new_name='targets',
        ),
    ]
