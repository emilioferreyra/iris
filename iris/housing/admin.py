# -*- coding: utf-8 -*-
# Python core modules
from __future__ import absolute_import, unicode_literals

# Django modules
from django.contrib import admin

# Third-party modules
from import_export.admin import ImportExportModelAdmin

# My modules
from .models import HouseMaterial
from .models import HousePart
from .models import PropertyType
from iris.admin_base import AdminBase


class HouseMaterialInline(admin.TabularInline):
    model = HouseMaterial
    min_num = 1
    extra = 0


@admin.register(HousePart)
class HousePartAdmin(admin.ModelAdmin):
    inlines = [HouseMaterialInline]


@admin.register(PropertyType)
class PropertyTypeAdmin(AdminBase, ImportExportModelAdmin):
    pass
