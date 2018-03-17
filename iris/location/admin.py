# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Country
from .models import Nationality
from .models import Region
from .models import Province
from .models import Town
from .models import Location
from .models import AddressType


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Nationality)
class NationalityAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10


class ProvinceInline(admin.TabularInline):
    model = Province


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    inlines = [ProvinceInline]


@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'region']
    list_display_links = ['id', 'name']
    list_filter = ['region']
    search_fields = ['name', 'region__name']
    list_per_page = 10


@admin.register(Town)
class TownAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'province']
    list_display_links = ['id', 'name']
    list_filter = ['province']
    search_fields = ['name', 'province__name']
    list_per_page = 10


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'town']
    list_display_links = ['id', 'name']
    list_filter = ['town']
    search_fields = ['name', 'town__name']
    list_per_page = 10


@admin.register(AddressType)
class AddressTypeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
