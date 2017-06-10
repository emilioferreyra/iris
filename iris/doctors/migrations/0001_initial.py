# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20160611_1610'),
        ('people', '0013_auto_20170608_1535'),
        ('suppliers', '0004_auto_20160625_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appointment_date', models.DateField(verbose_name='fecha de cita')),
                ('symptomatology', models.TextField(max_length=300, verbose_name='sintomatolog\xeda')),
                ('prescription', models.TextField(max_length=300, null=True, verbose_name='prescripci\xf3n', blank=True)),
                ('date_next_appoitment', models.DateField(null=True, verbose_name='fecha de pr\xf3xima cita', blank=True)),
            ],
            options={
                'verbose_name': 'Cita M\xe9dica',
                'verbose_name_plural': 'Citas M\xe9dicas',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='people.Person')),
            ],
            options={
                'verbose_name': 'M\xe9dico',
                'verbose_name_plural': 'M\xe9dicos',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Medicina',
                'verbose_name_plural': 'Medicinas',
            },
        ),
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(default=1, verbose_name='cantidad')),
                ('unit', models.CharField(max_length=1, verbose_name='unidad', choices=[('G', 'Gotas'), ('P', 'Pildoras'), ('S', 'Cucharada')])),
                ('frecuency', models.FloatField(default=1, verbose_name='frecuencia')),
                ('frecuency_unit', models.CharField(max_length=1, verbose_name='unidade de frecuencia', choices=[('H', 'Cada Hora'), ('D', 'Al D\xeda')])),
                ('appointment', models.ForeignKey(to='doctors.Appointment')),
                ('medicine', models.ForeignKey(verbose_name='medicamento', to='doctors.Medicine')),
            ],
            options={
                'db_table': 'doctors_prescribed_medicines',
                'verbose_name': 'Medicina prescrita',
                'verbose_name_plural': 'Medicinas prescritas',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Cl\xednica',
                'proxy': True,
                'verbose_name_plural': 'Cl\xednicas',
            },
            bases=('suppliers.suppliercompany',),
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ManyToManyField(to='doctors.Clinic', verbose_name='cl\xednicas'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialities',
            field=models.ManyToManyField(to='doctors.Speciality', verbose_name='especialidades'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(verbose_name='cl\xednica', to='doctors.Clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='clinic', to='doctors.Doctor', chained_field='clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='member',
            field=models.ForeignKey(verbose_name='miembro', to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('member', 'doctor', 'appointment_date')]),
        ),
    ]
