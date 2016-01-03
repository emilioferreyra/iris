# Core Django
from __future__ import absolute_import
from django.contrib import admin
# My apps
from . import models


admin.site.register(models.MedicalSpeciality)
admin.site.register(models.Doctor)
admin.site.register(models.Address)
admin.site.register(models.DoctorPhones)
