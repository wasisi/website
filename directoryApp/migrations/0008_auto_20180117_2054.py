# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-17 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryApp', '0007_auto_20180114_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='ref',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='producer',
            name='ref',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
