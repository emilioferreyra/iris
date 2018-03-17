# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import DocumentType
from .models import MaritalStatus
from .models import PhoneType
from .models import AcademicLevel
from .models import Kinship


@admin.register(DocumentType)
class DocuentTypeAdmin(ImportExportModelAdmin):
    pass


@admin.register(MaritalStatus)
class MaritalStatusAdmin(ImportExportModelAdmin):
    pass

@admin.register(PhoneType)
class PhoneTypeAdmin(ImportExportModelAdmin):
    pass

@admin.register(AcademicLevel)
class AcademicLevelAdmin(ImportExportModelAdmin):
    pass

@admin.register(Kinship)
class KinshipAdmin(ImportExportModelAdmin):
    pass
