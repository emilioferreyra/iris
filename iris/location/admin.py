from django.contrib import admin
from . import models


admin.site.register(models.Country)
admin.site.register(models.Nationality)
admin.site.register(models.Region)
admin.site.register(models.Province)
admin.site.register(models.Town)
admin.site.register(models.AddressType)
