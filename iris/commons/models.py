from django.db import models
# Third-party apps
from localflavor.us.models import PhoneNumberField
# My apps
from location.models import Nationality


class DocumentType(models.Model):
    document_type = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Documents types"
        db_table = 'commons_document_type'

    def __unicode__(self):
        return self.document_type


class MaritalStatus(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __unicode__(self):
        return self.name


class PhoneType(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']
        db_table = 'commons_phone_type'

    def __unicode__(self):
        return self.name


class Phone(models.Model):
    phone_type = models.ForeignKey(PhoneType)
    phone_number = PhoneNumberField(help_text='999-999-9999')

    class META:
        abstract = True


class AcademicLevel(models.Model):
    academic_level = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_academic_level'

    def __unicode__(self):
        return self.academic_level


class Kinship(models.Model):
    name = models.CharField(unique=True, max_length=45)

    def __unicode__(self):
        return self.name
