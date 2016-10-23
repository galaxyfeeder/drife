from __future__ import unicode_literals

from django.db import models

from ums.models import Driver


class Group(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    license_plate = models.CharField(max_length=50)
    group = models.ForeignKey(Group)


class CarAccess(models.Model):
    car = models.ForeignKey(Car)
    driver = models.ForeignKey(Driver)
    start_time = models.DateField()
    end_time = models.DateField(blank=True, null=True)
