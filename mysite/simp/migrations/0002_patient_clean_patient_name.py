# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='clean_patient_name',
            field=models.CharField(default='none', max_length=200, unique=False),
            preserve_default=False,
        ),
    ]
