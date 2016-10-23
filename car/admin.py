from django.contrib import admin

from car.models import Group, Car, CarAccess

admin.site.register(Group)
admin.site.register(Car)
admin.site.register(CarAccess)
