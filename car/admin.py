from django.contrib import admin

from car.models import Group, Car, CarAccess, DriverGroup

admin.site.register(Group)
admin.site.register(DriverGroup)
admin.site.register(Car)
admin.site.register(CarAccess)
