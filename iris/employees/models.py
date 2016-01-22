# -*- coding: utf-8 -*-
# Django core
from __future__ import absolute_import, unicode_literals
# from django.db import models

# from commons.models import PersonType
from people.models import Person


class Employee(Person):

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'E'
        super(Employee, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )
