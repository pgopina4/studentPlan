# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0017_auto_20170630_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='update1',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
