# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_auto_20160611_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='employeefamily',
            options={'verbose_name': 'Familiar', 'verbose_name_plural': 'Familiares'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['name'], 'verbose_name': 'Posici\xf3n', 'verbose_name_plural': 'Posiciones'},
        ),
        migrations.AlterModelOptions(
            name='positionlevel',
            options={'ordering': ['name'], 'verbose_name': 'Nivel de posici\xf3n', 'verbose_name_plural': 'Niveles de posiciones'},
        ),
        migrations.AlterModelOptions(
            name='workday',
            options={'ordering': ['id'], 'verbose_name': 'D\xeda Laborable', 'verbose_name_plural': 'D\xedas laborables'},
        ),
        migrations.AlterModelOptions(
            name='workschedule',
            options={'verbose_name': 'Calendario de Trabajo', 'verbose_name_plural': 'Calendarios de Trabajos'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='academic_level',
            field=models.ForeignKey(verbose_name='nivel acad\xe9mico', to='commons.AcademicLevel'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contract_termination_date',
            field=models.DateField(help_text='Introduzca la fecha de terminaci\xf3n del contrato', null=True, verbose_name='fecha terminaci\xf3n contrato', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(verbose_name='departamento', to='employees.Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.ForeignKey(verbose_name='tipo de empleado', to='employees.EmployeeType'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hiring_date',
            field=models.DateField(help_text='Ingrese la fecha de contrataci\xf3n', verbose_name='fecha contrataci\xf3n'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='department', to='employees.Position', chained_field='department', verbose_name='posici\xf3n'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(verbose_name='salario'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='workSchedule',
            field=models.ForeignKey(verbose_name='calendario trabajo', to='employees.WorkSchedule', help_text='Seleccione calendario de trabajo'),
        ),
        migrations.AlterField(
            model_name='position',
            name='department',
            field=models.ForeignKey(verbose_name='departamento', to='employees.Department'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_level',
            field=models.ForeignKey(verbose_name='nivel', to='employees.PositionLevel', null=True),
        ),
        migrations.AlterField(
            model_name='positionlevel',
            name='description',
            field=models.TextField(max_length=45, unique=True, null=True, verbose_name='descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='positionlevel',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='workday',
            name='name',
            field=models.CharField(unique=True, max_length=10, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='workschedule',
            name='end_hour',
            field=models.TimeField(verbose_name='hora fin'),
        ),
        migrations.AlterField(
            model_name='workschedule',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='workschedule',
            name='start_hour',
            field=models.TimeField(verbose_name='hora inicio'),
        ),
        migrations.AlterField(
            model_name='workschedule',
            name='workdays',
            field=models.ManyToManyField(to='employees.Workday', verbose_name='d\xedas laborables'),
        ),
    ]
