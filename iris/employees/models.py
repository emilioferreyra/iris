# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedForeignKey

from commons.models import PersonType, AcademicLevel
from people.models import Person, EmployeeManager, EmployeeFamilyManager


@python_2_unicode_compatible
class EmployeeType(models.Model):
    """
        Stores employee types.
        Related to model:
        :model:`employees.Employee`.
    """
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Employee Type"
        verbose_name_plural = "Employee Types"
        db_table = "employees_employee_type"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Department(models.Model):
    """
        Stores the employees departments.
        Related to model:
        :model:`employees.Employee` and :model:`employees.Position`.
    """
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PositionLevel(models.Model):
    """
        Stores employees positions levels.
        Related to model:
        :model:`employees.Position`
    """
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=45, unique=True, null=True)

    class Meta:
        verbose_name = "Position Level"
        verbose_name_plural = "Position Levels"
        db_table = "employees_position_levels"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Position(models.Model):
    """
        Stores employees positions.
        Relate to model:
        :model:`employees.Department`,
        :model:`employees.Employee` and
        :model:`employees.PositionLevel`.
    """
    department = models.ForeignKey(Department)
    position_level = models.ForeignKey(PositionLevel, null=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Workday(models.Model):
    """
        Stores workdays.
        Relate to model:
        :model:`employees.WorkSchedule`.
    """
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Workday"
        verbose_name_plural = "Workdays"
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class WorkSchedule(models.Model):
    """
        Stores WorkSchedule.
        Related to model:
        :model:`employees.Employee` and
        :model:`employees.Workday`.
    """
    name = models.CharField(max_length=45, unique=True)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    workdays = models.ManyToManyField(Workday)

    class Meta:
        verbose_name = "Work Schedule"
        verbose_name_plural = "Work Schedules"
        db_table = "employees_work_schedule"

    def __str__(self):
        return self.name


class Employee(Person):
    """
        Stores employees information.
        Relate to models:
        :model:`commons.AcademicLevel`,
        :model:`auth.User`,
        :model:`employees.Department`,
        :model:`people.Person`,
        :model:`commons.DocumentType`,
        :model:`employees.EmployeeType`,
        :model:`commons.Kinship`,
        :model:`commons.MaritalStatus`,
        :model:`location.Nationality`,
        :model:`commons.PersonType`,
        :model:`people.PersonAddress`,
        :model:`people.PersonPhone`,
        :model:`employees.Position` and
        :model:`employees.WorkSchedule`.
    """
    objects = EmployeeManager()

    hiring_date = models.DateField()
    academic_level = models.ForeignKey(AcademicLevel)
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
        """
        If employee age its lest then 18 years
        returns the message: Must be at least 18 years old to register.
        """
        dob = self.birth_day
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (
                today.year, today.month, today.day):
            raise ValidationError(
                {'birth_day': _('Must be at least 18 years old to register.')})
        if self.hiring_date <= today:
            raise ValidationError(
                {'hiring_date': _('The hiring date must to be minor or equal \
                    to today.')})

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Employee")
        super(Employee, self).save(*args, **kwargs)

    def years_of_work(self):
        """
        Return number of years worked by an employee.
        """
        today = date.today()
        eaf = Employee.objects.get(id=self.id)
        return today.year - eaf.hiring_date.year - (
            (today.month, today.day) <
            (eaf.hiring_date.month, eaf.hiring_date.day)
        )
    years_of_work.short_description = "Years of work"
    # Use the hiring date to ordering on Admin site.
    years_of_work.admin_order_field = "-hiring_date"


class EmployeeFamily(Person):
    """
        Stores the employees families.
        Related models:
        :model:`auth.User`,
        :model:`people.Person`,
        :model:`commons.DocumentType`,
        :model:`commons.Kinship`,
        :model:`commons.MaritalStatus`,
        :model:`location.Nationality`,
        :model:`commons.PersonType`,
        :model:`people.PersonAddress` and
        :model:`people.PersonPhone`.
    """
    objects = EmployeeFamilyManager()

    class Meta:
        verbose_name = "Employee Family"
        verbose_name_plural = "Employee Families"
        proxy = True
        app_label = "employees"

    def save(self, *args, **kwargs):
        """
        This method re-define the original save method to add a default
        value to person_type field.
        :return: Person type equal to "Employee Family" by default.
        """
        self.person_type = PersonType.objects.get(id=5)
        super(EmployeeFamily, self).save(*args, **kwargs)
