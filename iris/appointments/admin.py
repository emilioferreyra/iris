# -*- coding: utf-8 -*-

# Django core
from __future__ import absolute_import
from django.contrib import admin

# My apps
from .models import Appointment, Medicine, PrescribedMedicine


class PrescribedMedicineInlines(admin.TabularInline):
    """docstring for PrescribedMedicineInlines"""
    model = PrescribedMedicine
    extra = 0


class AppointmentAdmin(admin.ModelAdmin):
    """docstring for AppointmentAdmin"""
    model = Appointment
    fields = (
        ('date', 'clinic'),
        ('member', 'doctor'),
        'symptomatology',
        'date_next_appoitment'
    )
    list_display = [
        'id',
        'date',
        'member',
        'doctor',
        'clinic'
        ]
    search_fields = [
        'member',
        'doctor',
        'clinic'
        ]
    list_filter = [
        'doctor',
        'clinic',
        'date'
        ]
    list_display_links = [
        'date',
        'member',
        'doctor',
        'clinic'
        ]

    inlines = [PrescribedMedicineInlines]


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Medicine)
admin.site.register(PrescribedMedicine)
