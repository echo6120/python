# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testtime', models.DateTimeField(blank=True, null=True)),
                ('testername', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
                ('devicename', models.CharField(max_length=100)),
                ('bug', models.CharField(max_length=1000)),
                ('isbug', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bug',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateField(blank=True, null=True)),
                ('endtime', models.DateField(blank=True, null=True)),
                ('appversion', models.CharField(max_length=1000)),
                ('downloadurl', models.CharField(max_length=1000)),
                ('others', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'notify',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tester',
                'managed': True,
            },
        ),
    ]
