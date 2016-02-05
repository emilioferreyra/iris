# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from datetime import date
from sorl.thumbnail.admin import AdminImageMixin
# from django.forms import ModelForm
from django import forms

# Third party apps
from suit.widgets import EnclosedInput

# My models
from .models import Employee, Department, Position,\
    EmployeeType, Workday, WorkSchedule, EmployeeFamily, PositionLevel
from people.admin import PersonAddressInline, PersonPhoneInline
# from people.admin import PersonAdmin


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


class EmployeeAdmin(AdminImageMixin, admin.ModelAdmin):
    # form = EmployeeForm
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
                'status',
                ]
            }),
        ('Additional Info', {
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
        'position',
        'department',
        'email',
        'main_phone',
        # 'hiring_date',
        'years_of_work',
        # 'birth_day',
        # 'calculate_age',
        'status'
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
    }

    search_fields = ['name']

    ordering = ['department']

    inlines = [
        EmployeeAddressInline,
        EmployeePhoneInline,
        # AdditionalsFieldsInline,
        EmployeeFamilyInline,
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        employee = 1
        if db_field.name == "dependent_of":
            kwargs["queryset"] = Employee.objects.filter(
                person_type=employee
                )
        return super(EmployeeAdmin, self).\
            formfield_for_foreignkey(db_field, request, **kwargs)

    suit_form_tabs = (
        ('general', 'General'),
        ('additionalsfields', 'Additional Info'),
        ('employeeaddress', 'Addresses'),
        ('employeephone', 'Phones'),
        ('employeefamily', 'Family'),
        )


class WorkScheduleAdmin(admin.ModelAdmin):
    # filter_horizontal = ['workdays']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(EmployeeType)
admin.site.register(Workday)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(PositionLevel)
