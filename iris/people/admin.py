from __future__ import absolute_import
from datetime import date
from django.contrib import admin

from .models import Person, PersonAddress, PersonPhone
from people.models import Kinsman


class KinsmanInline(admin.StackedInline):
    model = Kinsman
    fields = [
        'kinship',
        ('names', 'father_last_name', 'mother_last_name'),
        ('gender', 'birth_day', 'nationality'),
        'marital_status'
    ]

    extra = 0
    min_num = 1

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
    }


class PersonAddressInlines(admin.StackedInline):
    model = PersonAddress
    extra = 1
    fields = [
        'address_type',
        ('street', 'building', 'apartment'),
        'country',
        ('region', 'province', 'town'),
        ]
    min_num = 1


class PersonPhoneInlines(admin.TabularInline):
    model = PersonPhone
    extra = 0
    min_num = 1


class PersonAdmin(admin.ModelAdmin):
    list_display_links = ('full_name',)
    list_editable = ['status']
    list_filter = ['status', 'person_type']
    fields = (
        ('names', 'father_last_name', 'mother_last_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        # ('dependent', 'parent_of'),
        'status', 'person_type'
        )

    list_display = [
        'id',
        'person_type',
        'full_name',
        'email',
        'calculate_age',
        'status'
        ]

    radio_fields = {
        # "marital_status": admin.HORIZONTAL,
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
    }

    search_fields = ['names', 'father_last_name', 'mother_last_name']

    inlines = [
        PersonAddressInlines,
        PersonPhoneInlines,
        KinsmanInline
    ]

    def full_name(self, obj):
        return "%s %s %s" % (
            obj.names,
            obj.father_last_name,
            obj.mother_last_name
        )
    full_name.short_description = 'Name'

    def calculate_age(self, obj):
        today = date.today()
        return today.year - obj.birth_day.year - (
            (today.month, today.day) < (obj.birth_day.month, obj.birth_day.day)
        )
    calculate_age.short_description = "Age"


# admin.site.register(PersonType)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonAddress)
# admin.site.register(PersonPhone)
