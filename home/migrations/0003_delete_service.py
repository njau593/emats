# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_reachus_cont_email_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='service',
        ),
    ]