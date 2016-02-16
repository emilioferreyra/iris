# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Q, Max

# Third-party apps
# from smart_selects.db_fields import ChainedForeignKey
# My apps
from commons.models import PersonType, AcademicLevel
from people.models import Person, MemberManager, MemberFamilyManager
from housing.models import PropertyType, HouseMaterialCeilling,\
    HouseMaterialWall, HouseMaterialFloor


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


class Ocupation(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name = "Ocupation"
        verbose_name_plural = "Ocupations"

    def __unicode__(self):
        return self.name


def number():
    no = Member.objects.aggregate(Max('member_number'))
    value = no.values()[0]
    if value is None:
        return 1
    else:
        return value + 1

"""
Children variables declaration to be used in member_is_mother
and children_quantity functions.
"""

son, daughter = 3, 4


class Member(Person):
    objects = MemberManager()
    member_number = models.IntegerField(unique=True, default=number)
    disabilities = models.ManyToManyField(Disability)
    cane_number = models.ForeignKey(Cane)
    academic_level = models.ForeignKey(AcademicLevel)
    currently_works = models.BooleanField(default=False)
    ocupation = models.ForeignKey(Ocupation, null=True, blank=True)
    where_work = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    observations = models.TextField(null=True, blank=True)
    is_mother = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Member")
        super(Member, self).save(*args, **kwargs)

    def member_is_mother(self):
        is_mother = self.is_mother
        children = Person.member_families.filter(
            Q(dependent_of=self.id),
            Q(kinship=son) | Q(kinship=daughter)
        ).count()
        if children > 0 and self.gender == 'F':
            Member.objects.filter(id=self.id).update(is_mother=True)
        if children == 0 and self.gender == 'F':
            Member.objects.filter(id=self.id).update(is_mother=False)
        return is_mother

    member_is_mother.admin_order_field = 'is_mother'
    member_is_mother.boolean = True
    member_is_mother.short_description = 'Is mother'

    def children_quantity(self):
        quantity = Person.member_families.filter(
            Q(dependent_of=self.id),
            Q(kinship=son) | Q(kinship=daughter)
        ).count()
        return quantity

    # children_quantity.admin_order_field = 'children_number'
    children_quantity.short_description = 'Children number'

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class House(models.Model):
    member_name = models.ForeignKey(Member)
    property_type = models.ForeignKey(PropertyType)
    ceilling = models.ForeignKey(HouseMaterialCeilling)
    wall = models.ForeignKey(HouseMaterialWall)
    floor = models.ForeignKey(HouseMaterialFloor)

    def __unicode__(self):
        return '%s %s' % (self.member_name, self.property_type)


class MemberFamily(Person):
    objects = MemberFamilyManager()

    class Meta:
        verbose_name = "Member Family"
        verbose_name_plural = "Member Families"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = PersonType.objects.get(name="Member Family")
        super(MemberFamily, self).save(*args, **kwargs)


"""

Academic level report:

from django.db.models import Count
from members.models import Member

field = 'academic_level__name'
for i in Member.objects.order_by(field).values(field).annotate(al_count=Count(field)):
...     print i

"""