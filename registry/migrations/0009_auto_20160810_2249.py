# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0008_auto_20160810_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='events/%Y/%m/%d/'),
        ),
    ]
