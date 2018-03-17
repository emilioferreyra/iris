# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0016_auto_20170609_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document_id',
            field=models.CharField(help_text='Introduzca el n\xfamero de documento', max_length=22, null=True, verbose_name='documento identidad', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='document_type',
            field=models.ForeignKey(blank=True, to='commons.DocumentType', help_text='Seleccione el tipo de documento de identidad', null=True, verbose_name='tipo documento identidad'),
        ),
    ]
