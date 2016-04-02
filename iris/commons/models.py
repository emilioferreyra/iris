# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Third-party apps
# from localflavor.us.models import PhoneNumberField


@python_2_unicode_compatible
class DocumentType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Documents types"
        db_table = 'commons_document_type'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MaritalStatus(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PhoneType(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']
        db_table = 'commons_phone_type'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AcademicLevel(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_academic_level'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Kinship(models.Model):
    name = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PersonType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Person Type"
        verbose_name_plural = "Person Types"
        db_table = "commons_person_type"
        ordering = ['id']

    def __str__(self):
        return self.name
