# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160215_2303'),
        ('housing', '0006_auto_20160403_1217'),
        ('commons', '0005_auto_20160216_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Disabilities',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ceiling', models.ForeignKey(to='housing.HouseMaterialCeiling')),
                ('floor', models.ForeignKey(to='housing.HouseMaterialFloor')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='people.Person')),
                ('member_number', models.IntegerField(default=members.models.number, unique=True)),
                ('currently_works', models.BooleanField(default=False)),
                ('where_work', models.CharField(max_length=100, null=True, blank=True)),
                ('observations', models.TextField(null=True, blank=True)),
                ('is_mother', models.BooleanField(default=False)),
                ('academic_level', models.ForeignKey(to='commons.AcademicLevel')),
                ('cane_number', models.ForeignKey(to='members.Cane')),
                ('disabilities', models.ManyToManyField(to='members.Disability')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Ocupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'db_table': 'members_ocupation',
                'verbose_name': 'Occupation',
                'verbose_name_plural': 'Occupations',
            },
        ),
        migrations.CreateModel(
            name='MemberFamily',
            fields=[
            ],
            options={
                'verbose_name': 'Member Family',
                'proxy': True,
                'verbose_name_plural': 'Member Families',
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='member',
            name='ocupation',
            field=models.ForeignKey(blank=True, to='members.Ocupation', null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='member_name',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AddField(
            model_name='house',
            name='property_type',
            field=models.ForeignKey(to='housing.PropertyType'),
        ),
        migrations.AddField(
            model_name='house',
            name='wall',
            field=models.ForeignKey(to='housing.HouseMaterialWall'),
        ),
    ]
