# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simp', '0006_remove_patient_clean_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_ok',
            field=models.BooleanField(default=False),
        ),
    ]