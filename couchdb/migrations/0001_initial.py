# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-04 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CouchCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('numofnodes', models.CharField(max_length=500)),
                ('ips', models.CharField(max_length=100)),
                ('names', models.CharField(default='', max_length=100)),
                ('haport', models.IntegerField(default=0)),
            ],
        ),
    ]
