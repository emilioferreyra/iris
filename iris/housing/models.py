from django.db import models


class HousePart(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ['id']
        db_table = 'housing_house_part'

    def __unicode__(self):
        return self.name


class HouseMaterial(models.Model):
    house_part = models.ForeignKey(HousePart)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = (('name', 'house_part'), )
        db_table = 'housing_house_material'

    def __unicode__(self):
        return '%s of %s' % (self.house_part, self.name)


class PropertyType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ['id']
        db_table = 'housing_property_type'

    def __unicode__(self):
        return self.name
