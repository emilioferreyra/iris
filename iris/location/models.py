# Django core
from __future__ import absolute_import
from django.db import models


class Country(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name


class Province(models.Model):
    region = models.ForeignKey(Region, default=1)
    name = models.CharField(unique=True, max_length=100)

    def __unicode__(self):
        return self.name


class Town(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class AddressType(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Address Type"
        verbose_name_plural = "Address types"
        db_table = 'location_address_type'

    def __unicode__(self):
        return self.name
