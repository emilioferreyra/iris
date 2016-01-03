from django.db import models
import datetime
from django.utils import timezone
from localflavor.us.models import PhoneNumberField
from commons.models import DocumentType, ContactInfo, AcademicLevel, PhoneType
from location.models import Nationality, Address
from smart_selects.db_fields import ChainedForeignKey


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


class MaritalStatus(models.Model):
    marital_status = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'members_marital_status'
        verbose_name_plural = 'Marital status'
        ordering = ['id']

    def __unicode__(self):
        return self.marital_status


class PropertyType(models.Model):
    property_type = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'members_property_type'

    def __unicode__(self):
        return self.property_type


class Member(ContactInfo):
    disability_type = models.ManyToManyField(Disability)
    cane_number = models.ForeignKey(Cane)
    marital_status = models.ForeignKey(MaritalStatus)
    nationality = models.ForeignKey(Nationality, default=21)
    academic_level = models.ForeignKey(AcademicLevel)
    property_type = models.ForeignKey(PropertyType)
    document_type = models.ForeignKey(DocumentType)
    document_id = models.CharField(max_length=22)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.person)

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class Kinship(models.Model):
    kinship = models.CharField(unique=True, max_length=45)

    def __unicode__(self):
        return self.kinship


class Kinsman(ContactInfo):
    phone_number = PhoneNumberField()
    kinship = models.ForeignKey(Kinship)
    member_name = models.ForeignKey(Member)

    def __unicode__(self):
        return '%s %s' % (self.kinsman_name, self.kinsman_last_name)


class HousePart(models.Model):
    house_part = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.house_part


class HouseMaterial(models.Model):
    house_material = models.CharField(max_length=20)
    house_part = models.ForeignKey(HousePart)

    class Meta:
        unique_together = (('house_material', 'house_part'), )
        db_table = 'members_house_material'

    def __unicode__(self):
        return '%s de %s' % (self.house_part, self.house_material)


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


class Phone(models.Model):
    phone_number = PhoneNumberField()
    phone_type = models.ForeignKey(PhoneType)

    def __unicode__(self):
        return self.phone
