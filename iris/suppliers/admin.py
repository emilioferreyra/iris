# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

# Third party apps
from sorl.thumbnail.admin import AdminImageMixin

# My apps
from .models import SupplierCompany, SupplierType, SupplierContact,\
    ContactAdditionalField


class ContactAdditionalFieldInline(admin.StackedInline):
    model = ContactAdditionalField
    min_num = 1
    max_num = 1
    extra = 0


class SupplierContactAdmin(AdminImageMixin, admin.ModelAdmin):
    fields = (
        ('picture', 'names', 'father_last_name', 'mother_last_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        'gender',
        )
    list_display = [
        'full_name',
        'email',
        ]

    inlines = [ContactAdditionalFieldInline]


class SupplierCompanyAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = [
        'name',
        'supplier_type',
        'address',
        'phone_number',
        'email',
        ]
    fields = (
        "company_logo",
        ("name", "supplier_type"),
        "country",
        ("region", "province", "town"),
        ("address", "phone_number", "email"),
        )


admin.site.register(SupplierContact, SupplierContactAdmin)
admin.site.register(SupplierCompany, SupplierCompanyAdmin)
admin.site.register(SupplierType)
