# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.shortcuts import get_object_or_404

from smart_selects.db_fields import ChainedForeignKey

from commons.models import PersonType
from people.models import Person, DoctorManager
from members.models import Member
from suppliers.models import SupplierCompany
from suppliers.models import SupplierType


class ClinicManager(models.Manager):
    def get_queryset(self):
        clinic = 1
        return super(ClinicManager, self).\
            get_queryset().filter(supplier_type=clinic)


@python_2_unicode_compatible
class Clinic(SupplierCompany):
    objects = ClinicManager()

    class Meta:
        verbose_name = "Clínica"
        verbose_name_plural = "Clínicas"
        ordering = ['name']
        proxy = True

    def save(self, *args, **kwargs):
        clinic = 1
        self.supplier_type = SupplierType.objects.get(id=clinic)
        super(Clinic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Speciality(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Doctor(Person):
    specialities = models.ManyToManyField(
        Speciality,
        verbose_name="especialidades"
    )
    clinic = models.ManyToManyField(
        Clinic,
        verbose_name="clínicas"
    )

    objects = DoctorManager()

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def doctor_name(self):
        if self.gender == 'F':
            return "Dra. %s %s %s" % (
                self.names,
                self.father_last_name,
                self.mother_last_name
                )
        else:
            return "Dr. %s %s %s" % (
                self.names,
                self.father_last_name,
                self.mother_last_name
                )

    doctor_name.short_description = 'Nombre'

    def __str__(self):
        if self.gender == 'F':
            return "Dra. %s %s %s" % (
                self.names,
                self.father_last_name,
                self.mother_last_name
                )
        else:
            return "Dr. %s %s %s" % (
                self.names,
                self.father_last_name,
                self.mother_last_name
                )

    def save(self, *args, **kwargs):
        # self.person_type = PersonType.objects.get(name="Doctor")
        self.person_type = get_object_or_404(PersonType, name="Doctor")
        super(Doctor, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Appointment(models.Model):
    member = models.ForeignKey(
        Member,
        verbose_name="miembro"
    )
    clinic = models.ForeignKey(
        Clinic,
        verbose_name="clínica"
    )
    doctor = ChainedForeignKey(
        Doctor,
        chained_field="clinic",
        chained_model_field="clinic",
        )
    appointment_date = models.DateField(
        verbose_name="fecha de cita"
    )
    symptomatology = models.TextField(
        max_length=300,
        verbose_name="sintomatología"
    )
    prescription = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="prescripción"
    )
    date_next_appoitment = models.DateField(
        null=True,
        blank=True,
        verbose_name="fecha de próxima cita"
    )

    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
        unique_together = (("member", "doctor", "appointment_date"),)

    def __str__(self):
        return '%s con %s en %s' % (
            self.member,
            self.doctor,
            self.clinic
        )


@python_2_unicode_compatible
class Medicine(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Medicina"
        verbose_name_plural = "Medicinas"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PrescribedMedicine(models.Model):
    UNIT_CHOICES = (
        ("G", "Gotas"),
        ("P", "Pildoras"),
        ("S", "Cucharada"),
    )
    FRECUENCY_UNIT_CHOICES = (
        ("H", "Cada Hora"),
        ("D", "Al Día"),
    )
    appointment = models.ForeignKey(Appointment)
    medicine = models.ForeignKey(
        Medicine,
        verbose_name="medicamento"
    )
    quantity = models.FloatField(
        default=1,
        verbose_name="cantidad"
    )
    unit = models.CharField(
        max_length=1,
        choices=UNIT_CHOICES,
        verbose_name="unidad"
    )
    frecuency = models.FloatField(
        default=1,
        verbose_name="frecuencia"
    )
    frecuency_unit = models.CharField(
        max_length=1,
        choices=FRECUENCY_UNIT_CHOICES,
        verbose_name="unidade de frecuencia"
    )

    class Meta:
        verbose_name = "Medicina prescrita"
        verbose_name_plural = "Medicinas prescritas"
        db_table = "doctors_prescribed_medicines"

    def __str__(self):
        return '%s %s %s %s cada %s' % (
            self.medicine,
            self.quantity,
            self.unit,
            self.frecuency,
            self.frecuency_unit
        )
