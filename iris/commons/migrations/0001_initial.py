# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
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
                ('name', models.CharField(unique=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'commons_marital_status',
                'verbose_name_plural': 'Marital status',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text=b'999-999-9999', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
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
    ]
