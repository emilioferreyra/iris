# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from . import models


admin.site.register(models.DocumentType)
admin.site.register(models.MaritalStatus)
admin.site.register(models.PhoneType)
admin.site.register(models.AcademicLevel)
admin.site.register(models.Kinship)
