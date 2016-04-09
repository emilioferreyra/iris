# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from datetime import date
from django.db import models

from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField
from localflavor.us.models import PhoneNumberField

from commons.models import MaritalStatus
from commons.models import DocumentType
from commons.models import Kinship
from commons.models import PersonType
from commons.models import PhoneType
from location.models import Nationality
from location.models import Country
from location.models import Region
from location.models import Province
from location.models import Town
from location.models import AddressType

#  PersonType variables.
d = dict(
    employee=1,
    member=2,
    doctor=3,
    supplier=4,
    employee_family=5,
    member_family=6
    )

# Men and women variables.
men, women = "M", "F"


class EmployeeManager(models.Manager):
    """
         Manage Employees query set to only return
         person type = employee
    """
    def get_queryset(self):
        return super(EmployeeManager, self).\
            get_queryset().filter(person_type=d['employee'])


class MemberManager(models.Manager):
    """
         Manage Members query set to only return
         person type = member
    """
    def get_queryset(self):
        return super(MemberManager, self).\
            get_queryset().filter(person_type=d['member'])


class DoctorManager(models.Manager):
    """
         Manage Doctors query set to only return
         person type = doctor
    """
    def get_queryset(self):
        return super(DoctorManager, self).\
            get_queryset().filter(person_type=d['doctor'])


class SupplierManager(models.Manager):
    """
         Manage Suppliers query set to only return
         person type = supplier
    """
    def get_queryset(self):
        return super(SupplierManager, self).\
            get_queryset().filter(person_type=d['supplier'])


class EmployeeFamilyManager(models.Manager):
    """
         Manage Employee Family query set to only return
         person type = employee_family
    """
    def get_queryset(self):
        return super(EmployeeFamilyManager, self).\
            get_queryset().filter(person_type=d['employee_family'])


class MemberFamilyManager(models.Manager):
    """
         Manage Member Family query set to only return
         person type = member_family
    """
    def get_queryset(self):
        return super(MemberFamilyManager, self).\
            get_queryset().filter(person_type=d['member_family'])


class MaleManager(models.Manager):
    """
         Manage Male query set to only return
         gender = men
    """
    def get_query_set(self):
        return super(MaleManager, self).get_query_set().filter(gender=men)


class FemaleManager(models.Manager):
    """
         Manage Female query set to only return
         gender = women
    """
    def get_query_set(self):
        return super(FemaleManager, self).get_query_set().filter(gender=women)


@python_2_unicode_compatible
class Person(TimeStampedModel, AuthStampedModel):
    """
        Stores person information. Related objects:
        :model:`auth.User`, :model:`people.Person`,
        :model:`doctors.Doctor`, :model:`commons.DocumentType`,
        :model:`employees.Employee`, :model:`commons.Kinship`,
        :model:`commons.MaritalStatus`, :model:`members.Member`,
        :model:`location.Nationality`, :model:`people.Person`,
        :model:`commons.PersonType`, :model:`people.PersonAddress`,
        :model:`people.PersonPhone`, :model:`people.PersonPhone` and
        :model:`suppliers.SupplierContact`.
    """
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
    email = models.EmailField(verbose_name="e-mail", blank=True)
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
    # employees = EmployeeQuerySet.as_manager()
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
        """
            Returns person's full name.
        """
        return "%s %s %s" % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )
    full_name.short_description = "Name"
    full_name.admin_order_field = "names"

    def calculate_age(self):
        """
            Returns person's age.
        """
        today = date.today()
        return today.year - self.birth_day.year - (
            (today.month, today.day) <
            (self.birth_day.month, self.birth_day.day)
        )
    calculate_age.short_description = "Age"
    # Use birth_day field to order in Admin site:
    calculate_age.admin_order_field = "-birth_day"

    def main_address(self):
        """
            Returns person's main address.
            If one or more addresses are marked as default,
            returns the first address that was added.
        """
        address = PersonAddress.objects.filter(
            person_name_id=self.id,
            is_default=True
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
        """
            Returns person's main phone.
            If one or more phones are marked as default,
            returns the first phone that was added.
        """
        phone = PersonPhone.objects.filter(
            person_name_id=self.id,
            is_default=True
            ).order_by('id').first()
        if phone:
            return phone
        else:
            phone = PersonPhone.objects.filter(
                person_name_id=self.id
                ).order_by('id').first()
            return phone

    main_phone.short_description = "Phone"

    def __str__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )

    def image_tag(self):
        return u'<img src="%s" />' % self.picture.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


@python_2_unicode_compatible
class PersonAddress(models.Model):
    """
        Store person's address.

    """
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
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
    # The next field its used to mark the address as default.
    is_default = models.BooleanField(
        default=False,
        verbose_name='Default Address',
        # choices=BOOL_CHOICES,
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "people_person_address"

    def __str__(self):
        return '%s %s %s' % (self.building, self.apartment, self.street)


@python_2_unicode_compatible
class PersonPhone(models.Model):
    """
        Store person's phones.
        Related models:
        :model:`people.Person` and :model:`commons.PhoneType`
    """
    phone_type = models.ForeignKey(PhoneType)
    phone_number = PhoneNumberField(help_text='999-999-9999')
    person_name = models.ForeignKey(Person)
    is_default = models.BooleanField(
        default=False,
        verbose_name='default phone'
        )

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        db_table = "people_person_phone"
        unique_together = (("person_name", "phone_type"),)

    def __str__(self):
        return self.phone_number
