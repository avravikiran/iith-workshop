# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_order_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='work',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
