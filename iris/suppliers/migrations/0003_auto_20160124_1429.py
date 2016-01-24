# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160120_1658'),
        ('suppliers', '0002_auto_20160124_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(default=1, to='location.Country')),
                ('province', smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', to='location.Province', chained_field='region')),
                ('region', models.ForeignKey(to='location.Region')),
                ('supplier_type', models.ForeignKey(to='suppliers.SupplierType')),
                ('town', smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', to='location.Town', chained_field='province')),
            ],
            options={
                'verbose_name': 'Supplier Company',
                'verbose_name_plural': 'Supplier Companies',
            },
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='country',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='province',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='region',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_type',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='town',
        ),
        migrations.AlterField(
            model_name='contactadditionalfield',
            name='supplier_name',
            field=models.ForeignKey(to='suppliers.SupplierCompany'),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
