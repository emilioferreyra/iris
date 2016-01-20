from django.db import models

# from commons.models import PersonType
from people.models import Person


class Doctor(Person):

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        proxy = True

    def save(self, *args, **kwargs):
        self.person_type = 'D'
        super(Doctor, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Dr. %s %s %s' % (
            self.names,
            self.father_last_name,
            self.mother_last_name
        )
