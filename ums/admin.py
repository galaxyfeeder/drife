from django.contrib import admin

from ums.models import Driver, NFCIdentification, BLEIdentificaiton

admin.site.register(Driver)
admin.site.register(NFCIdentification)
admin.site.register(BLEIdentificaiton)
