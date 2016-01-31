# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
# from django.db import models
# from django.forms import CheckboxSelectMultiple

# Third party apps
from sorl.thumbnail.admin import AdminImageMixin

# My apps
from .models import SupplierCompany, SupplierType, SupplierContact
from people.admin import PersonPhoneInline


class SupplierContactPhoneInline(PersonPhoneInline):
    suit_classes = 'suit-tab suit-tab-suppliercontactphone'


class SupplierContactAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'picture',
                'supplier_company',
                'names',
                'father_last_name',
                'mother_last_name',
                'email',
                'birth_day',
                'nationality',
                'marital_status',
                'gender',
                ]
            })]
    list_display = [
        'full_name',
        'supplier_company',
        'email',
        ]
    inlines = [SupplierContactPhoneInline]
    search_fields = ['name', 'supplier_company']
    # list_filter = ['supplier_company', 'supplier_company__supplier_type']
    list_filter = (
        ('supplier_company', admin.RelatedOnlyFieldListFilter),
        'supplier_company__supplier_type'
        )
    suit_form_tabs = (
        ('general', 'General'),
        ('suppliercontactphone', 'Phones'),
        )


class SupplierContactInline(admin.StackedInline):
    model = SupplierContact
    fields = [
        'picture',
        'supplier_company',
        'names',
        'father_last_name',
        'mother_last_name',
        'email',
        'birth_day',
        'nationality',
        'marital_status',
        'gender',
        ]
    min_num = 0
    extra = 0
    suit_classes = 'suit-tab suit-tab-suppliercontact'


class SupplierCompanyAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'supplier_type',
        'address',
        'phone_number',
        'email',
        ]

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                "company_logo",
                "name",
                "supplier_type",
                "country",
                "region",
                "province",
                "town",
                "address",
                "phone_number",
                "email",
                ]
            })]
    # inlines = [SupplierContactInline]

    search_fields = ['name']

    # list_filter = ('supplier_type',)

    list_filter = (
        ('supplier_type', admin.RelatedOnlyFieldListFilter),
        )

    suit_form_tabs = (
        ('general', 'General'),
        # ('suppliercontact', 'Contacts'),
        )


admin.site.register(SupplierContact, SupplierContactAdmin)
admin.site.register(SupplierCompany, SupplierCompanyAdmin)
admin.site.register(SupplierType)
