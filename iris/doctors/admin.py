# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
# from django.db import models
# from django.forms import CheckboxSelectMultiple

# My apps
from .models import Doctor, Clinic, Speciality, \
    Appointment, Medicine, PrescribedMedicine
from people.admin import PersonPhoneInline


class DoctorPhoneInline(PersonPhoneInline):
    suit_classes = 'suit-tab suit-tab-phones'


class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'picture',
                'names',
                'father_last_name',
                'mother_last_name',
                'email',
                'birth_day',
                'nationality',
                'marital_status',
                'gender',
                'document_type',
                'document_id',
                'status',
                ]
        }),
        ('Additional Info', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'specialities',
                'clinic'
                ]
            })]

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
    }

    list_display = [
        'id',
        'doctor_name',
        'email',
        'main_phone',
        'status',
        ]

    list_display_links = [
        'id',
        'doctor_name'
        ]

    filter_vertical = [
        'specialities',
        'clinic'
        ]

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name',
        # 'clinic',
        # 'specialities'
        ]

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    inlines = [
        DoctorPhoneInline
    ]

    list_filter = (
        'status',
        ('clinic', admin.RelatedOnlyFieldListFilter),
        ('specialities', admin.RelatedOnlyFieldListFilter),
        )

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Additional Info'),
        ('phones', 'Phones'),
        )


class PrescribedMedicineInlines(admin.StackedInline):
    """docstring for PrescribedMedicineInlines"""
    model = PrescribedMedicine
    extra = 0
    suit_classes = 'suit-tab suit-tab-prescribedmedicine'


class AppointmentAdmin(admin.ModelAdmin):
    """docstring for AppointmentAdmin"""
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'appointment_date',
                'clinic',
                'doctor',
                'member',
                'symptomatology',
                'date_next_appoitment'
                ]
            }),
        ('Prescription', {
            'classes': ('suit-tab', 'suit-tab-prescription',),
            'fields': [
                'prescription'
                ]
            })]

    list_display = [
        'id',
        'appointment_date',
        'member',
        'doctor',
        'clinic'
        ]
    search_fields = [
        'member',
        'doctor',
        'clinic'
        ]
    list_filter = (
        'appointment_date',
        ('clinic', admin.RelatedOnlyFieldListFilter),
        ('member', admin.RelatedOnlyFieldListFilter),
        ('doctor', admin.RelatedOnlyFieldListFilter),
    )
    list_display_links = [
        'id',
        'appointment_date',
        'member',
        # 'doctor',
        # 'clinic'
        ]
    # ordering = ['-id']

    inlines = [PrescribedMedicineInlines]

    suit_form_tabs = (
        ('general', 'General'),
        ('prescription', 'Prescription'),
        ('prescribedmedicine', 'Prescribed Medicines'),
        )


class ClinicAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'region',
        'province',
        'town',
        'address',
        'phone_number',
        'email',
        'company_logo',
        ]
    list_display = [
        'name',
        'town',
        'address',
        'phone_number',
        'email'
        ]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Speciality)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Medicine)
