# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20170617_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='date',
        ),
        migrations.RemoveField(
            model_name='update',
            name='date',
        ),
        migrations.AlterField(
            model_name='post1',
            name='Goal_old1',
            field=models.TextField(default='goal1'),
        ),
        migrations.AlterField(
            model_name='post1',
            name='Goal_old2',
            field=models.TextField(default='goal2'),
        ),
    ]
