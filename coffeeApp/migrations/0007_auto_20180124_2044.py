# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-24 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApp', '0006_auto_20180123_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeetransactions',
            name='BAGMARK',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='coffeetransactions',
            name='REF2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
