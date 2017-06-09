# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
# from datetime import date
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

#  My apps
from .models import Person, PersonAddress, PersonPhone, PersonType, AddressType
from commons.models import PhoneType


class PersonAddressInline(admin.StackedInline):
    max_num_addresses = AddressType.objects.count()
    model = PersonAddress
    extra = 0
    fields = [
        'address_type',
        'street',
        'building',
        'apartment',
        'region',
        'province',
        'town',
        'location',
        'is_default',
        ]
    min_num = 1
    max_num = max_num_addresses
    # radio_fields = {"is_default": admin.VERTICAL}
    suit_classes = 'suit-tab suit-tab-addresses'


class PersonPhoneInline(admin.TabularInline):
    max_num_phones = PhoneType.objects.count()
    model = PersonPhone
    extra = 0
    min_num = 1
    max_num = max_num_phones
    suit_classes = 'suit-tab suit-tab-phones'


@admin.register(Person)
class PersonAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display_links = ('id', 'full_name',)
    # list_editable = ['status']
    list_filter = (
        'status',
        ('person_type', admin.RelatedOnlyFieldListFilter),
        ('marital_status', admin.RelatedOnlyFieldListFilter),
    )
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
                'status'
                ]
            })]

    list_display = [
        'id',
        'image_tag',
        'status',
        'person_type',
        'full_name',
        'email',
        'calculate_age',
        ]

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
    }

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name',
        'email'
    ]

    inlines = [
        PersonAddressInline,
        PersonPhoneInline
    ]
    ordering = ['-id']

    suit_form_tabs = (
        ('general', 'General'),
        ('addresses', 'Addresses'),
        ('phones', 'Phones'),
        )

    list_per_page = 10


admin.site.register(PersonType)
# admin.site.register(Person, PersonAdmin)
