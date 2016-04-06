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
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Documents types"
        db_table = 'commons_document_type'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MaritalStatus(models.Model):
    """
        Stores the marital status related to :model:`people.Person`
    """
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PhoneType(models.Model):
    """
        Stores the phones types related to :model:`people.Person`
    """
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']
        db_table = 'commons_phone_type'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AcademicLevel(models.Model):
    """
        Stores the academics levels related to :model:`people.Person`
    """
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_academic_level'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Kinship(models.Model):
    """
        Stores the kinship related to :model:`people.Person`
    """
    name = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PersonType(models.Model):
    """
        Stores the person types related to :model:`people.Person`
    """
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Person Type"
        verbose_name_plural = "Person Types"
        db_table = "commons_person_type"
        ordering = ['id']

    def __str__(self):
        return self.name
