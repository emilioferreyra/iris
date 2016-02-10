# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.db import models
# from datetime import date
# from django.utils import timezone

# Third-party apps
from smart_selects.db_fields import ChainedForeignKey
# from localflavor.us.models import PhoneNumberField

# My apps
from commons.models import PersonType
from people.models import Person, DoctorManager
from members.models import Member
# from location.models import Region, Province, Town
from suppliers.models import SupplierCompany, SupplierType


class ClinicManager(models.Manager):
    def get_queryset(self):
        clinic = 1
        return super(ClinicManager, self).\
            get_queryset().filter(supplier_type=clinic)


class Clinic(SupplierCompany):
    objects = ClinicManager()

    class Meta:
        verbose_name = "Clinic"
        verbose_name_plural = "Clinics"
        ordering = ['name']
        proxy = True

    def save(self, *args, **kwargs):
        clinic = 1
        self.supplier_type = SupplierType.objects.get(id=clinic)
        super(Clinic, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __unicode__(self):
        return self.name


class Doctor(Person):
    objects = DoctorManager()
    specialities = models.ManyToManyField(Speciality)
    clinic = models.ManyToManyField(Clinic)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

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

    doctor_name.short_description = 'Name'

    def __unicode__(self):
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
        self.person_type = PersonType.objects.get(name="Doctor")
        super(Doctor, self).save(*args, **kwargs)


class Appointment(models.Model):
    member = models.ForeignKey(Member)
    clinic = models.ForeignKey(Clinic)
    doctor = ChainedForeignKey(
        Doctor,
        chained_field="clinic",
        chained_model_field="clinic",
        )
    appointment_date = models.DateField()
    symptomatology = models.TextField(max_length=300)
    prescription = models.TextField(max_length=300, null=True, blank=True)
    date_next_appoitment = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        unique_together = (("member", "doctor", "appointment_date"),)

    def __unicode__(self):
        return '%s with %s at %s' % (self.member, self.doctor, self.clinic)


class Medicine(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def __unicode__(self):
        return self.name


class PrescribedMedicine(models.Model):
    UNIT_CHOICES = (
        ("G", "Gout"),
        ("P", "Pill"),
        ("S", "Spoon"),
    )
    FRECUENCY_UNIT_CHOICES = (
        ("H", "By Hour"),
        ("D", "By Day"),
    )
    appointment = models.ForeignKey(Appointment)
    medicine = models.ForeignKey(Medicine)
    quantity = models.FloatField(default=1)
    unit = models.CharField(max_length=1, choices=UNIT_CHOICES)
    frecuency = models.FloatField(default=1)
    frecuency_unit = models.CharField(
        max_length=1,
        choices=FRECUENCY_UNIT_CHOICES
    )

    class Meta:
        verbose_name = "Prescribed Medicine"
        verbose_name_plural = "Prescribed Medicines"
        db_table = "doctors_prescribed_medicines"

    def __unicode__(self):
        return '%s %s %s %s cada %s' % (
            self.medicine,
            self.quantity,
            self.unit,
            self.frecuency,
            self.frecuency_unit
        )
