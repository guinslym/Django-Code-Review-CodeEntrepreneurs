# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_auto_20170723_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='course',
        ),
    ]