# -*- coding: utf-8 -*-
# Python core modules
from __future__ import absolute_import, unicode_literals

# Django modules
from django.contrib import admin

# Third-party modules
from sorl.thumbnail.admin import AdminImageMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import nested_admin

# My modules
from .models import Member
from .models import Diagnosis
from .models import Cane
from .models import House
from .models import Occupation
from .models import MemberFamily
from .models import WorkPlace
from people.admin import PersonAddressInline
from people.admin import PersonPhoneInline
from doctors.models import Appointment
from doctors.models import PrescribedMedicine
from .forms import MemberForm
from iris.admin_base import AdminBase


class MemberResource(resources.ModelResource):

    class Meta:
        model = Member
        fields = (
            'member_number',
            'names',
            'father_last_name',
            'mother_last_name',
            'email',
            'birthday',
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


class MemberFamilyInline(nested_admin.NestedStackedInline):
    model = MemberFamily
    fields = [
        'kinship',
        'names',
        'father_last_name',
        'mother_last_name',
        'gender',
        'birthday',
        'nationality',
        'marital_status'
    ]
    extra = 0
    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.VERTICAL,
    }
    suit_classes = 'suit-tab suit-tab-memberfamily'


class HouseInline(nested_admin.NestedStackedInline):
    model = House
    min_num = 1
    max_num = 1
    extra = 0
    suit_classes = 'suit-tab suit-tab-house'
    radio_fields = {
        "property_type": admin.HORIZONTAL,
        "ceiling": admin.HORIZONTAL,
        "wall": admin.HORIZONTAL,
        "floor": admin.HORIZONTAL
    }


class PrescribedMedicineInline(nested_admin.NestedStackedInline):
    model = PrescribedMedicine
    sortable_field_name = 'appointment'
    extra = 0
    radio_fields = {
        "unit": admin.HORIZONTAL,
        # "frecuency_unit": admin.HORIZONTAL,
    }
    fields = (
        ('medicine', 'quantity'),
        'unit',
        ('frecuency', 'frecuency_unit'),
        'instructions',
    )


class AppointmentInline(nested_admin.NestedStackedInline):
    model = Appointment
    sortable_field_name = 'member'
    min_num = 0
    extra = 0
    fields = [
        'appointment_date',
        'clinic',
        'doctor',
        'symptomatology',
        'prescription',
        'date_next_appoitment'
    ]
    # readonly_fields = [
    #     'appointment_date',
    #     'clinic',
    #     'doctor',
    #     'symptomatology',
    #     'prescription',
    #     'date_next_appoitment'
    # ]
    inlines = [PrescribedMedicineInline]
    suit_classes = 'suit-tab suit-tab-appointment'


@admin.register(Member)
class MemberAdmin(AdminImageMixin, nested_admin.NestedModelAdmin):
    form = MemberForm
    resources_class = MemberResource
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'picture',
                'names',
                ('father_last_name', 'mother_last_name',),
                'member_number',
                ('age', 'is_mother', 'children_quantity',),
                'main_location',
                'email',
                'birthday',
                'academic_level',
                'nationality',
                'marital_status',
                'gender',
                'document_type',
                'document_id',
                # 'status',
            ]}
        ),
        ('Additional Info', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'diagnosis',
                'cane_number',
                'currently_works',
                'occupation',
                'where_work',
                'health_insurance',
                'observations',
            ]}
        )
    ]

    list_display = [
        # 'member_number',
        'image_tag',
        'full_name',
        # 'gender',
        'member_is_mother',
        'get_children_quantity',
        'main_phone',
        'calculate_age',
        # 'academic_level',
        'main_address',
        'get_location',
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
        'currently_works',
        'where_work',
        # ('where_work', admin.RelatedOnlyFieldListFilter),
        ('marital_status', admin.RelatedOnlyFieldListFilter),
        ('academic_level', admin.RelatedOnlyFieldListFilter),
        ('occupation', admin.RelatedOnlyFieldListFilter),
        'house__property_type',
        ('main_location', admin.RelatedOnlyFieldListFilter),
        # DecadeBornListFilter
    ]

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
        "academic_level": admin.HORIZONTAL
    }

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    filter_horizontal = ['diagnosis', 'occupation']

    inlines = [
        MemberAddressInline,
        MemberPhoneInline,
        MemberFamilyInline,
        HouseInline,
        AppointmentInline,
    ]

    search_fields = [
        'names',
        'father_last_name',
        'mother_last_name'
    ]

    readonly_fields = (
        'member_number',
        'children_quantity',
        'is_mother',
        'age',
        'main_location',
    )

    def get_readonly_fields(self, request, obj=None):
        '''
        Query the group to which the user belongs and change the
        read-only fields if the group is "Secretarias" by the elements
        of the variable secretary_readonly_fields
        '''
        new_readonly_fields = Member._meta.get_all_field_names()

        ignored_list_fields = [
            'picture', 'where_work', 'occupation', 'observations',
            'health_insurance', 'academic_level', 'currently_works'
        ]

        for item in ignored_list_fields:
            new_readonly_fields.remove(item)

        secretary_readonly_fields = new_readonly_fields

        if request.user.groups.filter(name='Secretarias').exists() and obj:
            return secretary_readonly_fields
        else:
            return super(MemberAdmin, self)\
                .get_readonly_fields(request, obj=obj)

    list_per_page = 10

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Info-Adicional'),
        ('memberaddress', 'Direcciones'),
        ('memberphone', 'Telefonos'),
        ('memberfamily', 'Familiares'),
        ('house', 'Tipo de vivienda'),
        ('appointment', 'Citas médicas'),
    )

    ordering = ['-member_number']


@admin.register(Diagnosis)
class DiagnosisAdmin(AdminBase):
    pass


@admin.register(Cane)
class CaneAdmin(AdminBase):
    pass


@admin.register(Occupation)
class OccupationAdmin(AdminBase):
    pass


@admin.register(WorkPlace)
class WorkPlaceAdmin(AdminBase):
    pass
