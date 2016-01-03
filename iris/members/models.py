# Django core
from __future__ import absolute_import
from django.db import models
import datetime
from django.utils import timezone
# Third-party apps
from localflavor.us.models import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey
# My apps
from commons.models import ContactInfo, AcademicLevel, Kinship, Phone
from location.models import Address
from housing.models import HouseMaterial, HousePart, PropertyType


class Disability(models.Model):
    disability = models.CharField(unique=True, max_length=40)

    class Meta:
        verbose_name_plural = 'Disabilities'
        ordering = ['disability']

    def __unicode__(self):
        return self.disability


class Cane(models.Model):
    cane = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return str(self.cane)


class Member(ContactInfo):
    disability_type = models.ManyToManyField(Disability)
    cane_number = models.ForeignKey(Cane)
    # marital_status = models.ForeignKey(MaritalStatus)
    # nationality = models.ForeignKey(Nationality, default=21)
    academic_level = models.ForeignKey(AcademicLevel)
    property_type = models.ForeignKey(PropertyType)
    # document_type = models.ForeignKey(DocumentType)
    # document_id = models.CharField(max_length=22)
    # active = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s %s %s' % (self.names, self.father_name, self.mother_name)

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class Kinsman(ContactInfo):
    phone_number = PhoneNumberField()
    kinship = models.ForeignKey(Kinship)
    member = models.ForeignKey(Member)

    def __unicode__(self):
        return '%s %s' % (self.kinsman_name, self.kinsman_last_name)


class Housing(models.Model):
    member = models.ForeignKey(Member)
    house_part = models.ForeignKey(HousePart)
    house_material = ChainedForeignKey(
        HouseMaterial,
        chained_field="house_part",
        chained_model_field="house_part"
    )

    class Meta:
        unique_together = (('member', 'house_part'), )

    def __unicode__(self):
        return unicode(self.member)


class MemberAddress(Address):
    member_name = models.ForeignKey(Member)

    class Meta:
        db_table = 'members_address'
        verbose_name = "Address"
        verbose_name_plural = "Addreses"

    def __unicode__(self):
        pass


class MemberPhone(Phone):
    member_name = models.ForeignKey(Member, null=True)

    class META:
        db_table = 'members_phones'
        # verbose_name = "Member phone"
        verbose_name_plural = "Member phones"

    def __unicode__(self):
        return '%s %s %s %s' % (
                self.names,
                self.father_name,
                self.mother_name,
                self.phone_number
            )
