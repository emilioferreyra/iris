# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models

# Third-party modules
# from model_utils.models import TimeStampedModel
# from audit_log.models import AuthStampedModel
from smart_selects.db_fields import ChainedForeignKey
from localflavor.us.models import PhoneNumberField
from sorl.thumbnail import ImageField

# My apps
from commons.models import PersonType
from people.models import Person, SupplierManager
from location.models import Country, Region, Province, Town


class SupplierType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Supplier Type"
        verbose_name_plural = "Supplier Types"

    def __unicode__(self):
        return self.name


class SupplierCompany(models.Model):
    name = models.CharField(max_length=60, unique=True)
    supplier_type = models.ForeignKey(SupplierType)
    address = models.CharField(max_length=100)
    country = models.ForeignKey(Country, default=1)
    region = models.ForeignKey(Region, default=1)
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region"
        )
    town = ChainedForeignKey(
        Town,
        chained_field="province",
        chained_model_field="province"
        )
    phone_number = PhoneNumberField(help_text='999-999-9999')
    email = models.EmailField(null=True, blank=True)
    company_logo = ImageField(
        upload_to='suppliers_logos',
        null=True,
        blank=True
        )

    def image_tag(self):
        return u'<img src="%s" />' % self.company_logo.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "Supplier Company"
        verbose_name_plural = "Supplier Companies"
        db_table = "suppliers_supplier_company"
        ordering = ['name']

    def __unicode__(self):
        return self.name


class SupplierContact(Person):
    objects = SupplierManager()
    supplier_company = models.ForeignKey(SupplierCompany)

    class Meta:
        verbose_name = "Supplier Contact"
        verbose_name_plural = "Supplier Contacts"

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Supplier")
        super(SupplierContact, self).save(*args, **kwargs)
