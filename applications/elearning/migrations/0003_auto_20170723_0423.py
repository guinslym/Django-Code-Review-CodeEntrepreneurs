# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 08:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.models_utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elearning', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', utils.models_utils.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', utils.models_utils.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'verbose_name_plural': 'Registrations',
                'verbose_name': 'Register',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=utils.models_utils.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified',
            field=utils.models_utils.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=utils.models_utils.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='course',
            name='modified',
            field=utils.models_utils.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=utils.models_utils.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='modified',
            field=utils.models_utils.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='register',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Course'),
        ),
        migrations.AddField(
            model_name='register',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
