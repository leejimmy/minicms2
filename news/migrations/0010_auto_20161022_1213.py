# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20161022_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name='\u5bfc\u822a\u663e\u793a'),
        ),
    ]