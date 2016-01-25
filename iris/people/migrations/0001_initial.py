# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import smart_selects.db_fields
import audit_log.models.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('names', models.CharField(max_length=100)),
                ('father_last_name', models.CharField(max_length=50)),
                ('mother_last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, choices=[('M', 'Male'), ('F', 'Female')])),
                ('birth_day', models.DateField()),
                ('document_id', models.CharField(help_text='000-0000000-0', max_length=22, null=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('picture', sorl.thumbnail.fields.ImageField(null=True, upload_to='people_pictures', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='active')),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_people_person_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('dependent_of', models.ForeignKey(blank=True, to='people.Person', null=True)),
                ('document_type', models.ForeignKey(to='commons.DocumentType', null=True)),
                ('kinship', models.ForeignKey(to='commons.Kinship', null=True)),
                ('marital_status', models.ForeignKey(to='commons.MaritalStatus')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_people_person_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
                ('nationality', models.ForeignKey(default=21, to='location.Nationality')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.CharField(max_length=20, null=True, blank=True)),
                ('apartment', models.CharField(max_length=20, null=True, blank=True)),
                ('street', models.CharField(max_length=40)),
                ('default', models.BooleanField(default=False, verbose_name='Default Address')),
                ('address_type', models.ForeignKey(to='location.AddressType')),
                ('country', models.ForeignKey(default=1, to='location.Country')),
                ('person_name', models.ForeignKey(to='people.Person')),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region')),
                ('region', models.ForeignKey(to='location.Region')),
                ('town', smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province')),
            ],
            options={
                'db_table': 'people_person_address',
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='commons.Phone')),
                ('default', models.BooleanField(default=False, verbose_name='default phone')),
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
            name='PersonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'people_person_type',
                'verbose_name': 'Person Type',
                'verbose_name_plural': 'Person Types',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.ForeignKey(to='people.PersonType', null=True),
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
