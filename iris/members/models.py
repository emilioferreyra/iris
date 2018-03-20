# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Q, Max

from commons.models import PersonType
from commons.models import AcademicLevel
from people.models import Person
from people.models import MemberManager
from people.models import MemberFamilyManager
from housing.models import PropertyType
from housing.models import HouseMaterialCeiling
from housing.models import HouseMaterialWall
from housing.models import HouseMaterialFloor


member = 2
member_family = 6


@python_2_unicode_compatible
class Diagnosis(models.Model):
    """
    Store member's disabilities.
    Related model:
    :model:`members.Member`.
    """
    name = models.CharField(
        unique=True,
        max_length=40,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Diagnostico"
        verbose_name_plural = "Diagnosticos"
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
    name = models.PositiveIntegerField(
        verbose_name="número de bastón"
    )

    class Meta:
        verbose_name = "Bastón"
        verbose_name_plural = "Bastones"
        ordering = ['id']

    def __str__(self):
        return str(self.name)


@python_2_unicode_compatible
class WorkPlace(models.Model):
    """
    Store member's work place
    """
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = "Lugar de trabajo"
        verbose_name_plural = "Lugares de trabajo"
        ordering = ['id']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Occupation(models.Model):
    """
    Store member's occupations.
    Related model:
    :model:`members.Member`.
    """
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Ocupación"
        verbose_name_plural = "Ocupaciones"
        db_table = "members_occupation"
        ordering = ['id']

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


# Children dictionary to be used in member_is_mother
# and children_quantity functions.


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
    member_number = models.IntegerField(
        unique=True,
        default=number,
        verbose_name="número de miembro"
    )
    diagnosis = models.ManyToManyField(
        Diagnosis,
        verbose_name="Diagnosticos"
    )
    cane_number = models.ForeignKey(
        Cane,
        verbose_name="número de bastón"
    )
    academic_level = models.ForeignKey(
        AcademicLevel,
        verbose_name="nivel académico",
        help_text="Seleccione nivel académico"
    )
    currently_works = models.BooleanField(
        default=False,
        verbose_name="trabaja actualmente",
        help_text="Indique si actualmente tiene trabajo"
    )
    occupation = models.ManyToManyField(
        Occupation,
        verbose_name="Ocupación(es)",
        help_text="Seleccione ocupación",
        blank=True
    )
    where_work = models.ForeignKey(
        WorkPlace,
        verbose_name="Lugar donde trabaja",
        null=True
    )
    # where_work = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True,
    #     verbose_name="Donde trabaja",
    #     help_text="Empresa o lugar donde trabaja"
    # )
    observations = models.TextField(
        null=True,
        blank=True,
        verbose_name="Observaciones",
        help_text="Escribir observaciones adicionales"
    )
    is_mother = models.BooleanField(
        default=False,
        verbose_name="Es madre",
    )
    health_insurance = models.BooleanField(
        default=False,
        verbose_name="Seguro de Salud"
    )
    children_quantity = models.PositiveIntegerField(
        verbose_name="Cantidad de hijos",
        null=True
    )
    objects = MemberManager()

    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['-id']

    # class ReportBuilder:
    #     # exclude = ()  # Lists or tuple of excluded fields
    #     fields = (
    #         'names',
    #         'father_last_name',
    #         'mother_last_name',
    #         'gender',
    #         'birthday',
    #         'marital_status',
    #         'document_type',
    #         'document_id',
    #         'email',
    #         'kinship',
    #         'picture',
    #         'status',
    #         'age',
    #         'main_location',
    #         'academic_level',
    #     )  # Explicitly allowed fields
        # extra = ()  # List extra fields (useful for methods)

    def save(self, *args, **kwargs):
        """
        Modify original save method to make the field person_type
        equal to "member" by default when registry is saved.
        """
        self.person_type = PersonType.objects.get(id=member)
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
    member_is_mother.short_description = 'Madre'

    def get_children_quantity(self):
        q = Person.member_families.filter(
            Q(dependent_of=self.id),
            Q(kinship=d['son']) | Q(kinship=d['daughter'])
        ).count()
        if q > 0:
            Member.objects.filter(id=self.id).update(children_quantity=q)
        return q

    # children_quantity.admin_order_field = 'children_number'
    get_children_quantity.short_description = 'Cantidad de hijos'

    def was_created_recently(self):
        """
        This method indicate if the registry was created recently.
        Its used in admin site.
        :return: Date that was created.
        """
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Creado recientemente?'


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
    property_type = models.ForeignKey(
        PropertyType,
        verbose_name="Tipo de propiedad",
        help_text="Seleccione tipo de propiedad"
    )
    ceiling = models.ForeignKey(
        HouseMaterialCeiling,
        verbose_name="techo",
        help_text="Seleccione techo"
    )
    wall = models.ForeignKey(
        HouseMaterialWall,
        verbose_name="pared",
        help_text="Seleccione pared"
    )
    floor = models.ForeignKey(
        HouseMaterialFloor,
        verbose_name="piso",
        help_text="Seleccione piso"
    )

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Características de la Vivienda"

    def __str__(self):
        return "%s" % (str(self.property_type))


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
        verbose_name = "Familiar del miembro"
        verbose_name_plural = "Familiares del miembro"
        proxy = True

    def save(self, *args, **kwargs):
        """
        Modify original save method to make the field person_type
        equal to "member_family" by default when the registry is saved.
        """
        self.person_type = PersonType.objects.get(id=member_family)
        super(MemberFamily, self).save(*args, **kwargs)
