# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_delivery_serverlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='shell',
            field=models.CharField(blank=True, max_length=2048, verbose_name='shell'),
        ),
    ]
