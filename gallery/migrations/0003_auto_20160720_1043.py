# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160714_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
