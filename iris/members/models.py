# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Q, Max
from django.shortcuts import get_object_or_404

from commons.models import PersonType
from commons.models import AcademicLevel
from people.models import Person
from people.models import MemberManager
from people.models import MemberFamilyManager
from housing.models import PropertyType
from housing.models import HouseMaterialCeiling
from housing.models import HouseMaterialWall
from housing.models import HouseMaterialFloor


@python_2_unicode_compatible
class Disability(models.Model):
    """
        Store member's disabilities.
        Related model:
        :model:`members.Member`.
    """
    name = models.CharField(unique=True, max_length=40)

    class Meta:
        verbose_name_plural = 'Disabilities'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Cane(models.Model):
    """
        Store member's cane number.
        Related model:
        :model:`members.Member`.
    """
    name = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)


@python_2_unicode_compatible
class Occupation(models.Model):
    """
        Store member's occupations.
        Related model:
        :model:`members.Member`.
    """
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "Occupations"
        db_table = "members_occupation"

    def __str__(self):
        return self.name


def number():
    """
    Returns sequential number to be used like member_number field
    in Member model.
    """
    no = Member.objects.aggregate(Max('member_number'))
    value = no.values()[0]
    if value is None:
        return 1
    else:
        return value + 1

"""
Children dictionary to be used in member_is_mother
and children_quantity functions.
"""

d = dict(son=3, daughter=4)


class Member(Person):
    """
        Stores members information.
        Related model:
        :model:`commons.AcademicLevel`,
        :model:`doctors.Appointment`,
        :model:`members.Cane`,
        :model:`auth.User`,
        :model:`people.Person`,
        :model:`members.Disability`,
        :model:`commons.DocumentType`,
        :model:`members.House`,
        :model:`commons.Kinship`,
        :model:`commons.MaritalStatus`,
        :model:`location.Nationality`,
        :model:`members.Occupation`,
        :model:`commons.PersonType`,
        :model:`people.PersonAddress` and
        :model:`people.PersonPhone`.
    """
    objects = MemberManager()
    member_number = models.IntegerField(unique=True, default=number)
    disabilities = models.ManyToManyField(Disability)
    cane_number = models.ForeignKey(Cane)
    academic_level = models.ForeignKey(AcademicLevel)
    currently_works = models.BooleanField(default=False)
    occupation = models.ForeignKey(Occupation, null=True, blank=True)
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
        """
        Modify original save method to make the field person_type
        equal to "member" by default when registry is saved.
        """
        # self.person_type = PersonType.objects.get(name="Member")
        self.person_type = get_object_or_404(PersonType, name="Member")
        super(Member, self).save(*args, **kwargs)

    def member_is_mother(self):
        """
        If member has child and his gender is equal to "F" (woman).
        :return: A boolean that indicated if the member is a mother.
        """
        is_mother = self.is_mother
        children = Person.member_families.filter(
            Q(dependent_of=self.id),
            Q(kinship=d['son']) | Q(kinship=d['daughter'])
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
            Q(kinship=d['son']) | Q(kinship=d['daughter'])
        ).count()
        return quantity

    # children_quantity.admin_order_field = 'children_number'
    children_quantity.short_description = 'Children number'

    def was_created_recently(self):
        """
        This method indicate if the registry was created recently.
        Its used in admin site.
        :return: Date that was created.
        """
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


@python_2_unicode_compatible
class House(models.Model):
    """
        Stores the House whit other information.
        Related model:
        :model:`housing.HouseMaterialCeiling`,
        :model:`housing.HouseMaterialFloor`,
        :model:`members.Member`,
        :model:`housing.PropertyType` and
        :model:`housing.HouseMaterialWall`.
    """
    member_name = models.ForeignKey(Member)
    property_type = models.ForeignKey(PropertyType)
    ceiling = models.ForeignKey(HouseMaterialCeiling)
    wall = models.ForeignKey(HouseMaterialWall)
    floor = models.ForeignKey(HouseMaterialFloor)

    def __str__(self):
        return '%s %s' % (self.member_name, self.property_type)


class MemberFamily(Person):
    """
        Stores Member's families.
        Related model:
        :model:`auth.User`,
        :model:`people.Person`,
        :model:`commons.DocumentType`,
        :model:`commons.Kinship`,
        :model:`commons.MaritalStatus`,
        :model:`location.Nationality`,
        :model:`commons.PersonType`,
        :model:`people.PersonAddress` and
        :model:`people.PersonPhone`.
    """
    objects = MemberFamilyManager()

    class Meta:
        verbose_name = "Member Family"
        verbose_name_plural = "Member Families"
        proxy = True

    def save(self, *args, **kwargs):
        """
        Modify original save method to make the field person_type
        equal to "member_family" by default when the registry is saved.
        """
        # self.person_type = PersonType.objects.get(id=6)
        self.person_type = get_object_or_404(PersonType, name="Member")
        super(MemberFamily, self).save(*args, **kwargs)
