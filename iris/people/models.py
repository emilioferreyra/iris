# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# from datetime import date
from django.db import models

# Third-party modules
from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel
from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField

# My modules
from commons.models import MaritalStatus, DocumentType, Phone, Kinship
from location.models import \
    Nationality, Country, Region, Province, Town, AddressType


class Person(TimeStampedModel, AuthStampedModel):
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
    father_last_name = models.CharField(max_length=50)
    mother_last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
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
    person_type = models.CharField(
        max_length=1,
        choices=PERSON_TYPE_CHOICE,
        null=True
    )
    # dependent = models.BooleanField(default=False)
    parent_of = models.ForeignKey('self', null=True, blank=True)
    kinship = models.ForeignKey(Kinship, null=True)
    picture = ImageField(upload_to='people_pictures', null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['id']

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


class Kinsman(Person):

    class Meta:
        verbose_name = "Kinsman"
        verbose_name_plural = "Kinsmans"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'K'
        super(Kinsman, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )


class PersonAddress(models.Model):
    person_name = models.ForeignKey(Person)
    country = models.ForeignKey(Country, default=1)
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
        verbose_name_plural = "Addreses"
        db_table = "people_person_address"

    def __unicode__(self):
        return '%s %s %s' % (self.building, self.apartment, self.street)


class PersonPhone(Phone):
    person_name = models.ForeignKey(Person)
    default = models.BooleanField(
        default=False,
        verbose_name='default phone'
        )

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        db_table = "people_person_phone"

    def __unicode__(self):
        return '%s %s' % (self.person_name, self.phone_number)
