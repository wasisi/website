# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-24 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApp', '0007_auto_20180124_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeetransactions',
            name='SEASON',
        ),
    ]
