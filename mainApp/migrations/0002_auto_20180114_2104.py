# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={},
        ),
        migrations.RemoveField(
            model_name='about',
            name='body',
        ),
        migrations.AlterModelTable(
            name='about',
            table=None,
        ),
    ]
