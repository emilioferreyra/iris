# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from sorl.thumbnail.admin import AdminImageMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import (
    Member,
    Disability,
    Cane,
    House,
    Occupation,
    MemberFamily
)
from people.admin import PersonAddressInline, PersonPhoneInline


class MemberResource(resources.ModelResource):

    class Meta:
        model = Member
        fields = (
            'member_number',
            'names',
            'father_last_name',
            'mother_last_name',
            'email',
            'birth_day',
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
        'birth_day',
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


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin, AdminImageMixin):
    resources_class = MemberResource
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'picture',
                'member_number',
                'names',
                'father_last_name',
                'mother_last_name',
                'email',
                'birth_day',
                'academic_level',
                'nationality',
                'marital_status',
                'gender',
                'document_type',
                'document_id',
                'status',
            ]}
        ),
        ('Additional Info', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'disabilities',
                'cane_number',
                'currently_works',
                'occupation',
                'where_work',
                'observations',
            ]}
        )
    ]

    list_display = [
        # 'member_number',
        'image_tag',
        'full_name',
        'gender',
        'member_is_mother',
        'children_quantity',
        'main_phone',
        'calculate_age',
        'academic_level',
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
        'personaddress__location'
    ]

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
        "academic_level": admin.HORIZONTAL
    }

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    inlines = [
        MemberAddressInline,
        MemberPhoneInline,
        MemberFamilyInline,
        HouseInline
    ]

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name'
    ]

    readonly_fields = ('member_number',)

    list_per_page = 10

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Información Adicional'),
        ('memberaddress', 'Direcciones'),
        ('memberphone', 'Telefonos'),
        ('memberfamily', 'Familiares'),
        ('house', 'Tipo de vivienda'),
    )

    ordering = ['-member_number']


admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(Occupation)
