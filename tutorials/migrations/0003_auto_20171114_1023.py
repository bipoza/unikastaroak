# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 09:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
