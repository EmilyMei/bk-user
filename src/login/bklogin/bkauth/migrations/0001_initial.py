# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-14 10:51
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            bases=(models.Model, django.contrib.auth.models.AnonymousUser),
        ),
    ]