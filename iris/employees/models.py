# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Third party apps
from smart_selects.db_fields import ChainedForeignKey

# My apps
from commons.models import PersonType
from people.models import Person, EmployeeManager, EmployeeFamilyManager


class EmployeeType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Employee Type"
        verbose_name_plural = "Employee Types"
        db_table = "employees_employee_type"

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __unicode__(self):
        return self.name


class PositionLevel(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=45, unique=True, null=True)

    class Meta:
        verbose_name = "Position Level"
        verbose_name_plural = "Position Levels"
        db_table = "employees_position_lavels"

    def __unicode__(self):
        return self.name


class Position(models.Model):
    department = models.ForeignKey(Department)
    position_level = models.ForeignKey(PositionLevel, null=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __unicode__(self):
        return self.name


class Workday(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Workday"
        verbose_name_plural = "Workdays"
        ordering = ['id']

    def __unicode__(self):
        return self.name


class WorkSchedule(models.Model):
    name = models.CharField(max_length=45, unique=True)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    workdays = models.ManyToManyField(Workday)

    class Meta:
        verbose_name = "Work Schedule"
        verbose_name_plural = "Work Schedules"
        db_table = "employees_work_schedule"

    def __unicode__(self):
        return self.name


class Employee(Person):
    objects = EmployeeManager()
    hiring_date = models.DateField()
    department = models.ForeignKey(Department)
    position = ChainedForeignKey(
        Position,
        chained_field="department",
        chained_model_field="department",
        )
    workSchedule = models.ForeignKey(WorkSchedule)
    employee_type = models.ForeignKey(EmployeeType)
    salary = models.FloatField()
    contract_termination_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def clean(self):
        dob = self.birth_day
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (
                today.year, today.month, today.day):
            raise ValidationError(
                {'birth_day': _('Must be at least 18 years old to register.')})
        if self.hiring_date > today:
            raise ValidationError(
                {'hiring_date': _('The hiring date must to be minor or iqual \
                    to today.')})

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Employee")
        super(Employee, self).save(*args, **kwargs)

    def years_of_work(self):
        today = date.today()
        eaf = Employee.objects.get(id=self.id)
        return today.year - eaf.hiring_date.year - (
            (today.month, today.day) <
            (eaf.hiring_date.month, eaf.hiring_date.day)
        )
    years_of_work.short_description = "Years of work"

    # def get_position_level(self):
    #     position_level = Position.objects.filter(id=self.position_id)
    #     for e in position_level:
    #         return e.position_level_id
    # get_position_level.short_description = "Position level"


class EmployeeFamily(Person):
    objects = EmployeeFamilyManager()

    class Meta:
        verbose_name = "Employee Family"
        verbose_name_plural = "Employee Families"
        proxy = True
        app_label = "employees"

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Employee Family")
        super(EmployeeFamily, self).save(*args, **kwargs)
