# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-16 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hospital_city',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
