# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from django.db import models
from django.forms import CheckboxSelectMultiple
# from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

# My apps
from .models import Member, Disability, Cane,\
    House, Occupation, MemberFamily
from people.admin import PersonAddressInline, PersonPhoneInline
# from people.models import PersonAddress, PersonPhone

#
# class PersonAddressForm(forms.ModelForm):
#     class Meta:
#         model = PersonAddress
#         fields = "__all__"
#         yes_no = forms.BooleanField(widget=RadioChoiceInput(choices=[(True, 'Yes'),
#                                                             (False, 'No')]))


class MemberAddressInline(PersonAddressInline):
    # form = PersonAddressForm
    # radio_fields = {
    #     "default": admin.VERTICAL
    # }
    # formfield_overrides = {
    #         models.BooleanField: {'widget': RadioSelect},
    #     }
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


class MemberAdmin(AdminImageMixin, admin.ModelAdmin):
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
                ]
            }),
        ('Additional Info', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'disabilities',
                'cane_number',
                # 'property_type',
                'currently_works',
                'occupation',
                'where_work',
                'observations',
                ]
            })]

    list_display = [
        # 'id',
        'member_number',
        'status',
        'full_name',
        # 'names',
        # 'father_last_name',
        # 'mother_last_name',
        'gender',
        'member_is_mother',
        # 'is_mother',
        'children_quantity',
        # 'email',
        'main_phone',
        'calculate_age',
        # 'birth_day',
        # 'was_created_recently',
        # 'main_address',
        ]

    list_display_links = [
        'member_number',
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
        'personaddress__town',
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
        ('additionalsfields', 'Additional Info'),
        ('memberaddress', 'Addresses'),
        ('memberphone', 'Phones'),
        ('memberfamily', 'Family'),
        ('house', 'House Type'),
        )

admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(Member, MemberAdmin)
admin.site.register(Occupation)

# admin.site.register(MemberFamily)
