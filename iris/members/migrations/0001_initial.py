# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('housing', '0001_initial'),
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
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field='house_part', to='housing.HouseMaterial', chained_field='house_part')),
                ('house_part', models.ForeignKey(to='housing.HousePart')),
            ],
        ),
        migrations.CreateModel(
            name='MemberAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currently_works', models.BooleanField(default=False)),
                ('where_work', models.CharField(max_length=100, null=True, blank=True)),
                ('observations', models.TextField(null=True, blank=True)),
                ('cane_number', models.ForeignKey(to='members.Cane')),
                ('disabilities', models.ManyToManyField(to='members.Disability')),
            ],
            options={
                'db_table': 'members_member_additional_fields',
                'verbose_name': 'Additional Field',
                'verbose_name_plural': 'Additional Fields',
            },
        ),
        migrations.CreateModel(
            name='Ocupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Ocupation',
                'verbose_name_plural': 'Ocupations',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
            ],
            options={
                'verbose_name': 'Member',
                'proxy': True,
                'verbose_name_plural': 'Members',
            },
            bases=('people.person',),
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
            model_name='memberadditionalfield',
            name='member_name',
            field=models.OneToOneField(to='members.Member'),
        ),
        migrations.AddField(
            model_name='memberadditionalfield',
            name='ocupation',
            field=models.ForeignKey(blank=True, to='members.Ocupation', null=True),
        ),
        migrations.AddField(
            model_name='memberadditionalfield',
            name='property_type',
            field=models.ForeignKey(to='housing.PropertyType'),
        ),
        migrations.AddField(
            model_name='house',
            name='member_name',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='house',
            unique_together=set([('member_name', 'house_part')]),
        ),
    ]
