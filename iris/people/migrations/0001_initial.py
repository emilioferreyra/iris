# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('names', models.CharField(max_length=100)),
                ('father_last_name', models.CharField(max_length=50)),
                ('mother_last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birth_day', models.DateField()),
                ('document_id', models.CharField(help_text=b'000-0000000-0', max_length=22, null=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('person_type', models.CharField(max_length=1, null=True, choices=[(b'E', b'Employee'), (b'M', b'Member'), (b'D', b'Doctor'), (b'S', b'Supplier'), (b'K', b'Kinsman')])),
                ('status', models.BooleanField(default=True)),
                ('document_type', models.ForeignKey(to='commons.DocumentType', null=True)),
                ('kinship', models.ForeignKey(to='commons.Kinship', null=True)),
                ('marital_status', models.ForeignKey(to='commons.MaritalStatus')),
                ('nationality', models.ForeignKey(default=1, to='location.Nationality')),
                ('parent_of', models.ForeignKey(blank=True, to='people.Person', null=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=20, null=True, blank=True)),
                ('apartment', models.CharField(max_length=20, null=True, blank=True)),
                ('street', models.CharField(max_length=40)),
                ('address_type', models.ForeignKey(to='location.AddressType')),
                ('country', models.ForeignKey(to='location.Country')),
                ('person_name', models.ForeignKey(to='people.Person')),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', to='location.Province', chained_field=b'region')),
                ('region', models.ForeignKey(to='location.Region')),
                ('town', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='location.Town', chained_field=b'province')),
            ],
            options={
                'db_table': 'people_person_address',
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
        ),
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.Phone')),
                ('person_name', models.ForeignKey(to='people.Person')),
            ],
            options={
                'db_table': 'people_person_phone',
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
            },
            bases=('commons.phone',),
        ),
        migrations.CreateModel(
            name='Kinsman',
            fields=[
            ],
            options={
                'verbose_name': 'Kinsman',
                'proxy': True,
                'verbose_name_plural': 'Kinsmans',
            },
            bases=('people.person',),
        ),
    ]
