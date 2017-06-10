# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Country(models.Model):
    """
    Stores the countries related to :model:`people.PersonAddress`
    and :model:`suppliers.SupplierCompany`.
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Paises"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Nationality(models.Model):
    """
    Stores the nationalities related to :model:`people.Person`.
    """
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Region(models.Model):
    """
    Stores the regions related to :model:`people.PersonAddress`,
    :model:`location.Province` and :model:`suppliers.SupplierCompany`.
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Province(models.Model):
    """
    Stores the privinces related to :model:`people.PersonAddress`,
    :model:`location.Region`, :model:`suppliers.SupplierCompany`
    and :model:`location.Town`.
    """
    region = models.ForeignKey(
        Region,
        default=1,
        verbose_name="region"
    )
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Town(models.Model):
    """
    Stores the privinces related to :model:`people.PersonAddress`,
    :model:`location.Province`,:model:`suppliers.SupplierCompany`.
    """
    province = models.ForeignKey(
        Province,
        verbose_name="provincia"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Location(models.Model):
    """
    Stores the location related to :model: `people.PersonAddress`,
    :model:`location.Town`, :model:`suppliers.SupplierCompany`.
    """
    name = models.CharField(max_length=100, verbose_name="nombre", unique=True)
    town = models.ForeignKey(Town, default=203, verbose_name="municipio")

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AddressType(models.Model):
    """
    Stores the address types related to :model:`people.PersonAddress`.
    """
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de dirección"
        verbose_name_plural = "Tipo de direcciones"
        db_table = 'location_address_type'
        ordering = ['id']

    def __str__(self):
        return self.name
