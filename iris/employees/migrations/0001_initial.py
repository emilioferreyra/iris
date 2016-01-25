# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='EmployeeAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hiring_date', models.DateField()),
                ('salary', models.FloatField()),
                ('contract_termination_date', models.DateField(null=True, blank=True)),
                ('department', models.ForeignKey(to='employees.Department')),
            ],
            options={
                'db_table': 'employees_employee_additional_fields',
                'verbose_name': 'Employee Additional Field',
                'verbose_name_plural': 'Employee Additional Fields',
            },
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'employees_employee_type',
                'verbose_name': 'Employee Type',
                'verbose_name_plural': 'Employee Types',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('department', models.ForeignKey(to='employees.Department')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Workday',
                'verbose_name_plural': 'Workdays',
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('workdays', models.ManyToManyField(to='employees.Workday')),
            ],
            options={
                'db_table': 'employees_work_schedule',
                'verbose_name': 'Work Schedule',
                'verbose_name_plural': 'Work Schedules',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'verbose_name': 'Employee',
                'proxy': True,
                'verbose_name_plural': 'Employees',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='EmployeeFamily',
            fields=[
            ],
            options={
                'verbose_name': 'Employee Family',
                'proxy': True,
                'verbose_name_plural': 'Employee Families',
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='employeeadditionalfield',
            name='employee',
            field=models.OneToOneField(to='employees.Employee'),
        ),
        migrations.AddField(
            model_name='employeeadditionalfield',
            name='employee_type',
            field=models.ForeignKey(to='employees.EmployeeType'),
        ),
        migrations.AddField(
            model_name='employeeadditionalfield',
            name='position',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='department', to='employees.Position', chained_field='department'),
        ),
        migrations.AddField(
            model_name='employeeadditionalfield',
            name='workSchedule',
            field=models.ForeignKey(to='employees.WorkSchedule'),
        ),
    ]
