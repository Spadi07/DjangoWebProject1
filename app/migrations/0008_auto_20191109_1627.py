# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-09 13:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191019_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('item_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 11, 9, 16, 27, 9, 245984), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 16, 27, 9, 245984), verbose_name='Опубликована:'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='app.CartItem'),
        ),
    ]
