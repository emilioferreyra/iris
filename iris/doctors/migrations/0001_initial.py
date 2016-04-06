# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160215_2303'),
        ('members', '0003_auto_20160403_1220'),
        ('suppliers', '0004_auto_20160131_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appointment_date', models.DateField(default=datetime.date(2016, 4, 3))),
                ('symptomatology', models.TextField(max_length=300)),
                ('prescription', models.TextField(max_length=300, null=True, blank=True)),
                ('date_next_appoitment', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='people.Person')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=('people.person',),
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
                ('unit', models.CharField(max_length=1, choices=[('G', 'Gout'), ('P', 'Pill'), ('S', 'Spoon')])),
                ('frecuency', models.FloatField(default=1)),
                ('frecuency_unit', models.CharField(max_length=1, choices=[('H', 'By Hour'), ('D', 'By Day')])),
                ('appointment', models.ForeignKey(to='doctors.Appointment')),
                ('medicine', models.ForeignKey(to='doctors.Medicine')),
            ],
            options={
                'db_table': 'doctors_prescribed_medicines',
                'verbose_name': 'Prescribed Medicine',
                'verbose_name_plural': 'Prescribed Medicines',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
            ],
            options={
                'verbose_name': 'Speciality',
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Clinic',
                'proxy': True,
                'verbose_name_plural': 'Clinics',
            },
            bases=('suppliers.suppliercompany',),
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ManyToManyField(to='doctors.Clinic'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialities',
            field=models.ManyToManyField(to='doctors.Speciality'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(to='doctors.Clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='clinic', to='doctors.Doctor', chained_field='clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('member', 'doctor', 'appointment_date')]),
        ),
    ]
