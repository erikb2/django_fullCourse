# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
