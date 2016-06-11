# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import HouseMaterial
from .models import HousePart
from .models import PropertyType


class HouseMaterialInline(admin.TabularInline):
    model = HouseMaterial
    min_num = 1
    extra = 0


@admin.register(HousePart)
class HousePartAdmin(admin.ModelAdmin):
    inlines = [HouseMaterialInline]

#
# admin.site.register(HouseMaterial)
# admin.site.register(HousePart)
admin.site.register(PropertyType)
