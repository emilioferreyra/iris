# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20160521_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Cita M\xe9dica', 'verbose_name_plural': 'Citas M\xe9dicas'},
        ),
        migrations.AlterModelOptions(
            name='clinic',
            options={'ordering': ['name'], 'verbose_name': 'Cl\xednica', 'verbose_name_plural': 'Cl\xednicas'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'M\xe9dico', 'verbose_name_plural': 'M\xe9dicos'},
        ),
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Medicina', 'verbose_name_plural': 'Medicinas'},
        ),
        migrations.AlterModelOptions(
            name='prescribedmedicine',
            options={'verbose_name': 'Medicina prescrita', 'verbose_name_plural': 'Medicinas prescritas'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name': 'Especialidad', 'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(verbose_name='fecha de cita'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='clinic',
            field=models.ForeignKey(verbose_name='cl\xednica', to='doctors.Clinic'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_next_appoitment',
            field=models.DateField(null=True, verbose_name='fecha de pr\xf3xima cita', blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='member',
            field=models.ForeignKey(verbose_name='miembro', to='members.Member'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(max_length=300, null=True, verbose_name='prescripci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='symptomatology',
            field=models.TextField(max_length=300, verbose_name='sintomatolog\xeda'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='clinic',
            field=models.ManyToManyField(to='doctors.Clinic', verbose_name='cl\xednicas'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialities',
            field=models.ManyToManyField(to='doctors.Speciality', verbose_name='especialidades'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='frecuency',
            field=models.FloatField(default=1, verbose_name='frecuencia'),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='frecuency_unit',
            field=models.CharField(max_length=1, verbose_name='unidade de frecuencia', choices=[('H', 'Cada Hora'), ('D', 'Al D\xeda')]),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='medicine',
            field=models.ForeignKey(verbose_name='medicamento', to='doctors.Medicine'),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='quantity',
            field=models.FloatField(default=1, verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='unit',
            field=models.CharField(max_length=1, verbose_name='unidad', choices=[('G', 'Gotas'), ('P', 'Pildoras'), ('S', 'Cucharada')]),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(unique=True, max_length=60, verbose_name='nombre'),
        ),
    ]
