# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# from django.db import models
# from django.forms import CheckboxSelectMultiple

from sorl.thumbnail.admin import AdminImageMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import (
    Member,
    Diagnosis,
    Cane,
    House,
    Occupation,
    MemberFamily
)
from people.admin import PersonAddressInline, PersonPhoneInline
from doctors.models import Appointment
from .forms import MemberForm


# class DecadeBornListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('decade born')

#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decade'

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('80s', _('in the eighties')),
#             ('90s', _('in the nineties')),
#         )

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == '80s':
#             return queryset.filter(
#                 birthday__gte=date(1980, 1, 1),
#                 birthday__lte=date(1989, 12, 31)
#             )
#         if self.value() == '90s':
#             return queryset.filter(
#                 birthday__gte=date(1990, 1, 1),
#                 birthday__lte=date(1999, 12, 31)
#             )


class MemberResource(resources.ModelResource):

    class Meta:
        model = Member
        fields = (
            'member_number',
            'names',
            'father_last_name',
            'mother_last_name',
            'email',
            'birthday',
            'academic_level__name',
            'nationality__name',
            'marital_status__name',
            'gender',
            'document_type__name',
            'document_id',
            'status',
        )


class MemberAddressInline(PersonAddressInline):
    suit_classes = 'suit-tab suit-tab-memberaddress'


class MemberPhoneInline(PersonPhoneInline):
    suit_classes = 'suit-tab suit-tab-memberphone'


class MemberFamilyInline(admin.StackedInline):
    model = MemberFamily
    fields = [
        'kinship',
        'names',
        'father_last_name',
        'mother_last_name',
        'gender',
        'birthday',
        'nationality',
        'marital_status'
    ]
    extra = 0
    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.VERTICAL,
    }
    suit_classes = 'suit-tab suit-tab-memberfamily'


class HouseInline(admin.StackedInline):
    model = House
    min_num = 1
    max_num = 1
    extra = 0
    suit_classes = 'suit-tab suit-tab-house'


class AppointmentInline(admin.StackedInline):
    model = Appointment
    min_num = 0
    extra = 0
    fields = [
        'appointment_date',
        'clinic',
        'doctor',
        'symptomatology',
        'prescription',
        'date_next_appoitment'
    ]
    readonly_fields = [
        'appointment_date',
        'clinic',
        'doctor',
        'symptomatology',
        'prescription',
        'date_next_appoitment'
    ]
    suit_classes = 'suit-tab suit-tab-appointment'


@admin.register(Member)
class MemberAdmin(AdminImageMixin, ImportExportModelAdmin):
    form = MemberForm
    resources_class = MemberResource
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'picture',
                'names',
                ('father_last_name', 'mother_last_name',),
                'member_number',
                ('age', 'is_mother', 'children_quantity',),
                'main_location',
                'email',
                'birthday',
                'academic_level',
                'nationality',
                'marital_status',
                'gender',
                'document_type',
                'document_id',
                # 'status',
            ]}
        ),
        ('Additional Info', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'diagnosis',
                'cane_number',
                'currently_works',
                'occupation',
                'where_work',
                'health_insurance',
                'observations',
            ]}
        )
    ]

    list_display = [
        # 'member_number',
        'image_tag',
        'full_name',
        # 'gender',
        'member_is_mother',
        'get_children_quantity',
        'main_phone',
        'calculate_age',
        # 'academic_level',
        'main_address',
        'get_location',
        'status',
    ]

    list_display_links = [
        # 'member_number',
        'image_tag',
        'full_name',
    ]

    list_filter = [
        'status',
        'created',
        'is_mother',
        'gender',
        ('marital_status', admin.RelatedOnlyFieldListFilter),
        ('academic_level', admin.RelatedOnlyFieldListFilter),
        ('occupation', admin.RelatedOnlyFieldListFilter),
        'house__property_type',
        ('main_location', admin.RelatedOnlyFieldListFilter),
        # DecadeBornListFilter
    ]

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
        "academic_level": admin.HORIZONTAL
    }

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    filter_horizontal = ['diagnosis', 'occupation']

    inlines = [
        MemberAddressInline,
        MemberPhoneInline,
        MemberFamilyInline,
        HouseInline,
        # AppointmentInline,
    ]

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name'
    ]

    readonly_fields = (
        'member_number',
        'children_quantity',
        'is_mother',
        'age',
        'main_location',
    )

    def get_readonly_fields(self, request, obj=None):
        '''
        Query the group to which the user belongs and change the
        read-only fields if the group is "Secretarias" by the elements
        of the variable secretary_readonly_fields
        '''
        new_readonly_fields = Member._meta.get_all_field_names()

        ignored_list_fields = [
            'picture', 'where_work', 'occupation', 'observations',
            'health_insurance', 'academic_level', 'currently_works',
        ]

        for item in ignored_list_fields:
            new_readonly_fields.remove(item)

        secretary_readonly_fields = new_readonly_fields

        if request.user.groups.filter(name='Secretarias').exists():
            return secretary_readonly_fields
        else:
            return super(MemberAdmin, self)\
                .get_readonly_fields(request, obj=obj)

    list_per_page = 10

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Información Adicional'),
        ('memberaddress', 'Direcciones'),
        ('memberphone', 'Telefonos'),
        ('memberfamily', 'Familiares'),
        ('house', 'Tipo de vivienda'),
        # ('appointment', 'Citas médicas'),
    )

    ordering = ['-member_number']


admin.site.register(Diagnosis)
admin.site.register(Cane)
admin.site.register(Occupation)
