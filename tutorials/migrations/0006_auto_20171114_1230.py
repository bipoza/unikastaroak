# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_article_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='files',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
