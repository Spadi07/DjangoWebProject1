# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-09 13:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191109_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='app.CartItem'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 11, 9, 16, 56, 9, 858697), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 16, 56, 9, 858697), verbose_name='Опубликована:'),
        ),
    ]