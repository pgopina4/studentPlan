# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-10 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0023_auto_20170726_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Standard', models.TextField(default='7th')),
                ('Name', models.TextField(default='Sanjeev')),
                ('Outcomes', models.TextField(default='chosen Goals')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Assessment_Marks', models.TextField(default='1')),
            ],
        ),
    ]
