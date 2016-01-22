# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160120_2007'),
        ('doctors', '0003_auto_20160121_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
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
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=1, choices=[(b'G', b'Gout'), (b'P', b'Pill'), (b'S', b'Spoon')])),
                ('frecuency', models.IntegerField()),
                ('frecuency_unit', models.CharField(max_length=1, choices=[(b'H', b'By Hour'), (b'D', b'By Day')])),
                ('appointment', models.ForeignKey(to='appointments.Appointment')),
                ('medicine', models.ForeignKey(to='appointments.Medicine')),
            ],
            options={
                'db_table': 'appointments_prescribed_medicines',
                'verbose_name': 'Prescribed Medicine',
                'verbose_name_plural': 'Prescribed Medicines',
            },
        ),
    ]
