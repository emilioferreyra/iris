# -*- coding: utf-8 -*-
#  Django core
from __future__ import absolute_import, unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Nationality(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Province(models.Model):
    region = models.ForeignKey(Region, default=1)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Town(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AddressType(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Address Type"
        verbose_name_plural = "Address types"
        db_table = 'location_address_type'

    def __str__(self):
        return self.name
