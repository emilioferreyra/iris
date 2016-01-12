# Django core
from __future__ import absolute_import
from django.db import models
import datetime
from django.utils import timezone
# Third-party apps
from smart_selects.db_fields import ChainedForeignKey
# My apps
from people.models import Person
from housing.models import HouseMaterial, HousePart, PropertyType


class Disability(models.Model):
    name = models.CharField(unique=True, max_length=40)

    class Meta:
        verbose_name_plural = 'Disabilities'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Cane(models.Model):
    name = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return str(self.name)


class Member(Person):

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'M'
        super(Member, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class MemberAdditionalField(models.Model):
    member_name = models.OneToOneField(Member)
    disabilities = models.ManyToManyField(Disability)
    cane_number = models.ForeignKey(Cane)
    property_type = models.ForeignKey(PropertyType)
    observations = models.TextField()

    class Meta:
        verbose_name = "Additional Field"
        verbose_name_plural = "Additional Fields"
        db_table = "members_member_additional_fields"

    def __unicode__(self):
        return '%s %s %s' % (
            self.member_name,
            self.cane_number,
            self.property_type
        )


class Housing(models.Model):
    member_name = models.ForeignKey(Member)
    house_part = models.ForeignKey(HousePart)
    house_material = ChainedForeignKey(
        HouseMaterial,
        chained_field="house_part",
        chained_model_field="house_part"
    )

    class Meta:
        unique_together = (('member_name', 'house_part'), )

    def __unicode__(self):
        return '%s %s %s' % (
            self.member_name,
            self.house_part,
            self.house_material
        )
