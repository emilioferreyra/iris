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
from location.models import Location
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
        return super(MaleManager, self).get_query_set().filter(gender=women)


class FemaleManager(models.Manager):
    """
    Manage Female query set to only return
    gender = women
    """
    def get_query_set(self):
        return super(FemaleManager, self).get_query_set().filter(gender=men)


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
    names = models.CharField(
        verbose_name="nombres",
        max_length=100)
    father_last_name = models.CharField(
        max_length=50,
        verbose_name="Primer Apellido",
    )
    mother_last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Segundo Apellido",
    )
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', "Masculino"),
            ('F', "Femenino"),
        ),
        null=True,
        verbose_name="género",
        help_text='Seleccione género',
    )
    birthday = models.DateField(
        verbose_name="Fecha nacimiento",
        help_text="Introduzca Fecha de nacimiento",
        null=True,
        blank=True
    )
    nationality = models.ForeignKey(
        Nationality,
        default=21,
        verbose_name="nacionalidad",
        help_text="Seleccione nacionalidad"
    )
    marital_status = models.ForeignKey(
        MaritalStatus,
        verbose_name="estado civil",
        help_text="Seleccione estado civil",
        null=True,
        blank=True
    )
    document_type = models.ForeignKey(
        DocumentType,
        null=True,
        blank=True,
        verbose_name="tipo documento identidad",
        help_text="Seleccione el tipo de documento de identidad"
    )
    document_id = models.CharField(
        max_length=22,
        null=True,
        blank=True,
        verbose_name="documento identidad",
        help_text="Introduzca el número de documento"
    )
    email = models.EmailField(blank=True, verbose_name="e-mail")
    person_type = models.ForeignKey(
        PersonType,
        null=True,
        verbose_name="tipo de persona",
        help_text="Seleccione tipo de persona"
    )
    dependent_of = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name="supervisor"
    )
    kinship = models.ForeignKey(
        Kinship,
        null=True,
        verbose_name="parentezco",
        help_text="Seleccione parentezco"
    )
    picture = ImageField(
        upload_to='people_pictures',
        null=True,
        blank=True,
        # verbose_name="foto",
    )
    status = models.BooleanField(
        default=True,
        verbose_name="estado"
    )
    age = models.PositiveIntegerField(
        verbose_name='Edad',
        null=True
    )

    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
    employees = EmployeeManager()
    members = MemberManager()
    doctors = DoctorManager()
    suppliers = SupplierManager()
    employee_families = EmployeeFamilyManager()
    member_families = MemberFamilyManager()

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return '{} {} {}'.format(
            self.names,
            self.father_last_name,
            self.mother_last_name
        )

    def full_name(self):
        """
        Returns person's full name.
        """
        return "{} {} {}".format(
            self.names,
            self.father_last_name,
            self.mother_last_name
        )
    full_name.short_description = "Nombre"
    full_name.admin_order_field = "names"

    def calculate_age(self):
        """
            Returns person's age.
        """
        today = date.today()
        person = Person.people.filter(id=self.id)
        if self.birthday:
            age_calculated = today.year - self.birthday.year - (
                (today.month, today.day) <
                (self.birthday.month, self.birthday.day)
            )
            person.update(age=age_calculated)
        else:
            age_calculated = None
        return age_calculated
    calculate_age.short_description = "Edad"
    # Use birthday field to order in Admin site:
    calculate_age.admin_order_field = "-birthday"

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

    main_address.short_description = "Dirección"

    def get_location(self):
        """
        Returns person's town.
        If one or more addresses are marked as default,
        returns the first address that was added.
        """
        address = PersonAddress.objects.filter(
            person_name_id=self.id,
            is_default=True
        ).order_by('id').first()
        if address:
            return address.location
        else:
            address = PersonAddress.objects.filter(
                person_name_id=self.id
            ).order_by('id').first()
            return address.location

    get_location.short_description = "Localidad"

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

    main_phone.short_description = "Teléfono"

    def image_tag(self):
        if self.picture:
            return u'<img src="%s" width="100" height="75" />' \
                % self.picture.url
        else:
            return ' '
    image_tag.short_description = 'Foto'
    image_tag.allow_tags = True
    image_tag.admin_order_field = 'names'


@python_2_unicode_compatible
class PersonAddress(models.Model):
    """
        Store person's address.
        Related models:
        :model:`people.Person` and :model:`commons.AddressType`
    """
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    person_name = models.ForeignKey(Person)
    country = models.ForeignKey(
        Country,
        default=1,
        verbose_name="país",
        help_text="Seleccione país"
    )
    region = models.ForeignKey(
        Region,
        verbose_name="región",
        help_text="Seleccione región",
        default=1
    )
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region",
        verbose_name="provincia",
        help_text="Seleccione provincia",
        default=29
    )
    town = ChainedForeignKey(
        Town,
        chained_field="province",
        chained_model_field="province",
        verbose_name="municipio",
        help_text="Seleccione municipio",
        default=203
    )
    location = ChainedForeignKey(
        Location,
        chained_field="town",
        chained_model_field="town",
        verbose_name="localidad",
        help_text="Seleccione Localidad", null=True
    )
    address_type = models.ForeignKey(
        AddressType,
        verbose_name="tipo dirección",
        help_text="Seleccione tipo de dirección",
        default=1
    )
    building = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="edificio"
    )
    apartment = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="apartamento",
        help_text="Escriba número de apartamento"
    )
    street = models.CharField(
        max_length=40,
        verbose_name="calle",
        help_text="Escriba nombre de calle"
    )
    # The next field its used to mark the address as default.
    is_default = models.BooleanField(
        default=False,
        verbose_name='dirección principal',
        # choices=BOOL_CHOICES,
    )

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
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
    phone_type = models.ForeignKey(
        PhoneType,
        verbose_name="tipo de teléfono"
    )
    phone_number = PhoneNumberField(
        verbose_name="número de teléfono",
        help_text='999-999-9999'
    )
    person_name = models.ForeignKey(Person)
    is_default = models.BooleanField(
        default=False,
        verbose_name='teléfono principal'
    )

    class Meta:
        verbose_name = "Teléfono"
        verbose_name_plural = "Teléfonos"
        db_table = "people_person_phone"
        unique_together = (("person_name", "phone_type"),)

    def __str__(self):
        return self.phone_number
