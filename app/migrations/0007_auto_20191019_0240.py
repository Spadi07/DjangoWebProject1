# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-18 23:40
from __future__ import unicode_literals

import app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191010_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 10, 19, 2, 40, 55, 90173), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 2, 40, 55, 89170), verbose_name='Опубликована:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=app.models.image_folder),
        ),
    ]
