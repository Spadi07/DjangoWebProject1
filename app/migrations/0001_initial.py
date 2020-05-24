# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-08 17:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date_posted', models.DateTimeField(db_index=True, default=datetime.datetime(2019, 10, 8, 20, 48, 18, 754598), verbose_name='Дата комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии к статьям блога',
                'db_table': 'Comments',
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120, verbose_name='Заголовок:')),
                ('description', models.TextField(verbose_name='Краткое содержание:')),
                ('content', models.TextField(verbose_name='Полное содержание:')),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2019, 10, 8, 20, 48, 18, 754098), verbose_name='Опубликована:')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке:')),
            ],
            options={
                'verbose_name': 'Cтатья блога',
                'verbose_name_plural': 'Cтатьи блога',
                'db_table': 'Posts',
                'ordering': ['-date_posted'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post', verbose_name='Статья'),
        ),
    ]