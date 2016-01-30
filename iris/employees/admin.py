# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from datetime import date
from sorl.thumbnail.admin import AdminImageMixin
from django.forms import ModelForm

# Third party apps
from suit.widgets import EnclosedInput

# My models
from .models import Employee, Department, Position,\
    EmployeeType, Workday, WorkSchedule, EmployeeFamily
from people.admin import PersonAddressInline, PersonPhoneInline
# from people.admin import PersonAdmin


class EmployeeForm(ModelForm):
    class Meta:
        # model = Employee
        widgets = {
            'email': EnclosedInput(prepend='icon-envelope'),
            'salary': EnclosedInput(prepend='RD$'),
        }


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
    form = EmployeeForm
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
                'dependent_of',
                'workSchedule',
                'employee_type',
                'salary',
                'contract_termination_date',
            ]})]

    list_display = [
        'id',
        'full_name',
        # 'employee_position',
        # 'employee_department',
        # 'employee_hiring_date',
        'position',
        'department',
        'hiring_date',
        'years_of_work',
        'birth_day',
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
    inlines = [
        EmployeeAddressInline,
        EmployeePhoneInline,
        # AdditionalsFieldsInline,
        EmployeeFamilyInline,
    ]

    def years_of_work(self, obj):
        today = date.today()
        eaf = Employee.objects.get(id=obj.id)
        return today.year - eaf.hiring_date.year - (
            (today.month, today.day) <
            (eaf.hiring_date.month, eaf.hiring_date.day)
        )
    years_of_work.short_description = "Years of work"

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
