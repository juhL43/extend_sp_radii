# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 00:30
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_radii', '0002_db_ions_cn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_ions',
            name='cn',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=''), size=20), size=20),
        ),
    ]