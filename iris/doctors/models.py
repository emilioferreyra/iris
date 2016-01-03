# Django cores
from __future__ import absolute_import
from django.db import models
# My apps
from commons.models import ContactInfo, AcademicLevel, Phone
from location.models import Address


class MedicalSpeciality(models.Model):
    speciality_name = models.CharField(max_length=40)

    class Meta:
        db_table = "doctors_medical_speciality"
        verbose_name = "Medical speciality"
        verbose_name_plural = "Medical specialities"

    def __unicode__(self):
        return self.speciality_name


class Doctor(ContactInfo):
    speciality_name = models.ManyToManyField(MedicalSpeciality)
    academic_level = models.ForeignKey(AcademicLevel)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __unicode__(self):
        return '%s %s %s' % (self.names, self.father_name, self.mother_name)


class Address(Address):
    doctor = models.ForeignKey(Doctor)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addreses"


class DoctorPhones(Phone):
    doctor = models.ForeignKey(Doctor)

    class Meta:
        db_table = 'doctors_phone'
        verbose_name = 'Doctor phone'
        verbose_name_plural = 'Doctor phones'

    def __unicode__(self):
        return '%s %s %s %s' % (
            self.names,
            self.father_name,
            self.mother_name,
            self.phone_number
            )
