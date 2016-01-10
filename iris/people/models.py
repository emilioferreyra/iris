from django.db import models
# Third-party modules
from smart_selects.db_fields import ChainedForeignKey
# My modules
from commons.models import MaritalStatus, DocumentType, Phone
from location.models import \
    Nationality, Country, Region, Province, Town, AddressType


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    PERSON_TYPE_CHOICE = (
        ('E', 'Employee'),
        ('M', 'Member'),
        ('D', 'Doctor'),
        ('S', 'Supplier'),
        ('K', 'Kinsman'),
    )

    names = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_day = models.DateField()
    nationality = models.ForeignKey(Nationality)
    marital_status = models.ForeignKey(MaritalStatus)
    document_type = models.ForeignKey(DocumentType)
    document_id = models.CharField(max_length=22, help_text='000-0000000-0')
    email = models.EmailField(blank=True)
    person_type = models.CharField(
        max_length=1,
        choices=PERSON_TYPE_CHOICE,
        null=True
    )
    dependent = models.BooleanField(default=False)
    parent_of = models.ForeignKey('self', null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        ordering = ['id']

    def __unicode__(self):
        return '%s %s %s' % (self.names, self.father_name, self.mother_name)


class PersonAddress(models.Model):
    person_name = models.ForeignKey(Person)
    address_type = models.ForeignKey(AddressType)
    building = models.CharField(max_length=20, null=True, blank=True)
    apartment = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=40)
    country = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    # province_name = models.ForeignKey(Province)
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region"
        )
    # town_name = models.ForeignKey(Town)
    town = ChainedForeignKey(
        Town,
        chained_field="province",
        chained_model_field="province"
        )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addreses"
        db_table = "people_person_address"

    def __unicode__(self):
        return '%s %s %s' % (self.building, self.apartment, self.street)


class PersonPhone(Phone):
    person_name = models.ForeignKey(Person)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        db_table = "people_person_phone"

    def __unicode__(self):
        return '%s %s' % (self.person_name, self.phone_number)
