# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-27 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0018_auto_20171127_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[(0, '--Aukeratu--'), ('Teknologia', 'Teknologia'), ('Albisteak', 'Albisteak'), ('Lanak', 'Lanak')], max_length=25, null=True),
        ),
    ]
