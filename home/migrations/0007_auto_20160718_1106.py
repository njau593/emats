# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160714_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='home/photos'),
        ),
    ]