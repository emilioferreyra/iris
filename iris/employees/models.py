# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from smart_selects.db_fields import ChainedForeignKey

from commons.models import PersonType
from commons.models import AcademicLevel
from people.models import Person
from people.models import EmployeeManager
from people.models import EmployeeFamilyManager


# The next are Person's types variables:
employee_id = 1
employee_family_id = 5


@python_2_unicode_compatible
class EmployeeType(models.Model):
    """
        Stores employee types.
        Related to model:
        :model:`employees.Employee`.
    """
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de empleado"
        verbose_name_plural = "Tipos de empleados"
        db_table = "employees_employee_type"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Department(models.Model):
    """
        Stores the employees departments.
        Related to model:
        :model:`employees.Employee` and :model:`employees.Position`.
    """
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PositionLevel(models.Model):
    """
        Stores employees positions levels.
        Related to model:
        :model:`employees.Position`
    """
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )
    description = models.TextField(
        max_length=45,
        unique=True,
        null=True,
        verbose_name="descripción"
    )

    class Meta:
        verbose_name = "Nivel de posición"
        verbose_name_plural = "Niveles de posiciones"
        db_table = "employees_position_levels"
        ordering = ['name']

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
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="nombre"
    )
    department = models.ForeignKey(
        Department,
        verbose_name="departamento"
    )
    position_level = models.ForeignKey(
        PositionLevel,
        null=True,
        verbose_name="nivel"
    )

    class Meta:
        verbose_name = "Posición"
        verbose_name_plural = "Posiciones"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Workday(models.Model):
    """
        Stores workdays.
        Relate to model:
        :model:`employees.WorkSchedule`.
    """
    name = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Día Laborable"
        verbose_name_plural = "Días laborables"
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
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )
    start_hour = models.TimeField(verbose_name="hora inicio")
    end_hour = models.TimeField(verbose_name="hora fin")
    workdays = models.ManyToManyField(
        Workday,
        verbose_name="días laborables"
    )

    class Meta:
        verbose_name = "Calendario de Trabajo"
        verbose_name_plural = "Calendarios de Trabajos"
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
    hiring_date = models.DateField(
        verbose_name="fecha contratación",
        help_text="Ingrese la fecha de contratación"
    )
    academic_level = models.ForeignKey(
        AcademicLevel,
        verbose_name="nivel académico"
    )
    department = models.ForeignKey(
        Department,
        verbose_name="departamento"
    )
    position = ChainedForeignKey(
        Position,
        chained_field="department",
        chained_model_field="department",
        verbose_name="posición"
        )
    workSchedule = models.ForeignKey(
        WorkSchedule,
        verbose_name="calendario trabajo",
        help_text="Seleccione calendario de trabajo"
    )
    employee_type = models.ForeignKey(
        EmployeeType,
        verbose_name="tipo de empleado"
    )
    salary = models.FloatField(
        verbose_name="salario"
    )
    contract_termination_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="fecha terminación contrato",
        help_text="Introduzca la fecha de terminación del contrato"
    )

    objects = EmployeeManager()

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

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
                {'hiring_date': 'The hiring date must to be minor to today.'}
                )

    def save(self, *args, **kwargs):
        # self.person_type = PersonType.objects.get(name="Employee")
        self.person_type = employee_id
        super(Employee, self).save(*args, **kwargs)

    def years_of_work(self):
        """
        Return number of years worked by an employee.
        """
        today = date.today()
        # eaf = Employee.objects.get(id=self.id)
        eaf = get_object_or_404(Employee, id=self.id)
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
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"
        proxy = True
        app_label = "employees"

    def save(self, *args, **kwargs):
        """
        This method re-define the original save method to add a default
        value to person_type field.
        :return: Person type equal to "Employee Family" by default.
        """
        # self.person_type = PersonType.objects.get(id=5)
        self.person_type = employee_family_id
        super(EmployeeFamily, self).save(*args, **kwargs)
