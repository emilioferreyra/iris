from __future__ import absolute_import
from django.contrib import admin

from .models import Person, PersonAddress, PersonPhone


class PersonAddressInlines(admin.StackedInline):
    model = PersonAddress
    extra = 0
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
        ('names', 'father_name', 'mother_name', 'email'),
        ('birth_day', 'nationality', 'marital_status'),
        ('gender', 'document_type', 'document_id'),
        # ('dependent', 'parent_of'),
        'status', 'person_type'
        )

    list_display = [
        'id',
        'full_name',
        'email',
        'status'
        ]

    search_fields = ['names', 'father_name', 'mother_name']

    inlines = [
        PersonAddressInlines,
        PersonPhoneInlines
    ]

    def full_name(self, obj):
        return "%s %s %s" % (obj.names, obj.father_name, obj.mother_name)
    full_name.short_description = 'Name'


# admin.site.register(PersonType)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonAddress)
# admin.site.register(PersonPhone)
