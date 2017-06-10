# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import SupplierCompany
from .models import SupplierType
from .models import SupplierContact


class SupplierContactInline(admin.StackedInline):
    model = SupplierContact
    fields = [
        ('name', 'email',),
        ('phone_number', 'extension_number',),
        'mobile_number',
        ('department', 'position',),

    ]
    min_num = 0
    extra = 0
    suit_classes = 'suit-tab suit-tab-suppliercontact'


@admin.register(SupplierCompany)
class SupplierCompanyAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = [
        'image_tag',
        'name',
        'supplier_type',
        'address',
        'phone_number',
        'email',
    ]
    list_display_links = ['name', 'image_tag']

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                "company_logo",
                "name",
                ("supplier_type", "country",),
                ("region",
                "province",), ("town",
                "address",), ("phone_number",
                "email",),
            ]
        })]

    inlines = [SupplierContactInline]

    search_fields = ['name']

    list_filter = (
        ('supplier_type', admin.RelatedOnlyFieldListFilter),
    )

    suit_form_tabs = (
        ('general', 'General'),
        ('suppliercontact', 'Contacts'),
    )
    list_per_page = 5


admin.site.register(SupplierType)
