from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Driver(models.Model):
    user = models.OneToOneField(User)
    driver_id = models.CharField(max_length=30)


class DriverIdentification(models.Model):
    driver = models.ForeignKey(Driver)

    class Meta:
        abstract = True


class NFCIdentification(DriverIdentification):
    card_id = models.CharField(max_length=100)


class BLEIdentificaiton(DriverIdentification):
    minor = models.IntegerField()
    major = models.IntegerField()
