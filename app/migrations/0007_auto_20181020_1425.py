# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181020_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='neighbourhood_id',
            new_name='neighbour',
        ),
    ]