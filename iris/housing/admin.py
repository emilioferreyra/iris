# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from . import models


admin.site.register(models.HousePart)
admin.site.register(models.HouseMaterial)
admin.site.register(models.PropertyType)
