# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultPageMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.CharField(blank=True, help_text='Unique coma-separated keywords for this page/item', max_length=160, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='Short and unique description for this page/item', max_length=160, null=True)),
            ],
            options={
                'verbose_name': 'Default Page Meta Data',
            },
        ),
        migrations.CreateModel(
            name='PageMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.CharField(blank=True, help_text='Unique coma-separated keywords for this page/item', max_length=160, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='Short and unique description for this page/item', max_length=160, null=True)),
                ('url', models.CharField(help_text='Relative url E.g /home/ or /projects/', max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Page Meta Data',
                'verbose_name_plural': 'Page Meta Data',
            },
        ),
    ]