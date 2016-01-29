# # -*- coding: utf-8 -*-
# # Django core
# from __future__ import absolute_import, unicode_literals
# from django.contrib import admin
# # from django.db import models
# # from django.forms import CheckboxSelectMultiple

# # My apps
# from .models import Doctor, DoctorAdditionalField, Clinic, Speciality, \
#     Appointment, Medicine, PrescribedMedicine
# from people.admin import PersonPhoneInline


# class DoctorAdditionalFieldInline(admin.StackedInline):
#     model = DoctorAdditionalField
#     filter_horizontal = [
#         'specialities',
#         'clinics'
#     ]
#     suit_classes = 'suit-tab suit-tab-additionalsfields'


# class DoctorPhoneInline(PersonPhoneInline):
#     suit_classes = 'suit-tab suit-tab-phones'


# class DoctorAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {
#             'classes': ('suit-tab', 'suit-tab-general',),
#             'fields': [
#                 'picture',
#                 'names',
#                 'father_last_name',
#                 'mother_last_name',
#                 'email',
#                 'birth_day',
#                 'nationality',
#                 'marital_status',
#                 'gender',
#                 'document_type',
#                 'document_id',
#                 'status',
#                 ]
#             })]

#     list_display = [
#         'id',
#         # 'person_type',
#         'full_name',
#         'email'
#         ]
#     list_display_links = ['id', 'full_name']

#     inlines = [
#         DoctorAdditionalFieldInline,
#         DoctorPhoneInline
#     ]

#     list_filter = ['status']

#     suit_form_tabs = (
#         ('general', 'General'),
#         ('additionalsfields', 'Additional Info'),
#         ('phones', 'Phones'),
#         )


# class PrescribedMedicineInlines(admin.TabularInline):
#     """docstring for PrescribedMedicineInlines"""
#     model = PrescribedMedicine
#     extra = 0


# class AppointmentAdmin(admin.ModelAdmin):
#     """docstring for AppointmentAdmin"""
#     model = Appointment
#     fields = (
#         'date',
#         ('clinic', 'doctor'),
#         ('member'),
#         'symptomatology',
#         'prescription',
#         'date_next_appoitment'
#     )
#     list_display = [
#         'id',
#         'date',
#         'member',
#         'doctor',
#         'clinic'
#         ]
#     search_fields = [
#         'member',
#         'doctor',
#         'clinic'
#         ]
#     list_filter = (
#         'date',
#         ('clinic', admin.RelatedOnlyFieldListFilter),
#         ('member', admin.RelatedOnlyFieldListFilter),
#         ('doctor', admin.RelatedOnlyFieldListFilter),
#     )
#     list_display_links = [
#         'id',
#         'date',
#         # 'member',
#         # 'doctor',
#         # 'clinic'
#         ]
#     ordering = ['-id']

#     inlines = [PrescribedMedicineInlines]


# admin.site.register(Doctor, DoctorAdmin)
# # admin.site.register(DoctorAdditionalField)
# admin.site.register(Clinic)
# admin.site.register(Speciality)
# admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(Medicine)
# admin.site.register(PrescribedMedicine)
