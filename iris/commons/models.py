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
    marital_status = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __unicode__(self):
        return self.marital_status


class ContactInfo(models.Model):
    names = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    marital_status = models.ForeignKey(MaritalStatus)
    document_type = models.ForeignKey(DocumentType)
    document_id = models.CharField(max_length=22)
    nationality = models.ForeignKey(Nationality)
    active = models.BooleanField(default=True)

    class META:
        abstract = True


class PhoneType(models.Model):
    phone_type = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']
        db_table = 'commons_phone_type'

    def __unicode__(self):
        return self.phone_type


class Phone(models.Model):
    phone_number = PhoneNumberField()
    phone_type = models.ForeignKey(PhoneType)

    class META:
        abstract = True


class AcademicLevel(models.Model):
    academic_level = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_academic_level'

    def __unicode__(self):
        return self.academic_level


class Kinship(models.Model):
    kinship = models.CharField(unique=True, max_length=45)

    def __unicode__(self):
        return self.kinship
