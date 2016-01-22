# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.db import models

# Third-party apps
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from localflavor.us.models import PhoneNumberField

# My apps
from people.models import Person
from members.models import Member
from location.models import Region, Province, Town


class DoctorManager(models.Manager):
    def get_queryset(self):
        return super(DoctorManager, self).get_queryset().filter(person_type='D')


class Doctor(Person):
    objects = DoctorManager()

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'D'
        super(Doctor, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Dr. %s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )


class Clinic(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, null=True, default=1)
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region"
        )
    town = ChainedForeignKey(
        Town,
        chained_field="province",
        chained_model_field="province"
        )
    address = models.TextField(max_length=150, null=True, blank=True)
    phone_number = PhoneNumberField(
        help_text='999-999-9999',
        null=True,
        blank=True
        )

    class Meta:
        verbose_name = "Clinic"
        verbose_name_plural = "Clinics"
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __unicode__(self):
        return self.name


class DoctorAdditionalField(models.Model):
    doctor = models.OneToOneField(Doctor)
    specialities = models.ManyToManyField(Speciality)
    clinic = models.ManyToManyField(Clinic)

    class Meta:
        verbose_name = "Doctor Additional Field"
        verbose_name_plural = "Doctor Additional Fields"
        db_table = "doctors_doctor_additional_fields"

    def __unicode__(self):
        return '%s' % (self.doctor)


class Appointment(models.Model):
    member = models.ForeignKey(Member)
    clinic = models.ForeignKey(Clinic)
    # doctor = models.ForeignKey(Doctor)
    doctor = ChainedForeignKey(
        DoctorAdditionalField,
        chained_field="clinic",
        chained_model_field="clinic",
        )
    date = models.DateField()
    symptomatology = models.TextField(max_length=300)
    prescription = models.TextField(max_length=300, null=True, blank=True)
    date_next_appoitment = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

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
