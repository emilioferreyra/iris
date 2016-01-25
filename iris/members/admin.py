# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

# My apps
from .models import Member, MemberAdditionalField, Disability, Cane,\
    House, Ocupation, MemberFamily
from people.admin import \
    PersonAdmin, PersonAddressInlines, PersonPhoneInlines


class MemberAdditionalFieldInline(admin.StackedInline):
    model = MemberAdditionalField
    min_num = 1
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }
    fields = (
        ('disabilities', 'cane_number', 'property_type'),
        ('currently_works', 'ocupation', 'where_work'),
        'observations'
    )


class MemberFamilyInline(admin.StackedInline):
    model = MemberFamily
    fields = [
        'kinship',
        ('names', 'father_last_name', 'mother_last_name'),
        ('gender', 'birth_day', 'nationality'),
        'marital_status'
    ]
    extra = 0
    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.VERTICAL,
    }


class HouseInline(admin.TabularInline):
    model = House
    min_num = 3
    max_num = 3
    extra = 0


class MemberAdmin(PersonAdmin):
    fields = (
        'picture',
        ('names', 'father_last_name'), ('mother_last_name', 'email'),
        ('birth_day', 'nationality'), 'marital_status',
        'gender', 
        ('document_type', 'document_id'),
        'status'
        )

    list_display = [
        'id',
        'status',
        # 'was_created_recently',
        # 'picture',
        'gender',
        'is_mother',
        'children_quantity',
        'full_name',
        'email',
        'calculate_age',
        'birth_day',
        'was_created_recently',
        ]

    list_filter = [
        'status',
        'marital_status'
    ]

    inlines = [
        MemberAdditionalFieldInline,
        PersonAddressInlines,
        PersonPhoneInlines,
        MemberFamilyInline,
        HouseInline
    ]

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name'
    ]

    def get_queryset(self, request):
        qs = super(MemberAdmin, self).get_queryset(request)
        return qs.filter(person_type=2)


admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(Member, MemberAdmin)
admin.site.register(House)
admin.site.register(Ocupation)
