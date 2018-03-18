# -*- coding: utf-8 -*-
# Python core modules
from __future__ import absolute_import
from __future__ import unicode_literals

# Django modules
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class HousePart(models.Model):
    """
        Stores House Parts.
        Related to model: :model:`housing.HouseMaterial`.
    """
    name = models.CharField(
        unique=True,
        max_length=20,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Parte de la vivienda"
        verbose_name_plural = "Partes de la vivienda"
        ordering = ['id']
        db_table = 'housing_house_part'

    def __unicode__(self):
        return self.name


# House parts dictionary:
d = dict(ceiling=1, wall=2, floor=3)


class CeilingManager(models.Manager):
    """
        Manage ceiling part to define new query set,
        filtered by "ceiling".
    """
    def get_queryset(self):
        return super(CeilingManager, self).\
            get_queryset().filter(house_part_id=d['ceiling'])


class WallManager(models.Manager):
    """
        Manage wall part to define new query set,
        filtered by "wall".
    """
    def get_queryset(self):
        return super(WallManager, self).\
            get_queryset().filter(house_part_id=d['wall'])


class FloorManager(models.Manager):
    """
        Manage floor part to define new query set,
        filtered by "floor".
    """
    def get_queryset(self):
        return super(FloorManager, self).\
            get_queryset().filter(house_part_id=d['floor'])


@python_2_unicode_compatible
class HouseMaterial(models.Model):
    """
        Store House Material. Related to model:
        :model:`housing.HousePart`.
    """
    name = models.CharField(
        max_length=20,
        verbose_name="nombre"
    )
    house_part = models.ForeignKey(
        HousePart,
        verbose_name="parte de casa"
    )

    # ceiling = CeilingManager()
    # wall = WallManager()
    # floor = FloorManager()

    class Meta:
        verbose_name = "Material de la vivienda"
        verbose_name_plural = "Martiales de la vivienda"
        db_table = 'housing_house_material'
        ordering = ['id']

    def __str__(self):
        return self.name


class HouseMaterialCeiling(HouseMaterial):
    """
        Stores House Material Ceiling.
        Related model:
        :model:`housing.HousePart` and
        :model:`members.House`
    """
    objects = CeilingManager()

    class Meta:
        verbose_name = "Material del Techo"
        verbose_name_plural = "Materiales del Techo"
        proxy = True


class HouseMaterialWall(HouseMaterial):
    """
        Stores House Material Wall.
        Related Model:
        :model:`housing.HousePart` and
        :model:`members.House`
    """
    objects = WallManager()

    class Meta:
        verbose_name = "Material de la pared"
        verbose_name_plural = "Materiales de la pared"
        proxy = True


class HouseMaterialFloor(HouseMaterial):
    """
        Stores House Material Floor.
        Related Model:
        :model:`housing.HousePart` and
        :model:`members.House`
    """
    objects = FloorManager()

    class Meta:
        verbose_name = "Material del piso"
        verbose_name_plural = "Materiales del piso"
        proxy = True


@python_2_unicode_compatible
class PropertyType(models.Model):
    """
        Stores Property types like own, rented and so on.
        Related model:
        :model:`members.House`.
    """
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nombre"
    )

    class Meta:
        verbose_name = "Tipo de propiedad"
        verbose_name_plural = "Tipos de propiedades"
        ordering = ['id']
        db_table = 'housing_property_type'

    def __str__(self):
        return self.name
