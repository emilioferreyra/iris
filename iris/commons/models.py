from django.db import models


class DocumentType(models.Model):
    document_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Documents types"
        db_table = 'commons_document_type'

    def __unicode__(self):
        return self.document_type


class ContactInfo(models.Model):
    names = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    class META:
        abstract = True
        db_table = 'commons_contact_info'


class PhoneType(models.Model):
    phone_type = models.CharField(unique=True, max_length=45)

    class Meta:
        ordering = ['id']
        db_table = 'commons_phone_type'

    def __unicode__(self):
        return self.phone_type


class AcademicLevel(models.Model):
    academic_level = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_academic_level'

    def __unicode__(self):
        return self.academic_level


class MaritalStatus(models.Model):
    marital_status = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'commons_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __unicode__(self):
        return self.marital_status


class Kinship(models.Model):
    kinship = models.CharField(unique=True, max_length=45)

    def __unicode__(self):
        return self.kinship
