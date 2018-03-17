# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django import forms

from sorl.thumbnail.admin import AdminImageMixin

from .models import Employee
from .models import Department
from .models import Position
from .models import EmployeeType
from .models import Workday
from .models import WorkSchedule
from .models import EmployeeFamily
from .models import PositionLevel
from people.admin import PersonAddressInline
from people.admin import PersonPhoneInline


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        # widgets = {
        #     'email': EnclosedInput(prepend='icon-envelope'),
        #     'salary': EnclosedInput(prepend='RD$'),
        # }


class EmployeeAddressInline(PersonAddressInline):
    suit_classes = 'suit-tab suit-tab-employeeaddress'


class EmployeePhoneInline(PersonPhoneInline):
    suit_classes = 'suit-tab suit-tab-employeephone'


class EmployeeFamilyInline(admin.StackedInline):
    model = EmployeeFamily
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
        "document_type": admin.HORIZONTAL,
    }
    suit_classes = 'suit-tab suit-tab-employeefamily'


@admin.register(Employee)
class EmployeeAdmin(AdminImageMixin, admin.ModelAdmin):
    # def delete(self, obj):
    #     return '<input type="button" value="Delete" \
    # onclick="location.href=\%s/delete/\'" />'.format(obj.pk)

    # delete.allow_tags = True
    # delete.short_description = 'Delete object'

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
                'academic_level',
                'marital_status',
                'gender',
                'document_type',
                'document_id',
                'status',
                ]
            }),
        ('Información Adicional', {
            'classes': ('suit-tab', 'suit-tab-additionalsfields',),
            'fields': [
                'hiring_date',
                'department',
                'position',
                # 'employee_level',
                'dependent_of',
                'workSchedule',
                'employee_type',
                'salary',
                'contract_termination_date',
            ]})]

    list_display = [
        'id',
        'full_name',
        # 'get_position_level',
        'position',
        'department',
        'email',
        'main_phone',
        # 'hiring_date',
        'years_of_work',
        # 'birth_day',
        # 'calculate_age',
        'status',
        # 'delete_link',
        # 'edit_link',
        # 'delete',
        ]

    list_display_links = ['id', 'full_name']

    list_filter = (
        'status',
        ('marital_status', admin.RelatedOnlyFieldListFilter),
        'gender',
    )

    radio_fields = {
        "gender": admin.VERTICAL,
        "document_type": admin.HORIZONTAL,
        "marital_status": admin.HORIZONTAL,
        "academic_level": admin.HORIZONTAL,
    }

    search_fields = ['name']

    ordering = ['department']

    inlines = [
        EmployeeAddressInline,
        EmployeePhoneInline,
        # AdditionalsFieldsInline,
        EmployeeFamilyInline,
    ]

    def get_position_level(self, obj):
        position_level = Position.objects.filter(id=obj.position_id)
        for e in position_level:
            return e.position_level_id
    get_position_level.short_description = "Position level"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # position_level = Position.objects.filter(id=4)
        # for e in position_level:
        #     return e.position_level_id
        if db_field.name == "dependent_of":
            kwargs["queryset"] = Employee.objects.filter(
                position__position_level_id__gt=1
                )
        return super(EmployeeAdmin, self).\
            formfield_for_foreignkey(db_field, request, **kwargs)

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Adicional'),
        ('employeeaddress', 'Direcciones'),
        ('employeephone', 'Teléfonos'),
        ('employeefamily', 'Familiares'),
        )


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    # filter_horizontal = ['workdays']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(EmployeeType)
admin.site.register(Workday)
admin.site.register(PositionLevel)
