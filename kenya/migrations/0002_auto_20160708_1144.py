# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kenyainfo',
            name='keImage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
