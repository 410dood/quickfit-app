# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickfitapp', '0008_auto_20170808_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='athlete_id',
            new_name='athlete',
        ),
    ]