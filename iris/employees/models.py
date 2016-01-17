from django.db import models

# from commons.models import PersonType
from people.models import Person, PersonAddress, PersonPhone


class Employee(Person):

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'E'
        super(Employee, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (self.names, self.father_name, self.mother_name)


class EmployeeAddress(PersonAddress):

    class Meta:
        verbose_name = "Employee Address"
        verbose_name_plural = "Employee Addreses"
        proxy = True

    def __unicode__(self):
        pass


class EmployeePhone(PersonPhone):

    class Meta:
        verbose_name = "Employee Phone"
        verbose_name_plural = "Employee Phones"
        proxy = True

    def __unicode__(self):
        pass
