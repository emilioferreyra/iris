# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0017_contactinfo_active'),
        ('location', '0002_addresstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=20)),
                ('apartment', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=40)),
                ('address_type', models.ForeignKey(to='location.AddressType', null=True)),
                ('country_name', models.ForeignKey(to='location.Country')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.ContactInfo')),
                ('academic_level', models.ForeignKey(to='commons.AcademicLevel')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=('commons.contactinfo',),
        ),
        migrations.CreateModel(
            name='DoctorPhones',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.Phone')),
                ('doctor', models.ForeignKey(to='doctors.Doctor')),
            ],
            bases=('commons.phone',),
        ),
        migrations.CreateModel(
            name='MedicalSpeciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speciality_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Medical speciality',
                'verbose_name_plural': 'Medical specialities',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality_name',
            field=models.ManyToManyField(to='doctors.MedicalSpeciality'),
        ),
        migrations.AddField(
            model_name='address',
            name='doctor',
            field=models.ForeignKey(to='doctors.Doctor'),
        ),
        migrations.AddField(
            model_name='address',
            name='province_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region_name', to='location.Province', chained_field=b'region_name'),
        ),
        migrations.AddField(
            model_name='address',
            name='region_name',
            field=models.ForeignKey(to='location.Region'),
        ),
        migrations.AddField(
            model_name='address',
            name='town_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province_name', to='location.Town', chained_field=b'province_name'),
        ),
    ]
