# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import sorl.thumbnail.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20160611_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='nombre')),
                ('address', models.CharField(max_length=100, verbose_name='direcci\xf3n')),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20, verbose_name='n\xfamero de tel\xe9fono')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True)),
                ('company_logo', sorl.thumbnail.fields.ImageField(upload_to='suppliers_logos', null=True, verbose_name='logo de la empresa', blank=True)),
                ('country', models.ForeignKey(default=1, verbose_name='pa\xeds', to='location.Country')),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region', verbose_name='provincia')),
                ('region', models.ForeignKey(default=1, verbose_name='regi\xf3n', to='location.Region')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'suppliers_supplier_company',
                'verbose_name': 'Empresa Suplidora',
                'verbose_name_plural': 'Empresas Suplidoras',
            },
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Tipo de Suplidor',
                'verbose_name_plural': 'Tipos de Suplidores',
            },
        ),
        migrations.AddField(
            model_name='suppliercompany',
            name='supplier_type',
            field=models.ForeignKey(verbose_name='tipo de suplidor', to='suppliers.SupplierType'),
        ),
        migrations.AddField(
            model_name='suppliercompany',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province', verbose_name='municipio'),
        ),
    ]
