# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-30 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160830_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailedservice',
            name='service_Number',
            field=models.IntegerField(null=True),
        ),
    ]
