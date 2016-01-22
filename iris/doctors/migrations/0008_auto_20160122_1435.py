# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160120_2007'),
        ('doctors', '0007_auto_20160122_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('symptomatology', models.TextField(max_length=300)),
                ('date_next_appoitment', models.DateField()),
                ('clinic', models.ForeignKey(to='doctors.Clinic')),
                ('doctor', models.ForeignKey(to='doctors.Doctor')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
            },
        ),
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(default=1)),
                ('unit', models.CharField(max_length=1, choices=[(b'G', b'Gout'), (b'P', b'Pill'), (b'S', b'Spoon')])),
                ('frecuency', models.FloatField(default=1)),
                ('frecuency_unit', models.CharField(max_length=1, choices=[(b'H', b'By Hour'), (b'D', b'By Day')])),
                ('appointment', models.ForeignKey(to='doctors.Appointment')),
                ('medicine', models.ForeignKey(to='doctors.Medicine')),
            ],
            options={
                'db_table': 'doctors_prescribed_medicines',
                'verbose_name': 'Prescription',
                'verbose_name_plural': 'Prescriptions',
            },
        ),
        migrations.AlterModelTable(
            name='doctoradditionalfield',
            table='doctors_doctor_additional_fields',
        ),
    ]
