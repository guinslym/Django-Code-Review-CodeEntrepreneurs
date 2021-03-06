# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 08:11
from __future__ import unicode_literals

import applications.elearning.models
import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_auto_20170731_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', slugify=applications.elearning.models.custom_slugify, unique_with=('created', 'author')),
        ),
    ]
