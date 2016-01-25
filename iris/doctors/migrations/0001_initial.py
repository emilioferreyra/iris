# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('members', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
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
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=150, null=True, blank=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20, null=True, blank=True)),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region')),
                ('region', models.ForeignKey(default=1, to='location.Region', null=True)),
                ('town', smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Clinic',
                'verbose_name_plural': 'Clinics',
            },
        ),
        migrations.CreateModel(
            name='DoctorAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clinic', models.ManyToManyField(to='doctors.Clinic')),
            ],
            options={
                'db_table': 'doctors_doctor_additional_fields',
                'verbose_name': 'Doctor Additional Field',
                'verbose_name_plural': 'Doctor Additional Fields',
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
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Speciality',
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'verbose_name': 'Doctor',
                'proxy': True,
                'verbose_name_plural': 'Doctors',
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='doctoradditionalfield',
            name='doctor',
            field=models.OneToOneField(to='doctors.Doctor'),
        ),
        migrations.AddField(
            model_name='doctoradditionalfield',
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
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='clinic', to='doctors.DoctorAdditionalField', chained_field='clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
    ]
