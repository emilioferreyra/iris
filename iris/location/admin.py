from django.contrib import admin
from .models import Country, Nationality, Region, Province, Town


admin.site.register(Country)
admin.site.register(Nationality)
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(Town)
