# Generated by Django 5.0.4 on 2024-06-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_donatetostudents_paymentmode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatetostudents',
            name='paymentMode',
            field=models.CharField(choices=[('One Time', 'One Time'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Annually', 'Annually')], max_length=40),
        ),
    ]
