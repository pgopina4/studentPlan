# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0021_auto_20170706_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='What_did_I_learn_new',
            field=models.TextField(default='Not much'),
        ),
    ]
