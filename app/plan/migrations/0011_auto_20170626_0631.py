# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_auto_20170620_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='Name',
            field=models.TextField(default='Sanjeev'),
        ),
        migrations.AddField(
            model_name='update',
            name='Standard',
            field=models.TextField(default='Grade 7th'),
        ),
    ]
