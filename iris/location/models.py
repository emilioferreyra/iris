# Django core
from __future__ import absolute_import
from django.db import models
# Third-party modules
from smart_selects.db_fields import ChainedForeignKey


class Country(models.Model):
    country_name = models.CharField(unique=True, max_length=45)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return self.country_name


class Nationality(models.Model):
    nationality = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"

    def __unicode__(self):
        return self.nationality


class Region(models.Model):
    region_name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.region_name


class Province(models.Model):
    province_name = models.CharField(unique=True, max_length=100)
    region_name = models.ForeignKey(Region, default=1)

    def __unicode__(self):
        return self.province_name


class Town(models.Model):
    town_name = models.CharField(max_length=100)
    province_name = models.ForeignKey(Province, default=1)

    class Meta:
        ordering = ['town_name']

    def __unicode__(self):
        return self.town_name


class AddressType(models.Model):
    address_type = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Address Type"
        verbose_name_plural = "Address types"
        db_table = 'location_address_type'

    def __unicode__(self):
        return self.address_type


class Address(models.Model):
    building = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20)
    street_name = models.CharField(max_length=40)
    country_name = models.ForeignKey(Country)
    region_name = models.ForeignKey(Region)
    # province_name = models.ForeignKey(Province)
    province_name = ChainedForeignKey(
        Province,
        chained_field="region_name",
        chained_model_field="region_name"
        )
    # town_name = models.ForeignKey(Town)
    town_name = ChainedForeignKey(
        Town,
        chained_field="province_name",
        chained_model_field="province_name"
        )
    address_type = models.ForeignKey(AddressType, null=True)

    class Meta:
        abstract = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __unicode__(self):
        return '%s %s %s' % (self.building, self.apartment, self.street_name)
