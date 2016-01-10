# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
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
                'db_table': 'commons_academic_level',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('names', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('document_id', models.CharField(max_length=22)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_type', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'db_table': 'commons_document_type',
                'verbose_name': 'Document Type',
                'verbose_name_plural': 'Documents types',
            },
        ),
        migrations.CreateModel(
            name='Kinship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kinship', models.CharField(unique=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marital_status', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'commons_marital_status',
                'verbose_name_plural': 'Marital status',
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_type', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'commons_person_type',
                'verbose_name': 'Person Type',
                'verbose_name_plural': 'Person Types',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_type', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'commons_phone_type',
            },
        ),
        migrations.AddField(
            model_name='phone',
            name='phone_type',
            field=models.ForeignKey(to='commons.PhoneType'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='document_type',
            field=models.ForeignKey(to='commons.DocumentType'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='marital_status',
            field=models.ForeignKey(to='commons.MaritalStatus'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='nationality',
            field=models.ForeignKey(to='location.Nationality'),
        ),
    ]
