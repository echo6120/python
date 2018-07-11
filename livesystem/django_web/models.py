# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Bug(models.Model):
    testtime = models.DateTimeField(blank=True, null=True)
    testername = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    devicename = models.CharField(max_length=100)
    bug = models.CharField(max_length=1000)
    isbug = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bug'


class Device(models.Model):
    devicename = models.CharField(max_length=100)
    system = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'device'



class Notify(models.Model):
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    appversion = models.CharField(max_length=1000)
    downloadurl = models.CharField(max_length=1000)
    others = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'notify'


class Tester(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    class Meta:
        managed = True
        db_table = 'tester'
