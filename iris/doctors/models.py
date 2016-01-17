from django.db import models

# from commons.models import PersonType
from people.models import Person, PersonAddress, PersonPhone


class Doctor(Person):

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'D'
        super(Doctor, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s %s' % (self.names, self.father_name, self.mother_name)


class DoctorAddress(PersonAddress):

    class Meta:
        verbose_name = "Doctor Address"
        verbose_name_plural = "Doctor Addreses"
        proxy = True

    def __unicode__(self):
        pass


class DoctorPhone(PersonPhone):

    class Meta:
        verbose_name = "Doctor Phone"
        verbose_name_plural = "Doctor Phones"
        proxy = True

    def __unicode__(self):
        pass
