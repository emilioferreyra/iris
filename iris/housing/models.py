from django.db import models


class HousePart(models.Model):
    house_part = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ['id']
        db_table = 'housing_house_part'

    def __unicode__(self):
        return self.house_part


class HouseMaterial(models.Model):
    house_material = models.CharField(max_length=20)
    house_part = models.ForeignKey(HousePart)

    class Meta:
        unique_together = (('house_material', 'house_part'), )
        db_table = 'housing_house_material'

    def __unicode__(self):
        return '%s de %s' % (self.house_part, self.house_material)


class PropertyType(models.Model):
    property_type = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'housing_property_type'

    def __unicode__(self):
        return self.property_type
