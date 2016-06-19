# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import localflavor.us.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_auto_20160611_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suppliercompany',
            options={'ordering': ['name'], 'verbose_name': 'Empresa Suplidora', 'verbose_name_plural': 'Empresas Suplidoras'},
        ),
        migrations.AlterModelOptions(
            name='suppliercontact',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='suppliertype',
            options={'ordering': ['name'], 'verbose_name': 'Tipo de Suplidor', 'verbose_name_plural': 'Tipos de Suplidores'},
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='address',
            field=models.CharField(max_length=100, verbose_name='direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='company_logo',
            field=sorl.thumbnail.fields.ImageField(upload_to='suppliers_logos', null=True, verbose_name='logo de la empresa', blank=True),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='country',
            field=models.ForeignKey(default=1, verbose_name='pa\xeds', to='location.Country'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='name',
            field=models.CharField(unique=True, max_length=60, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20, verbose_name='n\xfamero de tel\xe9fono'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region', verbose_name='provincia'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='region',
            field=models.ForeignKey(default=1, verbose_name='regi\xf3n', to='location.Region'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='supplier_type',
            field=models.ForeignKey(verbose_name='tipo de suplidor', to='suppliers.SupplierType'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province', verbose_name='municipio'),
        ),
    ]
