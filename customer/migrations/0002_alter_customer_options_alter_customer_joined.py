# Generated by Django 5.0.7 on 2024-07-17 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id'], 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 15, 49, 45, 491925)),
        ),
    ]