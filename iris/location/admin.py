# -*- coding: utf-8 -*-
#  Python core
from __future__ import absolute_import, unicode_literals

# Django modules
from django.contrib import admin

# Third-party modules
from import_export.admin import ImportExportModelAdmin

# My modules
from .models import Country
from .models import Nationality
from .models import Region
from .models import Province
from .models import Town
from .models import Location
from .models import AddressType
from iris.admin_base import AdminBase


@admin.register(Country)
class CountryAdmin(AdminBase, ImportExportModelAdmin):
    pass


@admin.register(Nationality)
class NationalityAdmin(AdminBase, ImportExportModelAdmin):
    pass


class ProvinceInline(admin.TabularInline):
    model = Province


@admin.register(Region)
class RegionAdmin(AdminBase, ImportExportModelAdmin):
    inlines = [ProvinceInline]


@admin.register(Province)
class ProvinceAdmin(AdminBase, ImportExportModelAdmin):
    list_display = ['id', 'name', 'region']
    list_filter = ['region']


@admin.register(Town)
class TownAdmin(AdminBase, ImportExportModelAdmin):
    list_display = ['id', 'name', 'province']
    list_filter = ['province']


@admin.register(Location)
class LocationAdmin(AdminBase, ImportExportModelAdmin):
    list_display = ['id', 'name', 'town']
    list_filter = (
        ('town', admin.RelatedOnlyFieldListFilter),
    )


@admin.register(AddressType)
class AddressTypeAdmin(AdminBase, ImportExportModelAdmin):
    pass
