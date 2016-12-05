# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20160625_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True)),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20, null=True, verbose_name='tel\xe9fono', blank=True)),
                ('extension_number', models.PositiveSmallIntegerField(null=True, verbose_name='extensi\xf3n', blank=True)),
                ('movil_number', localflavor.us.models.PhoneNumberField(max_length=20, null=True, verbose_name='m\xf3vil', blank=True)),
                ('supplier_company', models.ForeignKey(to='suppliers.SupplierCompany')),
            ],
            options={
                'db_table': 'suppliers_contact',
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]
