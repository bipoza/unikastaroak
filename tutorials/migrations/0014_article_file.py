# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-21 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0013_auto_20171116_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]