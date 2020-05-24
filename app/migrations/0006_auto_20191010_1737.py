# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-10 14:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191010_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 10, 10, 17, 37, 14, 453534), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 10, 17, 37, 14, 452534), verbose_name='Опубликована:'),
        ),
    ]