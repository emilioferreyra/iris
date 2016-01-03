# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20160103_1139'),
        ('commons', '0017_contactinfo_active'),
        ('location', '0002_addresstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cane', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disability', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'ordering': ['disability'],
                'verbose_name_plural': 'Disabilities',
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'house_part', to='housing.HouseMaterial', chained_field=b'house_part')),
                ('house_part', models.ForeignKey(to='housing.HousePart')),
            ],
        ),
        migrations.CreateModel(
            name='Kinsman',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.ContactInfo')),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('kinship', models.ForeignKey(to='commons.Kinship')),
            ],
            bases=('commons.contactinfo',),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.ContactInfo')),
                ('academic_level', models.ForeignKey(to='commons.AcademicLevel')),
                ('cane_number', models.ForeignKey(to='members.Cane')),
                ('disability_type', models.ManyToManyField(to='members.Disability')),
                ('property_type', models.ForeignKey(to='housing.PropertyType')),
            ],
            bases=('commons.contactinfo',),
        ),
        migrations.CreateModel(
            name='MemberAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=20)),
                ('apartment', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=40)),
                ('address_type', models.ForeignKey(to='location.AddressType', null=True)),
                ('country_name', models.ForeignKey(to='location.Country')),
                ('member_name', models.ForeignKey(to='members.Member')),
                ('province_name', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region_name', to='location.Province', chained_field=b'region_name')),
                ('region_name', models.ForeignKey(to='location.Region')),
                ('town_name', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province_name', to='location.Town', chained_field=b'province_name')),
            ],
            options={
                'db_table': 'members_address',
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.Phone')),
                ('member_name', models.ForeignKey(to='members.Member', null=True)),
            ],
            bases=('commons.phone',),
        ),
        migrations.AddField(
            model_name='kinsman',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AddField(
            model_name='housing',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([('member', 'house_part')]),
        ),
    ]
