# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directoryApp', '0006_auto_20180114_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countyname',
            name='County',
        ),
        migrations.AlterField(
            model_name='producer',
            name='county_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countiesApp.County'),
        ),
        migrations.DeleteModel(
            name='CountyName',
        ),
    ]