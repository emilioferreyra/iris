# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import date
from django.db import models

# Third-party modules
from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField
from localflavor.us.models import PhoneNumberField

# My modules
from commons.models import MaritalStatus, DocumentType, Kinship,\
    PersonType, PhoneType
from location.models import Nationality, Country, Region, Province,\
    Town, AddressType

#  PersonType variables.
employee, member, doctor, supplier, employee_family, member_family = \
    1, 2, 3, 4, 5, 6

# Men and women variables.
men, women = "M", "F"


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeManager, self).\
            get_queryset().filter(person_type=employee)


class MemberManager(models.Manager):
    def get_queryset(self):
        return super(MemberManager, self).\
            get_queryset().filter(person_type=member)


class DoctorManager(models.Manager):
    def get_queryset(self):
        return super(DoctorManager, self).\
            get_queryset().filter(person_type=doctor)


class SupplierManager(models.Manager):
    def get_queryset(self):
        return super(SupplierManager, self).\
            get_queryset().filter(person_type=supplier)


class EmployeeFamilyManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeFamilyManager, self).\
            get_queryset().filter(person_type=employee_family)


class MemberFamilyManager(models.Manager):
    def get_queryset(self):
        return super(MemberFamilyManager, self).\
            get_queryset().filter(person_type=member_family)


class MaleManager(models.Manager):
    def get_query_set(self):
        return super(MaleManager, self).get_query_set().filter(gender=men)


class FemaleManager(models.Manager):
    def get_query_set(self):
        return super(FemaleManager, self).get_query_set().filter(gender=women)


class Person(TimeStampedModel, AuthStampedModel):
    names = models.CharField(max_length=100)
    father_last_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=(('M', 'Male'), ('F', 'Female'),),
        null=True
    )
    birth_day = models.DateField()
    nationality = models.ForeignKey(Nationality, default=21)
    marital_status = models.ForeignKey(MaritalStatus)
    document_type = models.ForeignKey(DocumentType, null=True)
    document_id = models.CharField(
        max_length=22,
        help_text='000-0000000-0',
        null=True
    )
    email = models.EmailField(blank=True)
    person_type = models.ForeignKey(PersonType, null=True)
    dependent_of = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='supervisor'
        )
    kinship = models.ForeignKey(Kinship, null=True)
    picture = ImageField(upload_to='people_pictures', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='active')
    people = models.Manager()
    employees = EmployeeManager()
    members = MemberManager()
    doctors = DoctorManager()
    suppliers = SupplierManager()
    employee_families = EmployeeFamilyManager()
    member_families = MemberFamilyManager()
    men = MaleManager()
    women = FemaleManager()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def full_name(self):
        return "%s %s %s" % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )
    full_name.short_description = "Name"
    # full_name.admin_order_field = "name"

    def calculate_age(self):
        today = date.today()
        return today.year - self.birth_day.year - (
            (today.month, today.day) <
            (self.birth_day.month, self.birth_day.day)
        )
    calculate_age.short_description = "Age"
    # calculate_age.admin_order_field = "age"

    def main_address(self):
        address = PersonAddress.objects.filter(
            person_name_id=self.id,
            default=True
            ).order_by('id').first()
        if address:
            return address
        else:
            address = PersonAddress.objects.filter(
                person_name_id=self.id
                ).order_by('id').first()
            return address

    main_address.short_description = "Address"

    def main_phone(self):
        phone = PersonPhone.objects.filter(
            person_name_id=self.id,
            default=True
            ).order_by('id').first()
        if phone:
            return phone
        else:
            phone = PersonPhone.objects.filter(
                person_name_id=self.id
                ).order_by('id').first()
            return phone

    main_phone.short_description = "Phone"

    def __unicode__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )

    def image_tag(self):
        return u'<img src="%s" />' % self.picture.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class PersonAddress(models.Model):
    person_name = models.ForeignKey(Person)
    country = models.ForeignKey(Country, default=1)
    region = models.ForeignKey(Region)
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
    address_type = models.ForeignKey(AddressType)
    building = models.CharField(max_length=20, null=True, blank=True)
    apartment = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=40)
    default = models.BooleanField(
        default=False,
        verbose_name='Default Address'
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "people_person_address"

    def __unicode__(self):
        return '%s %s %s' % (self.building, self.apartment, self.street)


class PersonPhone(models.Model):
    phone_type = models.ForeignKey(PhoneType)
    phone_number = PhoneNumberField(help_text='999-999-9999')
    person_name = models.ForeignKey(Person)
    default = models.BooleanField(
        default=False,
        verbose_name='default phone'
        )

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        db_table = "people_person_phone"
        unique_together = (("person_name", "phone_type"),)

    def __unicode__(self):
        return self.phone_number
