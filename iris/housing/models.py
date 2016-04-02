# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class HousePart(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ['id']
        db_table = 'housing_house_part'

    def __unicode__(self):
        return self.name


# House parts dictionary:
d = dict(ceilling=1, wall=2, floor=3)


class CeillingManager(models.Manager):
    def get_queryset(self):
        return super(CeillingManager, self).\
            get_queryset().filter(house_part_id=d['ceilling'])


class WallManager(models.Manager):
    def get_queryset(self):
        return super(WallManager, self).\
            get_queryset().filter(house_part_id=d['wall'])


class FloorManager(models.Manager):
    def get_queryset(self):
        return super(FloorManager, self).\
            get_queryset().filter(house_part_id=d['floor'])


@python_2_unicode_compatible
class HouseMaterial(models.Model):
    ceilling = CeillingManager()
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


class HouseMaterialCeilling(HouseMaterial):
    objects = CeillingManager()

    class Meta:
        verbose_name = "House Material Ceilling"
        verbose_name_plural = "House Material Ceillings"
        proxy = True


class HouseMaterialWall(HouseMaterial):
    objects = WallManager()

    class Meta:
        verbose_name = "House Material Wall"
        verbose_name_plural = "House Material Walls"
        proxy = True


class HouseMaterialFloor(HouseMaterial):
    objects = FloorManager()

    class Meta:
        verbose_name = "House Material  Floor"
        verbose_name_plural = "House Material Floors"
        proxy = True


@python_2_unicode_compatible
class PropertyType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'housing_property_type'

    def __str__(self):
        return self.name
