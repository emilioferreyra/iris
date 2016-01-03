# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_remove_contactinfo_active'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_level', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'members_academic_level',
            },
        ),
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
            name='HouseMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'members_house_material',
            },
        ),
        migrations.CreateModel(
            name='HousePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_part', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'house_part', to='members.HouseMaterial', chained_field=b'house_part')),
                ('house_part', models.ForeignKey(to='members.HousePart')),
            ],
        ),
        migrations.CreateModel(
            name='Kinship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kinship', models.CharField(unique=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Kinsman',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.ContactInfo')),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
                ('kinship', models.ForeignKey(to='members.Kinship')),
            ],
            bases=('commons.contactinfo',),
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marital_status', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'members_marital_status',
                'verbose_name_plural': 'Marital Status',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.ContactInfo')),
                ('document_id', models.CharField(max_length=22)),
                ('active', models.BooleanField(default=True)),
                ('academic_level', models.ForeignKey(to='members.AcademicLevel')),
                ('cane_number', models.ForeignKey(to='members.Cane')),
                ('disability_type', models.ManyToManyField(to='members.Disability')),
                ('document_type', models.ForeignKey(to='commons.DocumentType')),
                ('marital_status', models.ForeignKey(to='members.MaritalStatus')),
                ('nationality', models.ForeignKey(default=21, to='location.Nationality')),
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
                ('country_name', models.ForeignKey(to='location.Country')),
                ('member_name', models.ForeignKey(to='members.Member')),
                ('province_name', models.ForeignKey(to='location.Province')),
                ('region_name', models.ForeignKey(to='location.Region')),
                ('town_name', models.ForeignKey(to='location.Town')),
            ],
            options={
                'db_table': 'members_address',
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_type', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'members_property_type',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='property_type',
            field=models.ForeignKey(to='members.PropertyType'),
        ),
        migrations.AddField(
            model_name='kinsman',
            name='member_name',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AddField(
            model_name='housing',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AddField(
            model_name='housematerial',
            name='house_part',
            field=models.ForeignKey(to='members.HousePart'),
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([('member', 'house_part')]),
        ),
        migrations.AlterUniqueTogether(
            name='housematerial',
            unique_together=set([('house_material', 'house_part')]),
        ),
    ]
