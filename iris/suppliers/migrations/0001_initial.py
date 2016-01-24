# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20160124_1129'),
        ('location', '0002_auto_20160120_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(default=1, to='location.Country')),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region')),
                ('region', models.ForeignKey(to='location.Region')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='SupplierContactAdditionalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Additional Field',
                'verbose_name_plural': 'Additional Fields',
            },
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'verbose_name': 'Supplier Type',
                'verbose_name_plural': 'Supplier Types',
            },
        ),
        migrations.CreateModel(
            name='SupplierContact',
            fields=[
            ],
            options={
                'verbose_name': 'Supplier Contact',
                'proxy': True,
                'verbose_name_plural': 'Supplier Contacts',
            },
            bases=('people.person',),
        ),
        migrations.AddField(
            model_name='suppliercontactadditionalfield',
            name='supplier_contact',
            field=models.OneToOneField(to='suppliers.SupplierContact'),
        ),
        migrations.AddField(
            model_name='suppliercontactadditionalfield',
            name='supplier_name',
            field=models.ForeignKey(to='suppliers.Supplier'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier_type',
            field=models.ForeignKey(to='suppliers.SupplierType'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province'),
        ),
    ]
