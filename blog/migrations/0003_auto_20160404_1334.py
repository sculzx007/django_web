# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 05:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_zonesubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zonesubject',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 5, 34, 7, 622709, tzinfo=utc)),
        ),
    ]