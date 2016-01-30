# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

# My apps
from .models import Member, Disability, Cane,\
    House, Ocupation, MemberFamily
from people.admin import PersonAddressInline, PersonPhoneInline


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


class HouseInline(admin.TabularInline):
    model = House
    min_num = 3
    max_num = 3
    extra = 0
    suit_classes = 'suit-tab suit-tab-house'


class MemberAdmin(admin.ModelAdmin):
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
                'disabilities',
                'cane_number',
                'property_type',
                'currently_works',
                'ocupation',
                'where_work',
                'observations',
                ]
            })]

    list_display = [
        'id',
        'status',
        'full_name',
        'gender',
        'is_mother',
        'children_quantity',
        'email',
        'calculate_age',
        'birth_day',
        'was_created_recently',
        ]

    list_display_links = [
        'id',
        'full_name',
        ]

    list_filter = [
        'status',
        'marital_status'
    ]
    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
    }

    # filter_vertical = [
    #     'disabilities'
    #     ]

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

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Additional Info'),
        ('memberaddress', 'Addresses'),
        ('memberphone', 'Phones'),
        ('memberfamily', 'Family'),
        ('house', 'House Type'),
        )


admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(Member, MemberAdmin)
admin.site.register(House)
admin.site.register(Ocupation)
