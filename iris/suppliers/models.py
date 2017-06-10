# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
# from django.shortcuts import get_object_or_404

from smart_selects.db_fields import ChainedForeignKey
from sorl.thumbnail import ImageField
from localflavor.us.models import PhoneNumberField

# from commons.models import PersonType
# from people.models import Person
# from people.models import SupplierManager
from location.models import Country, Region, Province, Town

supplier_id = 4


@python_2_unicode_compatible
class SupplierType(models.Model):
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de Suplidor"
        verbose_name_plural = "Tipos de Suplidores"
        db_table = "suppliers_type"
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SupplierCompany(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        verbose_name="nombre"
    )
    supplier_type = models.ForeignKey(
        SupplierType,
        verbose_name="tipo de suplidor"
    )
    address = models.CharField(
        max_length=100,
        verbose_name="dirección"
    )
    country = models.ForeignKey(
        Country,
        default=1,
        verbose_name="país"
    )
    region = models.ForeignKey(
        Region,
        verbose_name="región",
        default=1
    )
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region",
        verbose_name="provincia",
        default=29
    )
    town = ChainedForeignKey(
        Town,
        chained_field="province",
        chained_model_field="province",
        verbose_name="municipio",
        default=203
    )
    phone_number = PhoneNumberField(
        verbose_name="número de teléfono",
        help_text='999-999-9999'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name="e-mail"
    )
    company_logo = ImageField(
        upload_to='suppliers_logos',
        null=True,
        blank=True,
        verbose_name="logo de la empresa"
    )

    class Meta:
        verbose_name = "Empresa Suplidora"
        verbose_name_plural = "Empresas Suplidoras"
        db_table = "suppliers_company"
        ordering = ['name']

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.company_logo:
            return u'<img src="%s" width="100" height="75" />' \
                % self.company_logo.url
        else:
            return ' '

    image_tag.short_description = 'Logo'
    image_tag.allow_tags = True
    image_tag.admin_order_field = 'name'


@python_2_unicode_compatible
class SupplierContact(models.Model):
    supplier_company = models.ForeignKey(SupplierCompany)
    name = models.CharField("nombre", max_length=100)
    email = models.EmailField("e-mail", null=True, blank=True)
    phone_number = PhoneNumberField(
        "teléfono",
        null=True,
        blank=True
    )
    extension_number = models.PositiveSmallIntegerField(
        "número de extensión",
        null=True,
        blank=True
    )
    mobile_number = PhoneNumberField("teléfono móvil", null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        db_table = "suppliers_contact"

    def __str__(self):
        return "%s, %s" % (self.supplier_company, self.name)
