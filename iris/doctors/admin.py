# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from sorl.thumbnail.admin import AdminImageMixin

from .models import (
    Doctor,
    Clinic,
    Speciality,
    Appointment,
    Medicine,
    PrescribedMedicine
)
from people.admin import PersonPhoneInline


class DoctorPhoneInline(PersonPhoneInline):
    suit_classes = 'suit-tab suit-tab-phones'


@admin.register(Doctor)
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
        ('additionalsfields', 'Adicional'),
        ('phones', 'Teléfonos'),
    )


class PrescribedMedicineInlines(admin.StackedInline):
    """docstring for PrescribedMedicineInlines"""
    model = PrescribedMedicine
    extra = 0
    suit_classes = 'suit-tab suit-tab-prescribedmedicine'


@admin.register(Appointment)
class AppointmentAdmin(AdminImageMixin, admin.ModelAdmin):
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
        # 'member_link',
        # 'doctor_link',
        'clinic'
    ]

    list_display_links = [
        'id',
        'appointment_date',
    ]

    search_fields = [
        'member__names',
        'member__father_last_name',
        'member__mother_last_name',
        'doctor__names',
        'doctor__father_last_name',
        'doctor__mother_last_name',
        'clinic__name'
    ]
    list_filter = (
        'appointment_date',
        ('clinic', admin.RelatedOnlyFieldListFilter),
        ('member', admin.RelatedOnlyFieldListFilter),
        ('doctor', admin.RelatedOnlyFieldListFilter),
        'prescribedmedicine__medicine',
    )

    inlines = [PrescribedMedicineInlines]

    suit_form_tabs = (
        ('general', 'General'),
        ('prescription', 'Prescripcion'),
        ('prescribedmedicine', 'Medicinas prescritas'),
    )
    list_per_page = 5

    read_only_fields = ('member_link', 'doctor_link',)

    def member_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:members_member_change", args=(obj.member.pk,)),
            obj.member.names
        ))
    member_link.short_description = 'miembro'
    member_link.admin_order_field = 'member'

    def doctor_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:doctors_doctor_change", args=(obj.doctor.pk,)),
            obj.doctor.father_last_name
        ))
    doctor_link.short_description = 'doctor'
    doctor_link.admin_order_field = 'doctor'


@admin.register(Clinic)
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
        'id',
        'name',
        'town',
        'address',
        'phone_number',
        'email'
    ]
    list_display_links = ['id', 'name']


admin.site.register(Speciality)
admin.site.register(Medicine)
