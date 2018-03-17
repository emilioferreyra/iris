# -*- coding: utf-8 -*-
# Python modules
from __future__ import absolute_import, unicode_literals

# Django core
from django.contrib import admin

# Third-party modules
from import_export.admin import ImportExportModelAdmin

# My modules
from .models import DocumentType
from .models import MaritalStatus
from .models import PhoneType
from .models import AcademicLevel
from .models import Kinship
from iris.admin_base import AdminBase


@admin.register(DocumentType)
class DocuentTypeAdmin(AdminBase, ImportExportModelAdmin):
    pass


@admin.register(MaritalStatus)
class MaritalStatusAdmin(AdminBase, ImportExportModelAdmin):
    pass

@admin.register(PhoneType)
class PhoneTypeAdmin(AdminBase, ImportExportModelAdmin):
    pass

@admin.register(AcademicLevel)
class AcademicLevelAdmin(AdminBase, ImportExportModelAdmin):
    pass

@admin.register(Kinship)
class KinshipAdmin(AdminBase, ImportExportModelAdmin):
    pass
