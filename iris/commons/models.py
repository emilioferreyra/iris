# -*- coding: utf-8 -*-
"""
    commons app:
    This app contain the models used by other apps like complement
    information.
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class DocumentType(models.Model):
    """
        Stores all types of documents id for identify a person,
        related to :model:`people.Person`.
    """
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"
        db_table = 'commons_document_type'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MaritalStatus(models.Model):
    """
        Stores the marital status related to :model:`people.Person`
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = 'Estado civil'
        verbose_name_plural = 'Estado civil'
        db_table = 'commons_marital_status'
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PhoneType(models.Model):
    """
        Stores the phones types related to :model:`people.Person`
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de teléfono"
        verbose_name_plural = "Tipos de teléfonos"
        db_table = 'commons_phone_type'
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AcademicLevel(models.Model):
    """
        Stores the academics levels related to :model:`people.Person`
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Nivel académico"
        verbose_name_plural = "Niveles académicos"
        db_table = 'commons_academic_level'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Kinship(models.Model):
    """
        Stores the kinship related to :model:`people.Person`
    """
    name = models.CharField(
        unique=True,
        max_length=45,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Parentezco"
        verbose_name_plural = "Parentezcos"
        ordering = ["name"]

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PersonType(models.Model):
    """
        Stores the person types related to :model:`people.Person`
    """
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de persona"
        verbose_name_plural = "Tipos de personas"
        db_table = "commons_person_type"
        ordering = ['id']

    def __str__(self):
        return self.name
