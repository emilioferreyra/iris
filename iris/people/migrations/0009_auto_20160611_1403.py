# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import smart_selects.db_fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160215_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='personaddress',
            options={'verbose_name': 'Direcci\xf3n', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='personphone',
            options={'verbose_name': 'Tel\xe9fono', 'verbose_name_plural': 'Tel\xe9fonos'},
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_day',
            field=models.DateField(help_text='Introduzca Fecha de nacimiento', verbose_name='Fecha nacimiento'),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_id',
            field=models.CharField(help_text='Introduzca el n\xfamero de documento', max_length=22, null=True, verbose_name='documento identidad'),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_type',
            field=models.ForeignKey(verbose_name='tipo documento identidad', to='commons.DocumentType', help_text='Seleccione el tipo de documento de identidad', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='father_last_name',
            field=models.CharField(help_text='Apellido del padre', max_length=50, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1, null=True, verbose_name='g\xe9nero', choices=[('M', 'Masculino'), ('F', 'Femenino')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='kinship',
            field=models.ForeignKey(verbose_name='parentezco', to='commons.Kinship', help_text='Seleccione parentezco', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='marital_status',
            field=models.ForeignKey(verbose_name='estado civil', to='commons.MaritalStatus', help_text='Seleccione estado civil'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother_last_name',
            field=models.CharField(help_text='Apellido de la madre', max_length=50, null=True, verbose_name='Apellido Materno', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='names',
            field=models.CharField(help_text='Introduzca Nombres', max_length=100, verbose_name='nombres'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationality',
            field=models.ForeignKey(default=21, verbose_name='nacionalidad', to='location.Nationality', help_text='Seleccione nacionalidad'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.ForeignKey(verbose_name='tipo de persona', to='commons.PersonType', help_text='Seleccione tipo de persona', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(upload_to='people_pictures', null=True, verbose_name='fotograf\xeda', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='address_type',
            field=models.ForeignKey(verbose_name='tipo direcci\xf3n', to='location.AddressType', help_text='Seleccione tipo de direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='apartment',
            field=models.CharField(help_text='Escriba n\xfamero de apartamento', max_length=20, null=True, verbose_name='apartamento', blank=True),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='building',
            field=models.CharField(max_length=20, null=True, verbose_name='edificio', blank=True),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='country',
            field=models.ForeignKey(default=1, verbose_name='pa\xeds', to='location.Country', help_text='Seleccione pa\xeds'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='direcci\xf3n principal'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', chained_field='region', verbose_name='provincia', to='location.Province', help_text='Seleccione provincia'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='region',
            field=models.ForeignKey(verbose_name='regi\xf3n', to='location.Region', help_text='Seleccione regi\xf3n'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='street',
            field=models.CharField(help_text='Escriba nombre de calle', max_length=40, verbose_name='calle'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', chained_field='province', verbose_name='municipio', to='location.Town', help_text='Seleccione municipio'),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='tel\xe9fono principal'),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20, verbose_name='n\xfamero de tel\xe9fono'),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='phone_type',
            field=models.ForeignKey(verbose_name='tipo de tel\xe9fono', to='commons.PhoneType'),
        ),
    ]
