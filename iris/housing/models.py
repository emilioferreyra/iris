# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class HousePart(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ['id']
        db_table = 'housing_house_part'

    def __unicode__(self):
        return self.name


# House parts variables
ceilling, wall, floor = 1, 2, 3


class CeillingManager(models.Manager):
    def get_queryset(self):
        return super(CeillingManager, self).\
            get_queryset().filter(house_part_id=ceilling)


class WallManager(models.Manager):
    def get_queryset(self):
        return super(WallManager, self).\
            get_queryset().filter(house_part_id=wall)


class FloorManager(models.Manager):
    def get_queryset(self):
        return super(FloorManager, self).\
            get_queryset().filter(house_part_id=floor)


class HouseMaterial(models.Model):
    ceilling = CeillingManager()
    wall = WallManager()
    floor = FloorManager()
    house_part = models.ForeignKey(HousePart)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = (('name', 'house_part'), )
        db_table = 'housing_house_material'
        ordering = ['id']

    def __unicode__(self):
        return '%s of %s' % (self.house_part, self.name)


class HouseMaterialCeilling(HouseMaterial):
    objects = CeillingManager()

    class Meta:
        verbose_name = "HouseMaterialCeilling"
        verbose_name_plural = "HouseMaterialCeillings"
        proxy = True


class HouseMaterialWall(HouseMaterial):
    objects = WallManager()

    class Meta:
        verbose_name = "HouseMaterialWall"
        verbose_name_plural = "HouseMaterialWalls"
        proxy = True


class HouseMaterialFloor(HouseMaterial):
    objects = FloorManager()

    class Meta:
        verbose_name = "HouseMaterialFloor"
        verbose_name_plural = "HouseMaterialFloors"
        proxy = True


class PropertyType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'housing_property_type'

    def __unicode__(self):
        return self.name
