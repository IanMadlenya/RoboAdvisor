# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_merge_20161020_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='mapping',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='recommendedAsset',
        ),
        migrations.DeleteModel(
            name='Recommendation',
        ),
    ]