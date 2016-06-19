# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Country
from .models import Nationality
from .models import Region
from .models import Province
from .models import Town
from .models import AddressType


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Nationality)
class NationalityAdmin(ImportExportModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    pass


@admin.register(Town)
class TownAdmin(ImportExportModelAdmin):
    pass


@admin.register(AddressType)
class AddressTypeAdmin(ImportExportModelAdmin):
    pass
