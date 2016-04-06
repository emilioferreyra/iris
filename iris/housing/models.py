# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class HousePart(models.Model):
    """
        Stores House Parts.
        Related to model: :model:`housing.HouseMaterial`.
    """
    name = models.CharField(unique=True, max_length=20)

    class Meta:
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
    ceiling = CeilingManager()
    wall = WallManager()
    floor = FloorManager()
    house_part = models.ForeignKey(HousePart)
    name = models.CharField(max_length=20)

    class Meta:
        # unique_together = (('name', 'house_part'), )
        db_table = 'housing_house_material'
        ordering = ['id']

    def __str__(self):
        return '%s of %s' % (self.house_part, self.name)


class HouseMaterialCeiling(HouseMaterial):
    """
        Stores House Material Ceiling.
        Related model:
        :model:`housing.HousePart` and
        :model:`members.House`
    """
    objects = CeilingManager()

    class Meta:
        verbose_name = "House Material Ceiling"
        verbose_name_plural = "House Material Ceilings"
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
        verbose_name = "House Material Wall"
        verbose_name_plural = "House Material Walls"
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
        verbose_name = "House Material  Floor"
        verbose_name_plural = "House Material Floors"
        proxy = True


@python_2_unicode_compatible
class PropertyType(models.Model):
    """
        Stores Property types like own, rented and so on.
        Related model:
        :model:`members.House`.
    """
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'housing_property_type'

    def __str__(self):
        return self.name
