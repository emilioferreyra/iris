from django.db import models
from localflavor.us.models import PhoneNumberField


class DocumentType(models.Model):
    document_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"
        db_table = 'commons_document_type'

    def __unicode__(self):
        return self.document_type


class ContactInfo(models.Model):
    names = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    active = models.BooleanField(default=True)

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


class Phone(models.Model):
    phone_number = PhoneNumberField()
    phone_type = models.ForeignKey(PhoneType)

    def __unicode__(self):
        return self.phone
