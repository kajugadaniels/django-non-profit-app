# Generated by Django 5.0.4 on 2024-06-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_donatetostudents_paymentmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatetostudents',
            name='paymentMode',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='donatetostudents',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]