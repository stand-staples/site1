# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simp', '0002_patient_clean_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='clean_patient_name',
            field=models.CharField(max_length=200),
        ),
    ]
