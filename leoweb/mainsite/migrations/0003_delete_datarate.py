# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-31 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_stream'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Datarate',
        ),
    ]