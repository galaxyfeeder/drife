from django.contrib import admin

from car.models import Group, Car, CarAccess, DriverGroup, CarUsage

admin.site.register(Group)
admin.site.register(DriverGroup)
admin.site.register(Car)
admin.site.register(CarAccess)
admin.site.register(CarUsage)
