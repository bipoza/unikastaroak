# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20171114_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
