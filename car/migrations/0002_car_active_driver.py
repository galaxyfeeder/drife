# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0001_initial'),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='active_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ums.Driver'),
        ),
    ]
