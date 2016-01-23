# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.db import models

# Third party apps
from smart_selects.db_fields import ChainedForeignKey

# from commons.models import PersonType
from people.models import Person


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeManager, self).get_queryset().filter(person_type='E')


class Employee(Person):
    objects = EmployeeManager()

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'E'
        super(Employee, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )


class Department(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __unicode__(self):
        return self.name


class Position(models.Model):
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __unicode__(self):
        return self.name


class EmployeeType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Employee Type"
        verbose_name_plural = "Employee Types"
        db_table = "employees_employee_type"

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


class EmployeeAdditionalField(models.Model):
    employee = models.OneToOneField(Employee)
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
        verbose_name = "Employee Additional Field"
        verbose_name_plural = "Employee Additional Fields"
        db_table = "employees_employee_additional_fields"

    def __unicode__(self):
        return '%s %s' % (self.employee, self.hiring_date)
