# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 02:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_radii', '0005_auto_20171208_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_ions',
            name='r_ir',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=20), default=None, size=20),
            preserve_default=False,
        ),
    ]
