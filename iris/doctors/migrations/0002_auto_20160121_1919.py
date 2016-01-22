# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Clinic',
                'verbose_name_plural': 'Clinics',
            },
        ),
        migrations.CreateModel(
            name='DoctorAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clinic', models.ForeignKey(to='doctors.Clinic')),
                ('doctor', models.OneToOneField(to='doctors.Doctor')),
            ],
            options={
                'verbose_name': 'Doctor Additional Field',
                'verbose_name_plural': 'Doctor Additional Fields',
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
        migrations.AddField(
            model_name='doctoradditionalfield',
            name='specialities',
            field=models.ManyToManyField(to='doctors.Speciality'),
        ),
    ]
