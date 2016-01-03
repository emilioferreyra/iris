# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_addresstype'),
        ('commons', '0009_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='document_id',
            field=models.CharField(max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='document_type',
            field=models.ForeignKey(to='commons.DocumentType', null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='marital_status',
            field=models.ForeignKey(to='commons.MaritalStatus', null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='nationality',
            field=models.ForeignKey(to='location.Nationality', null=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='document_type',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(max_length=20),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_type',
            field=models.ForeignKey(to='commons.PhoneType'),
        ),
    ]
