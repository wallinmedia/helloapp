# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0005_auto_20160503_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktiviteter',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
