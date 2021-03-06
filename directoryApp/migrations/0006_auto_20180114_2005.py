# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countiesApp', '0002_auto_20180114_2005'),
        ('directoryApp', '0005_remove_producer_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('County', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countiesApp.County')),
            ],
        ),
        migrations.AddField(
            model_name='producer',
            name='county_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='directoryApp.CountyName'),
            preserve_default=False,
        ),
    ]
